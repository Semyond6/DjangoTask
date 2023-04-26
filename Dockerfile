FROM python:3.10-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

# copy project
COPY . .