# amiller.im-py3
amiller.im website source code

### Dependencies
python3.5 or python 3.6
python3-devel
redhat-rpm-config (Fedora)

### Installation
```bash
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements.txt
honcho start dev
```
This will start a development server which should auto reload the web application on code changes or alternatively to start a prod server
```bash
honcho start prod
```

### Tests
```bash
make test
```

