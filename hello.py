import os, io
import socket,time
from flask import Flask, request, jsonify, send_file, abort, render_template
from werkzeug import secure_filename

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def hello():
    
     return render_template('websockettest.php')
    
@app.route("/test")
def test():
    
    TCP_IP = '172.25.13.141'
    TCP_PORT = 30000
    BUFFER_SIZE = 1024
    MESSAGE="Hello World"

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((TCP_IP,TCP_PORT))
    time.sleep(1)
    s.send(MESSAGE)
    s.close()

    return "done"
              
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# and allowed_file(file.filename)
