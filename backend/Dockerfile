FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src
ENV PYTHONPATH=/code/src:/code/src/app

WORKDIR /code/src

CMD uvicorn app.asgi:app --host $APP_HOST --port $APP_PORT
