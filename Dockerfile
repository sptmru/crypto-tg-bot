FROM python:3.11
WORKDIR /application
COPY . /application

RUN apt update && apt install python3-pip -y

RUN pip3 install -U pip
RUN pip3 install -r /application/requirements.txt

CMD python main.py
