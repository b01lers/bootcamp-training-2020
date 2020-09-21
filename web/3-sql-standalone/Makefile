all: build ufw run

NAME = 3-sql
PORT = 8003

build:
	docker build -t $(NAME)-build .

ufw:
	ufw allow $(PORT)

run: start exec
start:
	docker run --rm -itd --name $(NAME)-run -p $(PORT):5000 -e MYSQL_ROOT_PASSWORD=root_pass_is_toor -e MYSQL_DATABASE=part1_db $(NAME)-build

exec:
	docker exec -itd $(NAME)-run /entrypoint.sh

stop:
	docker kill $(NAME)-run
