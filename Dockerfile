FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code