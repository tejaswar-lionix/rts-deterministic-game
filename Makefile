build:
	docker build -t rts-game .

test:
	pytest -q

run:
	python manage.py runserver 0.0.0.0:8000
