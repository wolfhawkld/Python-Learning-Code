''' Demo 1
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}
host = ('localhost', 8101)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
'''

''' Demo 2
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get('/test/a={a}/b={b}')
def calculate(a: int=None, b: int=None):
    c = a + b
    res = {"res":c}
    return res
 
 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8101,
                workers=1)

'''

from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def insert():
    info = request.json
    print("You Json is:{}",info)
    msg = "Receive Json：{}".format(info)
    os.system("123.bat")
    return str({'success': True, 'msg': msg})

if __name__ == '__main__':
    app.run()