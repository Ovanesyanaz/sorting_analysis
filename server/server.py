from flask import Flask
from flask import send_file
import base64
app = Flask(__name__)


@app.route("/members")
def members():
    return {"members": ["members1", "members2", "members3"]}



@app.route('/get_image')
def get_image():
    filename = "img/bogom_dan.jpg"
    img_in_bytes = str(base64.b64encode(open(filename, "rb").read()))[2:-6]
    return {"img_in_bytes" : img_in_bytes}


if __name__ == "__main__":
    app.run(debug=True)