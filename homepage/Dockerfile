FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update && apt-get install -y apt-utils

RUN apt install -y python3-pip openjdk-8-jdk

RUN mkdir /homepage

COPY requirements.txt /homepage/requirements.txt
COPY grade.py /homepage/grade.py

WORKDIR /homepage

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/homepage/grade.py", "/mounted"]
