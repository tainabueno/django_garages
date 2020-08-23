DJANGO_MANAGEMENT = python manage.py
HTTP_PORT ?= 8000

.PHONY: build run test

run:
	@echo 'Running Garage Server'
	$(DJANGO_MANAGEMENT) runserver 0.0.0.0:$(HTTP_PORT)

build:
	@echo 'Building Garage Server'
	$(DJANGO_MANAGEMENT) makemigrations
	$(DJANGO_MANAGEMENT) migrate
	$(DJANGO_MANAGEMENT) make_admin
	$(DJANGO_MANAGEMENT) create_vehicles
