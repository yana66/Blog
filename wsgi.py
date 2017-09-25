#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))


# 必须有一个叫做application 的变量
# gunicorn 需要这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
application = app.app




# 这是把代码部署到 apache gunicorn nginx 后面的套路
# wsgi 文件是给gunicorn用的
# 用 gunicorn 运行程序
# gunicorn wsgi --bind 0.0.0.0:2000

"""
ln -s /var/www/blog/conf/supervisor.conf /etc/supervisor/conf.d/blog.conf
ln -s /var/www/blog/conf/nginx.conf /etc/nginx/sites-enabled/blog

→ ~ nano /etc/supervisor/conf.d/<xx>.conf

#写入下面这个文件
[program:blog]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/blog.pid
# 到哪个目录底下执行命令(程序在哪个目录)
directory=/var/www/blog
autostart=true
autorestart=true
"""

# 重启supervisor
# service supervisor restart

# supervisorctl restart blog