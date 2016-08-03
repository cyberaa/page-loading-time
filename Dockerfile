FROM python:alpine
MAINTAINER Corentin Gitton <corentin.gitton@gmail.com>

RUN pip install -r requirements.txt

COPY app.py /app.py

CMD ["python", "/app.py"]
