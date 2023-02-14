FROM python:3.11
WORKDIR /application
COPY . /application


RUN python3.11 -m venv ./.venv \
RUN source ./.venv/bin/activate
RUN python -m pip install -U pip
RUN pip install -r requirements.txt

CMD python main.py
