FROM python:3.12.0-alpine3.18

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "entrypoint.sh"]
