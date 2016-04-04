
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

    # workaround to make sure client and server uses the same api version
    # is there a better way to handle this? !help-wanted
    docker_version_bytes = subprocess.check_output(['docker','version'])
    api_version = docker_version_bytes.decode('utf-8').splitlines()[1][20:]

    cli = Client(base_url='unix://var/run/docker.sock', version=api_version)
else:
    import docker
    cli = docker.from_env(assert_hostname=False)

init_validate_containers = cli.containers(all=True)




