FROM jazzdd/alpine-flask:latest
ADD ./app /app
ENV FLASK_APP=/app/app.py
EXPOSE 5000
WORKDIR /app
RUN apk add --no-cache py-mysqldb
RUN pip install flask-cors
ENTRYPOINT flask run --host=0.0.0.0
