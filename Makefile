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

lint:
	venv/bin/python -m pylint app --errors-only

test:
	venv/bin/python -m unittest tests.test_amiller_im

boot-deploy:
	kubectl run amiller-im-py3 --image=gcr.io/${PROJECT_ID}/amiller-im-py3:v2 --port 8080

deploy:
	kubectl set image deployment/amiller-im-py3 amiller-im-py3=gcr.io/${PROJECT_ID}/amiller-im-py3:v2

docker: docker-build

docker-build:
	docker build -t gcr.io/${PROJECT_ID}/amiller-im-py3:v2 .

docker-run:
	docker run \
	--detach \
	--rm \
    --publish 8080:8080 \
    --name=amiller-im-py3 \
    gcr.io/${PROJECT_ID}/amiller-im-py3:v2

docker-bash:
	docker exec \
	-i -t amiller-im-py3 /bin/bash

docker-push:
	gcloud docker -- push gcr.io/${PROJECT_ID}/amiller-im-py3:v2

docker-stop:
	docker stop amiller-im-py3

ci-amiller-im: spruce-amiller-im fly-amiller-im

spruce-amiller-im:
	spruce merge ci/pipeline_amiller_im.yml > ci/compiled/compiled_pipeline_amiller_im.yml

fly-amiller-im:
	fly -t nuc set-pipeline -p amiller.im -c ci/compiled/compiled_pipeline_amiller_im.yml
	#fly -t vbox set-pipeline -p amiller.im -c ci/compiled/compiled_pipeline_amiller_im.yml

lb:
	kubectl expose deployment amiller-im-py3 --type=LoadBalancer --port 80 --target-port 8080

get-ext-ip:
	kubectl get service

clean-venv:
	rm -rf venv
