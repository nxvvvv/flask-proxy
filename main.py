from flask import Flask
from requests import get
app = Flask(__name__)

SITE_NAME = 'https://youtube.com/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  resp = get(f'{SITE_NAME}{path}')
  if resp.headers.get('content-type'):
    return resp.content
  return resp.text
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
