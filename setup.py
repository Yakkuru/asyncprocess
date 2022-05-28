from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Process managing async task'
LONG_DESCRIPTION = 'Simple package that help you isolate your code in async task and run them on a single process with asyncio.'

setup(
    name="asyncprocess",
    version=VERSION,
    author="Marc-Antoine St-Pierre",
    author_email="<yakinquiries@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    python_requires="~=3.7",
    keywords=['python', 'asyncio', 'async', 'task'],
    classifiers=[
    ]
)