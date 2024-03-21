#!/bin/bash

# 结束 program1.py 的进程
pkill -9 -f "python client.py"

# 结束 program2.py 的进程
pkill -9 -f  "python-server.py"

ps -ef | grep python