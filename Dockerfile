FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y git

RUN apt-get install nodejs -y

RUN mkdir /store_monitoring

WORKDIR /store_monitoring

ADD requirements.txt requirements.txt

# Install python project requirements.
RUN pip install -r requirements.txt -U

COPY . .