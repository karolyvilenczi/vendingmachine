APP_NAME= wending_machine

IMG_NAME = kvilenczi/img_python_app_$(APP_NAME):latest
CONT_NAME = cont_python_app_$(APP_NAME)


build:
	docker build -t $(IMG_NAME) .

# Checks
run_black:
	docker exec -it $(CONT_NAME) black /app

run_mypy:
	docker exec -it $(CONT_NAME) mypy --show-column-numbers --explicit-package-bases /app

# to run this run (e.g.) run_rm_it_bash before to have the container up and running
run_checks: run_black run_mypy

# Tests
run_pytest:
	docker exec -it $(CONT_NAME) pytest -v -s


# Runners
run_rm_d_app:
	docker run -d --rm --network host --name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/app \
	--mount type=bind,source=$$(pwd)/app/docs,target=/app/docs \
	$(IMG_NAME)

run_rm_it_app:
	docker run -it --rm --network host --name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/app \
	--mount type=bind,source=$$(pwd)/app/docs,target=/app/docs \
	$(IMG_NAME) /bin/bash -c "python app.py"

run_rm_it_bash:
	docker run -it --rm --network host --name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/app \
	--mount type=bind,source=$$(pwd)/app/docs,target=/app/docs \
	$(IMG_NAME) /bin/bash

run_rm_it_ep:
	docker run -it --rm --network host --name $(CONT_NAME) \
	--mount type=bind,source=$$(pwd)/app,target=/app \
	--mount type=bind,source=$$(pwd)/app/docs,target=/app/docs \
	$(IMG_NAME) /bin/bash -c "uvicorn app:ep_app --host 127.0.0.1 --port 8000 --log-level debug --use-colors --reload"


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
