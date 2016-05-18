import os

class DockerContainerException(Exception):
    def __init__(self, exceptionArgs):
        # maybe not the best way
        super(DockerContainerException, self).__init__("{}".format(exceptionArgs))
        self.message = os.path.basename(__file__).split('.')[0] +"::{0}".format(exceptionArgs)