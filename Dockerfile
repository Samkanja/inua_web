FROM python:3.10-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /inua_web

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip



RUN pip install -r requirements.txt


COPY . .

