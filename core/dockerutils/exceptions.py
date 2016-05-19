class DockerContainerException(Exception):
    def __init__(self, exception_message):
        super(DockerContainerException, self).__init__(exception_message)

class DockerImageException(Exception):
    def __init__(self, exception_message):
        super(DockerImageException, self).__init__(exception_message)
