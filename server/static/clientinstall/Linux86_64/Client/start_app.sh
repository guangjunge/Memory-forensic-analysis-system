#!/bin/bash
server_ip="192.168.56.1"
server_port="5000"

current_time=$(date +"%Y-%m-%d %H:%M:%S")
# 获取系统名称和版本号
sys_info=$(uname -a | awk '{print $2 " " $3}')

# 获取本机 IP 地址
ip_address=$(ifconfig ens33 | grep "inet 地址:" | awk '{print $2}')
ip_address=${ip_address#*:}
# 创建 client.cfg 文件
echo "[info]" > client.cfg
echo "CLIENT_NAME=$sys_info $current_time" >> client.cfg
echo "CLIENT_IP=$ip_address" >> client.cfg
echo "URL=http://$server_ip:$server_port" >> client.cfg


# 打印文件内容
cat client.cfg

nohup python client.py > program1.log 2>&1 &
nohup python ClientMon/python-server.py > program2.log 2>&1 &