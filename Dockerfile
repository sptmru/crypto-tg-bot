FROM python:3.11
WORKDIR /application
COPY . /application

RUN /application/create-venv
CMD /application/start
