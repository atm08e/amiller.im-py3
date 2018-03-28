from ubuntu:18.04

RUN apt-get -y update \
    && apt-get -y install \
    python3.6 \
    python3.6-dev \
    python3-pip

ADD ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD python SimpleHTTPServer
#CMD gunicorn app.gunicorn:app --worker-class aiohttp.worker.GunicornWebWorker --bind 127.0.0.1:5000
