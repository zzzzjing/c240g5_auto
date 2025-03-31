import geni.portal as portal
import geni.rspec.pg as pg

request = portal.Context().makeRequestRSpec()

node = request.RawPC("gpu_node")
node.hardware_type = "c240g5"
node.disk_image = "urn:public:image:CloudLab-PG0:gpu-ubuntu22.04-cuda11.8"

node.routable_control_ip = True

portal.context.printRequestRSpec(request)
