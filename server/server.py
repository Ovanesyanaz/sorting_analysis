from flask import Flask
from flask import render_template
from flask import send_file
from flask import request
from matplotlib.figure import Figure
import numpy as np
import base64
from io import BytesIO
import time

def generate_random_data(data_type, data_size):
    print(data_type, data_size)
    return [0,1,2,3]

app = Flask(__name__, static_folder='../client/build', static_url_path='/')

def get_new_graphs(old_graphs, new_sort_name):
    '''
    Функция принимает на вход
    old_graphs - массив объектов которые нужно поместить на график (не нужно пересчитывать только отобразить)
    new_sort_name  - имя сортировки время работы которой нужно получить и поместить на общий график
    size - количество элементов в массиве который будем сортровать


    На выходе должна быть картинка, график содержащий старые сортировки и один новый 
    + 
    обновленная информация и графике (новый объект в массиве объектов old_graphs)
    '''
    pass

def generate_first_graphs(data):
    time.sleep(1)
    fig = Figure()
    ax = fig.subplots()
    for i in range(len(data)):
        ax.plot(data[i])
    buf = BytesIO()
    fig.savefig(buf, format="png")
    return base64.b64encode(buf.getbuffer()).decode("ascii")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/server/get_new_graphs/<new_sort_name>', methods=["POST"])
def generate_new_graphs(new_sort_name):
    old_graphs = request.get_json()
    get_new_graphs(old_graphs, new_sort_name)

@app.route('/server/get_info_about_sorts/<data_type>/<data_size>', methods=["POST"])
def get_info_about_sorts(data_type,data_size):
    data_size = int(data_size)
    print(data_type, data_size)
    img_in_bytes = generate_first_graphs([np.random.randint(-10000, 10000, data_size), np.random.randint(-10000, 10000, data_size)])
    data = generate_random_data(data_type, data_size)
    return {"info_about_sorts" : data, "img_in_bytes" : img_in_bytes}


@app.route('/server/chart_update', methods=["POST"])
def chart_update():
    time.sleep(2)
    data = request.get_json()
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
