FROM python:3.5.2 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y libgeos-c1

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
