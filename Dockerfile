FROM python:3.11

RUN mkdir /app
COPY . /app/

WORKDIR /app

RUN apt update && apt install python3-pip -y

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt