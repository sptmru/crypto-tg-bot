FROM python:3.11

RUN mkdir /app
COPY . /app/

WORKDIR /app

ENV TELEGRAM_BOT_API_TOKEN=5041121803:AAHYApDpcK4NN0o6avs33o5cTVUU7ALM42k

RUN apt update && apt install python3-pip -y

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

CMD python main.py
