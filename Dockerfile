from python:3.6.4

RUN pip install -r requirements

CMD gunicorn app.gunicorn:app --worker-class aiohttp.worker.GunicornWebWorker --bind 127.0.0.1:5000
