install:
	pip install --upgrade pip && \
	pip install -r requirement.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest test_hello.py


all: install lint test
