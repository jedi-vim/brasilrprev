clean:
	rm -rf dist
	rm -rf *.egg-info
	find . -type f -name *.pyc -exec rm -f {} \;

build: clean
	docker-compose stop
	docker-compose rm
	docker-compose build

run:
	export DYNACONF_MONGO_HOST=mongo
	export DYNACONF_REDIS_HOST=redis
	docker-compose up

prompt:
	docker-compose exec brprev_cli bash

install: clean
	poetry install

lint: clean
	flake8 brprev_cli

test: lint
	pytest -v --cov-fail-under=90 --cov=brprev_cli brprev_cli/tests 

test-report:
	pytest -v --cov-fail-under=90 --cov=brprev_cli --cov-report=html brprev_cli/tests