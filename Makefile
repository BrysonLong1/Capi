PY=python3

.PHONY: install dev run worker test lint fmt

install:
	$(PY) -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

dev:
	. .venv/bin/activate && FLASK_APP=app/main.py flask run --port 8080 --debug

run:
	. .venv/bin/activate && gunicorn -c gunicorn.conf.py app.main:app

worker:
	. .venv/bin/activate && rq worker trovix --url $$REDIS_URL

test:
	. .venv/bin/activate && pytest -q

fmt:
	. .venv/bin/activate && python -m black app
