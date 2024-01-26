FROM python:3.11-slim-buster

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && pip cache purge

RUN mkdir /app
WORKDIR /app
COPY app/* /app/
