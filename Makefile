APP_NAME= wending_machine
APP_USER_NAME=app_user

IMG_NAME = kvilenczi/img_python_app_$(APP_NAME):latest
CONT_NAME = cont_python_app_$(APP_NAME)

# Build 
build:
	docker build \
	--build-arg GROUP_ID=$$(id -g) \
	--build-arg USER_ID=$$(id -u) \
	--build-arg USER_NAME=$(APP_USER_NAME) -t $(IMG_NAME) . 

# Runners
run_rm_it_ep:
	docker run -it --rm --network host \
	--name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/home/$(APP_USER_NAME)/app \
	$(IMG_NAME) /bin/bash -c "uvicorn app:ep_app --host 127.0.0.1 --port 8000 --log-level debug --use-colors --reload"


run_rm_d_app:
	docker run -d --rm --network host --name $(CONT_NAME) --mount type=bind,source=$$(pwd)/app,target=/app $(IMG_NAME)

run_rm_it_app:
	docker run -it --rm --network host \
	--name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/home/$(APP_USER_NAME)/app \
	$(IMG_NAME) /bin/bash -c "python app.py"

run_rm_it_bash:
	docker run -it --rm --network host \
	--name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/home/$(APP_USER_NAME)/app \
	$(IMG_NAME) /bin/bash

# Enter
enter_bash:
	docker exec -it $(CONT_NAME) bash

# Checks
run_mypy:
	docker exec -it $(CONT_NAME) mypy --show-column-numbers --explicit-package-bases .

run_black:
	docker exec -it $(CONT_NAME) python -m black .

run_checks: run_black run_mypy

# Tests
run_pytest:
	docker exec -it $(CONT_NAME) python -m pytest -v -s


run_coverage:
	docker exec -it $(CONT_NAME) python -m pytest -v -s --cov=app


run_tox:
	docker exec -it $(CONT_NAME) python -m tox

# Utility commands
stop:
	docker stop $(CONT_NAME)

remove:
	docker rm $(CONT_NAME)

logs:
	docker logs -f $(CONT_NAME)

stop_remove: stop remove

run_log: run_rm_d_app logs

re_build_run: build run_rm_it_app

ps:
	docker ps --all

push:
	docker push $(IMG_NAME)

prune:
	docker system prune --all -f

prune_img:
	docker image prune -f

prune_vol:
	docker volume prune -f

prune_net:
	docker network prune -f

purge: prune prune_img


# Some cleaners
clean_build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -name '*.egg' -exec rm -f {} +

clean_pyc: ## remove Python file artifacts
	find . -name '*.pyc' -name '*.pyo' -name '*~' -name '__pycache__' -exec rm -f {} +
	find . -type d -name '.mypy_cache' -exec rm -rf {} +


clean_test: ## remove test and coverage artifacts
	find . -name '.pytest_cache' -name '.tox' -name '.coverage' -exec rm -f {} +
	
