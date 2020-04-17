clean:
	rm -rf dist
	rm -rf *.egg.info
	find . -type f -name *.pyc -exec rm -f {} \;

build:
	docker-compose stop
	docker-compose rm
	docker-compose build

run:
	docker-compose up

install: clean
	poetry install

lint: clean
	flake8 brprev_bot

test: lint
	pytest -v --cov-fail-under=90 --cov=brprev_bot brprev_bot/tests 

test-report:
	pytest -v --cov-fail-under=90 --cov=brprev_bot --cov-report=html brprev_bot/tests

db-init:
	poetry run initialize_db

db-migrate:
	flask db migrate -m "$(message)"

db-upgrade:
	flask db upgrade