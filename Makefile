test:
	export PYTHONPATH=.; pytest
install:
	pip install -U pip setuptools
	pip install -r requirements.txt