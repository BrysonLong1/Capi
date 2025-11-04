FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -U pip && pip install -r requirements.txt

COPY . /app

# Create socket dir
RUN mkdir -p /run && chmod 777 /run

CMD ["gunicorn", "-c", "gunicorn.conf.py", "app.main:app"]
