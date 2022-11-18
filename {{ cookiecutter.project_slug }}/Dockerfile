FROM python:3-alpine

WORKDIR /usr/src/app

COPY app .
RUN pip install --no-cache-dir ./bootstrap

CMD [ "python", "bootstrap" ]