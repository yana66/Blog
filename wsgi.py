#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

application = app.app


