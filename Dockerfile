FROM python:3.8-slim

ADD ./platform-dependencies/requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
