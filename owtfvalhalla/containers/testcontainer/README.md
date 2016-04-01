To run do the following

```shell
# Build the image specified in the Dockerfile
$ docker build -t <iimage-name> . 

# Create a container from the image
# -d - deamonizes the container
# -p - exports port 5000 in the container port 5000
$ docker run -d -p 5000:5000 --name <container-name> <image-name>

# Start the container
$ docker start <container-name>

# Go to your localhost or docker-machine 5000

# Stop the container
$ docker kill <container-name>
```
