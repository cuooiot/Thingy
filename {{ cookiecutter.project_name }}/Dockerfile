FROM python:3-alpine

WORKDIR /usr/src

COPY app app
COPY bootstrap bootstrap
RUN pip install --no-cache-dir ./bootstrap

CMD [ "python", "bootstrap" ]