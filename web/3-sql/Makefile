all: build

NAME = 3-sql

build:
	docker build -t $(NAME)-build .

run: start wait exec
start:
	docker run --rm -itd --name $(NAME)-run -p 8003:5000 -e MYSQL_ROOT_PASSWORD=root_pass_is_toor -e MYSQL_DATABASE=part1_db $(NAME)-build

wait:
	sleep 30

exec:
	docker exec -itd $(NAME)-run /entrypoint.sh

export:
	docker save $(NAME)-build > $(NAME)-build.tar

import:
	docker load < $(NAME)-build.tar

test:
	docker exec -it $(NAME)-run bash

stop:
	docker kill $(NAME)-run
