all:
	python3 amiller_im.py

freeze:
	pip freeze > requirements.txt

env:
	virtualenv -p /usr/bin/python3.5 venv

run:
	honcho start

test:
	venv/bin/python -m unittest tests.test_amiller_im

deploy:
	ansible-playbook -i environment playbook.yml
