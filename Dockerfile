FROM python:3.11

RUN mkdir /app
COPY . /app/

WORKDIR /app

RUN echo 'export FLYCTL_INSTALL="/root/.fly"' >> /root/bash_profile
RUN echo 'export PATH="$FLYCTL_INSTALL/bin:$PATH"' >> /root/bash_profile
RUN export /root/bash_profile

RUN apt update && apt install python3-pip -y

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

CMD python main.py
