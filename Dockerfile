FROM python:3.8.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY requirements/production.txt .
RUN pip3 install --upgrade pip && pip3 install -r production.txt
ENV PYTHONPATH /app
WORKDIR /app
COPY . /app

EXPOSE 8000
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
