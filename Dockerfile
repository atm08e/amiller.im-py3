from ubuntu:18.04

# Needed
RUN apt-get -y update \
    && apt-get -y install \
    python3.6 \
    python3.6-dev \
    python3-pip \
    && apt-get autoremove \
    && mkdir -p /opt/amiller-im-py3

# Nice to have for DevOps
RUN apt-get -y install \
    vim \
    htop \
    netcat \
    && apt-get autoremove

COPY . /opt/amiller-im-py3

WORKDIR /opt/amiller-im-py3

RUN pip3 install \
    --no-cache-dir \
    -r requirements.txt

EXPOSE 8080
#EXPOSE 8081
#CMD python3 -m http.server 8080
CMD source .env; gunicorn app.gunicorn:app --worker-class aiohttp.worker.GunicornWebWorker --bind 0.0.0.0:8080
