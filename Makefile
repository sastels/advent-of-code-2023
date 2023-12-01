.DEFAULT_GOAL := help
SHELL := /bin/bash #bash | sh
DATE = $(shell date +%Y-%m-%dT%H:%M:%S)

PIP_ACCEL_CACHE ?= ${CURDIR}/cache/pip-accel

GIT_BRANCH ?= $(shell git symbolic-ref --short HEAD 2> /dev/null || echo "detached")
GIT_COMMIT ?= $(shell git rev-parse HEAD 2> /dev/null || echo "")


.PHONY: help
help:
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test:
	./scripts/run_tests.sh


.PHONY: freeze-requirements
freeze-requirements:
	poetry lock --no-update

.PHONY: test-requirements
test-requirements:
	poetry lock --check

.PHONY: format
format:
	isort ./app ./tests
	black ./app ./tests
	flake8 ./app ./tests
	isort --check-only ./app ./tests
	mypy ./
