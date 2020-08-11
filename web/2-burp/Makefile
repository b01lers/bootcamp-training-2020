all: build

NAME = 2-burp


build:
	docker build -t $(NAME)-build .

run: start
start:
	docker run --rm -itd --name $(NAME)-run -p 8002:5000 $(NAME)-build

exec:
	docker exec -it $(NAME)-run bash

export:
	docker save $(NAME)-build > $(NAME)-build.tar

import:
	docker load < $(NAME)-build.tar

stop:
	docker kill $(NAME)-run
