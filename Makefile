DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint: ## Run linters
	./scripts/lint.sh

.PHONY: clean
clean: clean_pyc ## Clean all build artifacts

.PHONY: clean_pyc
clean_pyc: ## Clean all \*.pyc files
	find . -type f -name "*.pyc" -delete || true

.PHONY: migrate
migrate: ## Run database migrations
	python manage.py migrate --noinput

.PHONY: migrations
migrations: ## Generate new migrations
	python manage.py makemigrations

.PHONY: requirements
requirements: ## Install the requirements
	pip install -r requirements/development.txt

.PHONY: run
run: ## Start the development server
	python manage.py runserver

.PHONY: run_plus
run_plus: ## Start the development server with django extensions runserver\_plus
	python manage.py runserver_plus

.PHONY: shell
shell: ## Start the shell using django extensions shell\_plus
	python manage.py shell_plus

.PHONY: show_urls
show_urls: ## Show the available URLs
	python manage.py show_urls

.PHONY: test
test: ## Run the tests
	pytest $(TESTONLY) --disable-pytest-warnings -s -vv $(CREATE_DB)

.PHONY: go
go: ## Start the virtual environment and source the files
	source .venv/bin/activate

ifndef VERBOSE
.SILENT:
endif