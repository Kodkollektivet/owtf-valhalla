FROM python:3.5

ADD . /owtf
WORKDIR /owtf

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]