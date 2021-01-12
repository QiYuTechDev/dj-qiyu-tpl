#!/usr/bin/env bash

set -e

echo "Django 开始 migrate 数据库..."
cd $SUPERVISOR_DJANGO_DIRECTORY && python manage.py migrate
echo "数据库迁移成功"

echo "启动 supervisord 管理主进程"
/usr/local/bin/supervisord -c /app/supervisor/daemon.ini
