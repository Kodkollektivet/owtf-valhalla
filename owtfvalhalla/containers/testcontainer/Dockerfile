FROM python:3.5
RUN apt-get update
RUN pip install --upgrade pip

ADD . /webapp
WORKDIR /webapp

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]