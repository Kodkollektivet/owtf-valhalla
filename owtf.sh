#!/bin/bash

HELP_MSG="Usage: $0 {setup|start|test}"

VIRTUAL_ENV="venv/bin/activate"
MANAGE_PY="core/manage.py"

function setup {
  printf "Creating virtual environment...\n\n"
  virtualenv --python=/usr/bin/python3 venv || virtualenv --python=/usr/local/bin/python3 venv
  source venv/bin/activate
  pip install -q --log-file log/pip-error.log -r requirements.txt

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
  python core/manage.py test
}

if [[ $# > 1 ]]; then
  echo $HELP_MSG
  exit
fi

case "$1" in
  setup)
    setup
    ;;

  start)
    init
    start
    ;;

   test)
     init
     test
     ;;

   *)
     echo $HELP_MSG
     exit 1
esac
