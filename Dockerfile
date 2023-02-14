FROM python:3.11
WORKDIR /application
COPY . /application

RUN python -m pip install -U pip
RUN pip install -r /application/requirements.txt

CMD python main.py
