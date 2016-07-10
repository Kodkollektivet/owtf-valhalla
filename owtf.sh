#!/bin/bash

HELP_MSG="Usage: $0 {setup|start|test}"

VIRTUAL_ENV="venv/bin/activate"
MANAGE_PY="valhalla/django/manage.py"

function setup {
  printf "Creating virtual environment...\n\n"
  virtualenv --python=/usr/bin/python3 venv || virtualenv --python=/usr/local/bin/python3 venv
  source venv/bin/activate
  pip install -q --log-file logs/pip-error.log -r requirements.txt

  printf "\n'Taking care of things for you...' - Microsoft\n"
  python $MANAGE_PY makemigrations
  python $MANAGE_PY migrate
}

function init {
  if [ ! -e $VIRTUAL_ENV ]
    then
      printf "Could not find virtual environment at '$VIRTUAL_ENV'... \n"
      setup
  fi
  source venv/bin/activate
  printf "Virtual environment activated!\n"
}

function start {
  printf "Starting Offensive Web Testing Framework - Valhalla...\n"
  python $MANAGE_PY runserver 0.0.0.0:8000
}

function test {
  echo "Running nosetests..."
  #nosetests-2.7 -q -w test/
  #python -m unittest discover -v
  python $MANAGE_PY test -v 3 --with-doctest --exclude-dir=valhalla/containers --exclude-dir=valhalla/qt --with-coverage --cover-package=valhalla --doctest-options=+ELLIPSIS
}

function startqt {
  python -m valhalla.qt
}

if [[ $# > 2 ]]; then
  echo $HELP_MSG
  exit
fi

case "$1" in
  setup)
    setup
    ;;

  start)
    init
    if [ "$2" = "qt" ]; then
      startqt
    else
      start
    fi
    ;;

   test)
     init
     test
     ;;

   *)
     echo $HELP_MSG
     exit 1
esac
