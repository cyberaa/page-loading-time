FROM python:alpine
MAINTAINER Corentin Gitton <corentin.gitton@gmail.com>

COPY src /app
RUN apk add --no-cache ca-certificates && \
	pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080

CMD ["python", "/app/server.py"]
