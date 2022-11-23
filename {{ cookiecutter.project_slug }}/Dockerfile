FROM python:3-alpine

mv /usr/src/app /usr/src/thingy

WORKDIR /usr/src/thingy

COPY app app
COPY bootstrap bootstrap
RUN pip install --no-cache-dir ./bootstrap

CMD [ "python", "bootstrap" ]