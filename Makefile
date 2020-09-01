start:
	docker-compose up -d --build

stop:
	docker-compose stop

build:
	docker-compose build

restart:
	docker-compose build
	docker-compose up -d

clean:
	docker-compose rm --force --stop
	docker-compose down --volumes

db:
	docker exec -it membermanager_db-api_1 python manage.py $(MAKECMDGOALS)
