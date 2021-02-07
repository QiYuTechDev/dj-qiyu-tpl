#!/usr/bin/env bash

set -e

echo "Django 开始 migrate 数据库..."
cd $DJANGO_DIRECTORY && python manage.py migrate
echo "数据库迁移成功"

echo "启动 gunicorn 管理主进程"
exec /usr/local/bin/gunicorn -b 127.0.0.1:$DJANGO_PORT --worker-class gthread --threads $DJANGO_THREADS $DJANGO_SETTINGS
