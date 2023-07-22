FROM python:3.10-slim

USER root
RUN apt-get update && apt-get install -y git

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt