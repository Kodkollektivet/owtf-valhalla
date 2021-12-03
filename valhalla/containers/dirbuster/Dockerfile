FROM python:3.5

ADD . /owtf
WORKDIR /owtf

RUN apt-get update
RUN apt-get install unzip -y
RUN apt-get install openjdk-7-jdk -y
RUN wget http://downloads.sourceforge.net/dirbuster/DirBuster-0.12.zip
RUN unzip DirBuster-0.12.zip
RUN cp -r DirBuster-0.12/* ./
RUN pip install -r requirements.txt

#ENTRYPOINT ["python"]
#CMD ["app.py"]