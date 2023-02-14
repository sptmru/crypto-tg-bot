FROM python:3.11
WORKDIR /application
COPY . /application

RUN  -m pip install -U pip
RUN /usr/lib/python install -r /application/requirements.txt

CMD python main.py
