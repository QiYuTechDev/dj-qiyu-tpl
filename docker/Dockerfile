FROM python:3.9

RUN  mkdir /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip config set global.index https://mirrors.aliyun.com/pypi/simple        \
    && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip install -r requirements.txt

COPY . /app/
ENTRYPOINT /app/supervisor/entrypoint.sh
