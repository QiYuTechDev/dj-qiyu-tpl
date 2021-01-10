#!/usr/bin/env bash

# 初始化超级管理员
(cd $(SUPERVISOR_DJANGO_DIRECTORY) && python manage.py migrate) || {
        echo '数据库迁移失败' ;
        exit 1;
}

# 启动 supervisor 监控
/usr/local/bin/supervisord -c /app/supervisor/daemon.ini
