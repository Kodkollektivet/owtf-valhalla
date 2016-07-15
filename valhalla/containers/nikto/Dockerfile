FROM python:3.5

ADD . /owtf
WORKDIR /owtf

RUN apt-get update
RUN apt-get install unzip
RUN wget https://github.com/sullo/nikto/archive/master.zip
RUN ls
RUN unzip master.zip
ENV PATH /owtf/nikto-master/program:$PATH
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
