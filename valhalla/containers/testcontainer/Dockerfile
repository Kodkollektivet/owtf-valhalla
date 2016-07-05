FROM python:3.5

ADD . /webapp
WORKDIR /webapp

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]