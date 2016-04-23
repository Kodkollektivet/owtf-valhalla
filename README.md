# OWTF-Valhalla

## This application is under heavy development##

## Slack

You are more than welcome to join us in the Slack channel:

[https://owtfvalhalla.slack.com/](https://owtfvalhalla.slack.com/)


## Dependencies
* Python 2
* docker-py 1.8.0rc4
* django
* requests
* Docker server API version 1.22

At the moment docker-py have issues with Python 3.
As we heavily depend on that we need to be on Python 2
as for now. 

If you installed docker.io via apt-get, you may have an old version which is not compatible with docker-py. To check this run:
```bash
docker version
```
The output shows you what Server API version you are running.

## Run tests

Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Create a venv for the project.

```bash
virtualenv --python=/usr/bin/python venv
```

Activate the venv.
Make sure that the venv is Python 2!

```bash
source venv/bin/activate
```

Install requirements.

```bash
pip install -r requirements.txt
```

Run the tests

```bash
python -m unittest discover tests
```

Start Django web server

```bash
cd owtfvalhalla
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open browser and go to [http://127.0.0.1:8000/containers/](http://127.0.0.1:8000/containers/)

