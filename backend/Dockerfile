FROM python:3.11

WORKDIR /app
COPY . /app

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

RUN pip install fastapi uvicorn sqlalchemy pydantic requests sqlalchemy psycopg2-binary

CMD ["/wait-for-it.sh", "postgres:5432", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

