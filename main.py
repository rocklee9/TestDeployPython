

from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin





CLIENT_ID = "f43a700c4095ed6"
PATH = "C:\\Users\\ADMIN\\Desktop\\anh.png"

im = pyimgur.Imgur(CLIENT_ID)

scale = 0.00392
conf_threshold = 0.5
nms_threshold = 0.4

# Doan ma khoi tao server
app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return '<h1>hello !<h1>'



# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True)
    