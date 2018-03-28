all:
	python3 amiller_im.py

freeze:
	pip freeze > requirements.txt

venv:
	virtualenv -p `which python3` venv; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt;

run:
	honcho start

test:
	venv/bin/python -m unittest tests.test_amiller_im

deploy:
	ansible-playbook -i environment playbook.yml

docker-build:
	docker build -t amiller_im_test .

docker-run:
	docker run -d \
    -p 5000:5000 \
    --name=amiller_im_test \
    amiller_im_test:latest

docker-bash:
	docker exec \
	-i -t amiller_im_test /bin/bash

clean:
	rm -rf venv
