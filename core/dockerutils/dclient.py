
"""
This is a singleton patterns.
The benefit is that we only needs to import 
dclient into a module that will work with 
the docker client.

Ex:
from dclient import dclient as cli
"""
import subprocess
from sys import platform

if platform == "linux" or platform == "linux2":
    from docker import Client
    cli = Client(base_url='unix://var/run/docker.sock')
else:
    import docker
    cli = docker.from_env(assert_hostname=False)

init_validate_containers = cli.containers(all=True)




