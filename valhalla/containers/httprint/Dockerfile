FROM python:3.5

ADD . /owtf
WORKDIR /owtf

RUN apt-get update
RUN apt-get install unzip -y
RUN wget http://www.net-square.com/_assets/httprint_linux_301.zip
RUN unzip httprint_linux_301.zip
ENV PATH /owtf/httprint_301/linux:$PATH
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]