FROM python:alpine

ADD . /app
WORKDIR /app
ENV PORT 8000
EXPOSE 8000

CMD ["python", "server.py"]

