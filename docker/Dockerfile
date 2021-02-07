FROM python:3.9

RUN  mkdir /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip config set global.index https://mirrors.aliyun.com/pypi/simple        \
    && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip install -r requirements.txt

# 设置为 线上 状态
ENV DJANGO_PROD=1

ENV DJANGO_PORT=8080
ENV DJANGO_THREADS=200
ENV DJANGO_SETTINGS=hello.wsgi
ENV DJANGO_DIRECTORY=/app/hello

COPY . /app/
ENTRYPOINT /app/supervisor/entrypoint.sh
