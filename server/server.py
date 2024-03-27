from flask import Flask
from flask import send_file
from flask import request
import base64
import time
app = Flask(__name__)

def generate_random_data(data_type, data_size):
    print(data_type, data_size)
    return [0,1,2,3]


@app.route('/server/get_info_about_sorts/<data_type>/<data_size>', methods=["POST"])
def get_info_about_sorts(data_type,data_size):
    data = generate_random_data(data_type, data_size)
    filename = "img/bogom_dan.jpg"
    img_in_bytes = str(base64.b64encode(open(filename, "rb").read()))[2:-6]
    return {"info_about_sorts" : data, "img_in_bytes" : img_in_bytes}


@app.route('/test', methods=["POST"])
def test():
    time.sleep(1)
    data = request.get_json()
    print(data)
    return data


@app.route('/get_image', methods = ["POST"])
def get_image():
    time.sleep(2)
    filename = "img/bogom_dan.jpg"
    img_in_bytes = str(base64.b64encode(open(filename, "rb").read()))[2:-6]
    return {"img_in_bytes" : img_in_bytes}


if __name__ == "__main__":
    app.run(debug=True)
