test:
	pip install -e .
	python test.py

release:
	python setup.py sdist bdist_wheel

publish:
	twine upload dist/*