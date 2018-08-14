FROM python:3.7.0-alpine3.8

# gcc needed for python3 Cryptography moduke
# musl-dev needed for #include <limit.h>
# libffi-dev needed for #include <ffi.h>
# openssl-dev need for #include <openssl/opensslv.h>
# make for uvloop compilation
RUN set -ex && \
    apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    make \
    && \
    pip install pipenv && \
    mkdir -p /opt/amiller-im-py3

COPY . /opt/amiller-im-py3

WORKDIR /opt/amiller-im-py3

RUN pipenv install --deploy --system

EXPOSE 8080

CMD source .env; gunicorn app.main:create_app --worker-class aiohttp.worker.GunicornWebWorker --bind 0.0.0.0:8080