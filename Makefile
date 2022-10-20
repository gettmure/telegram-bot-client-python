build-client:
	python3 setup.py install

run-linter-all:
	autopep8 --in-place --aggressive --aggressive *.py
