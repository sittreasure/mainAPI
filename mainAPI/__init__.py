import os
import requests

url = os.environ.get('GATEWAY_URL')
name = 'mainapi'

requests.put(
  url = '{url}/services/{name}'.format(
    url = url,
    name = name
  ),
  data = {
    'name': name,
    'host': os.environ.get('APP_URL'),
    'port': os.environ.get('APP_PORT')
  }
)

requests.post(
  url = '{url}/services/{name}/routes'.format(
    url = url,
    name = name
  ),
  data = {
    'name': 'all-main-api-routes',
    'paths': [
      '/mainapi'
    ]
  }
)
