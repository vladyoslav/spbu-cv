# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apk add --no-cache gcc libc-dev linux-headers
RUN pip3 install uwsgi

COPY . .

CMD ["uwsgi", "wsgi.ini"]