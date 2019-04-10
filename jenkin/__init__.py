import os
import py_eureka_client.eureka_client as eureka_client

url = os.environ.get('DISCOVERY_URL')
port = int(os.environ.get('APP_PORT'))

eureka_client.init(
  eureka_server="{url}/eureka/".format(url = url),
  app_name="mainapi",
  instance_port=port
)