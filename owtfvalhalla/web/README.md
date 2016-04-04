
## JSON Rest API endpoints

List all containers

```bash
GET
container/
```

Info about image/container

```bash
GET
container/<IMAGE>/

Example:
/containers/owtfvalhallatestcontainer:0.1/
```

Build image

```bash
GET
container/<IMAGE>/build_image/

Example:
/containers/owtfvalhallatestcontainer:0.1/build_image/
```


Build container

```bash
GET
container/<IMAGE>/build_container/

Example:
/containers/owtfvalhallatestcontainer:0.1/build_container/
```

Start container

```bash
GET
container/<IMAGE>/start/

Example:
/containers/owtfvalhallatestcontainer:0.1/start/
```


Stop container

```bash
GET
container/<IMAGE>/stop/

Example:
/containers/owtfvalhallatestcontainer:0.1/stop/
```




