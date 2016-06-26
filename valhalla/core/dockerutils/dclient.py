
"""
This is a singleton patterns.
The benefit is that we only needs to import 
dclient into a module that will work with 
the docker client.

Ex:
from dclient import dclient as cli
"""
from sys import platform

is_linux = False

if "linux" in platform:
    from docker import Client
    cli = Client(base_url='unix://var/run/docker.sock')
    is_linux = True

else:
    import docker
    cli = docker.from_env(assert_hostname=False)

print("Platform: " + platform)

init_validate_containers = cli.containers(all=True)




