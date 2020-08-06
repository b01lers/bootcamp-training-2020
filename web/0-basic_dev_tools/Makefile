all: build

NAME = 0-basic_dev_tools


build:
	docker build -t $(NAME)-build .

run: start
start:
	docker run --rm -itd --name $(NAME)-run -p 8000:5000 $(NAME)-build

exec:
	docker exec -it $(NAME)-run bash

export:
	docker save $(NAME)-build > $(NAME)-build.tar

import:
	docker load < $(NAME)-build.tar

stop:
	docker kill $(NAME)-run
