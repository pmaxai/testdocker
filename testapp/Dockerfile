FROM python:3.11-slim
WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
