# OWTF-Valhalla

## This application is under heavy development

## Dependencies
* Python 2
* docker-py 1.8.0rc4
* django
* requests

At the moment docker-py have issues with Python 3.
As we heavily depend on that we need to be on Python 2
as for now.


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


## Todo

- [ ] Fix logging
- [ ] Get all basic container commands (start/stop/remove/build)
- [ ] What happens if the application craches?
