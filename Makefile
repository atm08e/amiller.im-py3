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

clean:
	rm -rf venv
