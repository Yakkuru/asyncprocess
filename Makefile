test:
	pip install -e .
	python test.py

clean:
	rm -rf asyncprocess.egg-info
	rm -rf build
	rm -rf dist

commit:
	python setup.py sdist bdist_wheel

push:
	twine upload dist/*