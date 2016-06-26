# OWTF-Valhalla

[![Travis](https://travis-ci.org/Kodkollektivet/owtf-valhalla.svg?branch=master)](https://travis-ci.org/Kodkollektivet/owtf-valhalla)

## This application is under heavy development

## Slack

You are more than welcome to join us in the Slack channel:

[https://owtfvalhalla.slack.com/](https://owtfvalhalla.slack.com/)


## Dependencies
* Python 2
* docker-py ^1.8
* django
* requests
* Docker server API version 1.22

At the moment docker-py have issues with Python 3.
As we heavily depend on that we need to be on Python 2 as for now. 

If you installed docker.io via apt-get, you may have an old version which is not compatible with docker-py. To check this run:
```bash
docker version
```
The output shows you what Server API version you are running.

---------------------------------------------------------------------------------

# Run

Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```bash
./owtf.sh setup         # Setup
./owtf.sh test          # Test
./owtf.sh start         # Start
```

Open browser and go to [http://127.0.0.1:8000/containers/](http://127.0.0.1:8000/containers/)

