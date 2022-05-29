test:
	pip install -e .
	python test.py

commit:
	python setup.py sdist bdist_wheel

push:
	twine upload dist/*