FROM python:3.7.0-alpine3.8

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    && pip install pipenv \
    && mkdir -p /opt/amiller-im-py3
# gcc needed for python3 Cryptography moduke
# musl-dev needed for #include <limit.h>
# libffi-dev needed for #include <ffi.h>
# openssl-dev need for #include <openssl/opensslv.h>

COPY . /opt/amiller-im-py3

WORKDIR /opt/amiller-im-py3

RUN pipenv install

EXPOSE 8080
#EXPOSE 8081
#CMD python3 -m http.server 8080
CMD source .env; pipenv run gunicorn app.main:create_app --worker-class aiohttp.worker.GunicornWebWorker --bind 0.0.0.0:8080
