FROM python:3.11
COPY . app

ENV HEROKU_LOGIN="telegram@sptm.dev"
ENV HEROKU_TOKEN="939c73a2-8c1a-42c6-a1e5-fc30a525f985"
ENV TG_API_KEY="5041121803:AAHYApDpcK4NN0o6avs33o5cTVUU7ALM42k"

RUN ./app/create-venv
CMD ./start
