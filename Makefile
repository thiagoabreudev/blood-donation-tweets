set_env_development:
	@rm docker-compose.override.yml || true
	ln -s docker-compose.development.yml docker-compose.override.yml

set_env_production:
	@rm docker-compose.override.yml || true
	ln -s docker-compose.production.yml docker-compose.override.yml

makemigrations:
	docker-compose run backend bash -c "python manage.py makemigrations"	

migrate:
	docker-compose run backend bash -c "python manage.py migrate"

createsuperuser:
	docker-compose run backend bash -c "python manage.py createsuperuser"	

startapp:
	docker-compose run backend bash -c "python manage.py startapp $(app)"	

build-install-modules:
	docker-compose run frontend sh -c "cd frontend && npm install"

build-frontend:
	docker-compose run frontend sh -c "cd frontend && npm run build"