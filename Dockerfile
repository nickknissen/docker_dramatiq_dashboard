FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ["requirements.txt", "run.py", "/app/"]

RUN python3 -m pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "run:app", "--bind 0.0.0.0:8000"]
