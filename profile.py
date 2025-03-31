# profile.py - CloudLab 实验配置脚本：c240g5 + Tesla P100 + CUDA 11.8

import geni.portal as portal
import geni.rspec.pg as pg

# 创建 portal request 对象
request = portal.Context().makeRequestRSpec()

# 申请 1 台 c240g5 机器（含 Tesla P100 GPU）
node = request.RawPC("gpu-node")
node.hardware_type = "c240g5"

# 选择内置 GPU 驱动和 CUDA 的镜像（Ubuntu 22.04 + CUDA 11.8）
node.disk_image = "urn:public:image:CloudLab-PG0:gpu-ubuntu22.04-cuda11.8"

# 启用 X11 forwarding（可选）
node.routable_control_ip = True

# 提交请求
portal.context.printRequestRSpec(request)
