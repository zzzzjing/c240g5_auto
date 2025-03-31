# -*- coding: utf-8 -*-

# CloudLab 实验配置：c240g5 + Tesla P100 + Ubuntu 22.04 + CUDA 11.8

import geni.portal as portal
import geni.rspec.pg as pg

# 创建 request 对象
request = portal.Context().makeRequestRSpec()

# 添加一台 GPU 节点（c240g5 机器带 Tesla P100）
node = request.RawPC("gpu-node")
node.hardware_type = "c240g5"
node.disk_image = "urn:public:image:CloudLab-PG0:gpu-ubuntu22.04-cuda11.8"

# 启用外网控制 IP（可选）
node.routable_control_ip = True

# 提交请求
portal.context.printRequestRSpec(request)
