FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD gunicorn analytics_project.wsgi:application --bind 0.0.0.0:10000
