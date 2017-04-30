all:
	python3 amiller_im.py

freeze:
	pip freeze > requirements.txt

env:
	virtualenv -p /usr/bin/python3.5 venv

s:
	$("source venv/bin/activate")

run:
	honcho start
