import os
import fnmatch
import threading
from queue import Queue
import time

from valhalla.dockerutils import OwtfContainer
from valhalla.middleman import send_for_execution
from valhalla.django.settings.settings import CONTAINER_DIR

qtowtfcontainers = []


class QtOwtfContainer(OwtfContainer):

    def __init__(self, owtf_image_path: str):
        super().__init__(owtf_image_path)
        self.build_thread = threading.Thread(target=self._build)
        self.execute_thread = threading.Thread(target=self._start_execute_thread)
        self.execute_queue = Queue(maxsize=0)  # Unlimited Queue
        self.results_lock = threading.Lock()
        self.is_built = True if self.is_image_built and self.is_container_built else False

    def _build(self):
        """Builds both image and container"""
        self.build_image()
        time.sleep(1)
        self.build_container()
        time.sleep(1)

    def build(self):
        """API call."""
        self.build_thread.start()
        time.sleep(1)
        del self.build_thread
        self.build_thread = threading.Thread(target=self._build)
        self.is_built = True

    def add_command(self, command):
        """Add command to execution queue."""
        self.execute_queue.put(command)

    def execute(self):
        """Start execute commands thread."""
        if self.execute_thread.is_alive():  # Already running
            return
        else:
            self.execute_thread.start()  # Start thread

    def _start_execute_thread(self):
        """Execute commands in queue."""
        while not self.execute_queue.empty():
            command = self.execute_queue.get(block=True)
            self._add_to_results(send_for_execution(self, command))
        del self.execute_thread
        self.execute_thread = threading.Thread(target=self._start_execute_thread)

    def _add_to_results(self, result):
        """Add to the results list."""
        self.results_lock.acquire()
        self.results.append(result)
        self.results_lock.release()

    def get_results(self) -> list:
        """Get command execution results."""
        self.results_lock.acquire()
        results = self.results
        self.results_lock.release()
        return results

    def remove(self):
        """Call the internal _remove_container and _remove_image"""
        self.stop()
        time.sleep(1)
        self._remove_container()
        time.sleep(1)
        self._remove_image()


def locate_owtf_containers(location=CONTAINER_DIR):
    """Locates the containers that lives inside of the container folder.
    The containers list the filled up with OwtfContainer objects.

    location is only used for testing.
    """
    for root, dirnames, filenames in os.walk(location):
        for filename in fnmatch.filter(filenames, 'config.json'):
            if 'Dockerfile' and 'config.json' in filenames:
                qtowtfcontainers.append(QtOwtfContainer(root))


locate_owtf_containers()


def get_owtf_c(image=None, image_id=None, container_id=None):
    """This is the facade to the outside.
    If get_owtf_c() with no arguments is called, returns all the containers
    If get_owtf_c(image=<IMAGE>), return that container
    If get_owtf_c(image=<IMAGE_ID>) if image is build, return that container
    If get_owtf_c(image=<CONTAINER_ID>) if container is buld, return that container

    Only one or no argument can be passed.

    Returns a tuple (bool, obj)
    bool = status
    obj = object
    """

    if image and image_id and container_id is not None:
        return False, ValueError("All params cant be set. Choose one of them of none.")

    elif image is not None:
        for img in qtowtfcontainers:
            if img.image == image:
                return True, img
        return False, None

    elif image_id is not None:
        for image in qtowtfcontainers:
            if image_id == image.image_id:
                return True, image
        return False, None

    elif container_id is not None:
        for container in qtowtfcontainers:
            if container_id == container.container_id:
                return True, container
        return False, None

    else:
        return True, qtowtfcontainers