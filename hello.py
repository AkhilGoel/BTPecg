import os, io
import socket
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
    TCP_PORT = 4000
    BUFFER_SIZE = 1024
    MESSAGE="Hello World"

    s = socket.socket(socket.AF_INET,socket.SCOK_STREAM)
    s.connect((TCP_IP,TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    return "received data:",data
              

@app.route("/analyse", methods=['POST'])
def analyse():
    data = request.files.get('file', '')
    if data:
        filename = secure_filename(data.filename)
        in_memory_file = io.BytesIO()
        data.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        text = ''.join(chr(i) for i in data)
        value = []
        t = text.split("\n")
        t = t[0:len(t)-1]
        for line in t:
            if line:
                value.append(float(line))
        return "Analysis"
    else:
        abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# and allowed_file(file.filename)
