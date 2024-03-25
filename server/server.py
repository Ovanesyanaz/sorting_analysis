from flask import Flask
from flask import send_file
from flask import request
import base64
import time
app = Flask(__name__)


# @app.route('/test', methods=["POST"])
# def test():
#     data = request.get_json()
#     print(data)
#     return {"answ" : str((int(data[0]) + int(data[1])))}


@app.route('/test', methods=["POST"])
def test():
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
