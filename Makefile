# If the first argument is "poetry"...
ifeq (poetry,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "poetry"
  POETRY_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_ARGS):;@true)
endif

# If the first argument is "poetry-install"...
ifeq (poetry-install,$(firstword $(MAKECMDGOALS)))
ifeq ($(words $(MAKECMDGOALS)),3)
  # use the rest as arguments for "poetry-install"
  $(info $(MAKECMDGOALS))
  POETRY_INSTALL_PACKAGE_NAME := $(word 2,$(MAKECMDGOALS))
  POETRY_INSTALL_PACKAGE_VERSION := $(word 3,$(MAKECMDGOALS))

  POETRY_INSTALL_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_INSTALL_ARGS):;@true)
else
  $(error poetry-install needs 2 arguments. See help)
endif
endif

# If the first argument is "poetry-install-dev"...
ifeq (poetry-install-dev,$(firstword $(MAKECMDGOALS)))
ifeq ($(words $(MAKECMDGOALS)),3)
  # use the rest as arguments for "poetry-install"
  $(info $(MAKECMDGOALS))
  POETRY_INSTALL_PACKAGE_NAME := $(word 2,$(MAKECMDGOALS))
  POETRY_INSTALL_PACKAGE_VERSION := $(word 3,$(MAKECMDGOALS))

  POETRY_INSTALL_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_INSTALL_ARGS):;@true)
else
  $(error poetry-install-dev needs 2 arguments. See help)
endif
endif

# help
###
.PHONY: help
help: ;@true
	$(info Makefile for Tourmanique project)
	$(info )
	$(info Avaliable targets: )
	$(info  * install-local-deps                        - installs all dependencies from poetry.lock to have helpers for code locally)
	$(info  * lint                                      - runs linting)
	$(info  -- next will be executed via docker --)
	$(info  * poetry                                    - executes poetry command in the **docker** container)
	$(info  * poetry-install <package> <version>        - installs package in the **docker** container)
	$(info  * run                                       - runs the api locally via **docker**)
	$(info  * test                                      - runs unit tests via **docker**)
	$(info )
	$(info Makefile: feel free to extend me!)

.PHONY: install-local-deps
install-local-deps: ## installs all dependencies from poetry.lock to have helpers for code locally
	poetry install

.PHONY: lint
lint: ## runs linting
	poetry run pylint \
	--load-plugins pylint_flask \
	--load-plugins pylint_flask_sqlalchemy \
	--generated-members=Column \
	--output-format=colorized \
	application.py tourmanique || poetry run pylint-exit $$?

.PHONY: poetry
poetry: ## executes poetry command in the docker container
	@echo poetry $(POETRY_ARGS)
	docker compose run --rm --no-deps association-model poetry $(POETRY_ARGS)

.PHONY: poetry-install
poetry-install: ## installs package in the **docker** container
	docker compose -f docker-compose.yml build --quiet association-model
	docker compose -f docker-compose.yml run --rm --no-deps association-model poetry add $(POETRY_INSTALL_PACKAGE_NAME) $(POETRY_INSTALL_PACKAGE_VERSION)

.PHONY: run
run: ## runs the api locally via **docker**
	docker compose -f docker-compose.yml up --build run-model-locally

.PHONY: test
test: ## runs unit tests via **docker**
	docker compose run --rm --no-deps associations-model poetry run pytest -v

.PHONY: create-migration
create-migration: ## create migration with <migration_name> via **docker**
	docker compose -f docker-compose.yml run --rm --no-deps associations-model poetry run flask db migrate -m "$(MIGRATION_NAME)"