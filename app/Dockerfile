FROM python:3.8-slim
MAINTAINER ahmetssaglam
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . ./
#RUN python manage.py wait_for_db_connection
#RUN python manage.py migrate
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]