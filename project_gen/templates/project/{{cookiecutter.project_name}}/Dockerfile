FROM python:latest

COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry
RUN poetry install --no-root

CMD pytest /tests
