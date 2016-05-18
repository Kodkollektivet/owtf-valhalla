import os

class DockerImageException(Exception):
    def __init__(self, exceptionArgs):
        # maybe not the best way
        super(DockerImageException, self).__init__("{}".format(exceptionArgs))
        self.message = os.path.basename(__file__).split('.')[0] +"::{0}".format(exceptionArgs)