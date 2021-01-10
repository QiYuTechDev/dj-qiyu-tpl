FROM python:3.9

RUN  mkdir /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip config set global.index https://mirrors.aliyun.com/pypi/simple \
    && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

RUN pip install -r requirements.txt

# 设置为 开发 状态
ENV DJANGO_DEV=1

ENV SUPERVISOR_USERNAME=supervisor
ENV SUPERVISOR_PASSWORD=supervisor
ENV SUPERVISOR_PROMPT=supervisor

ENV SUPERVISOR_DJANGO_PORT=8080
ENV SUPERVISOR_DJANGO_THREADS=200
ENV SUPERVISOR_DJANGO_SETTINGS=hello.wsgi
ENV SUPERVISOR_DJANGO_DIRECTORY=/app/hello

COPY . /app/
ENTRYPOINT /app/supervisor/entrypoint.sh
