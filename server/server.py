from flask import Flask
from flask import render_template
from flask import send_file
from flask import request
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import ctypes
import random
import os
import numpy as np
import base64
from io import BytesIO
import time

def generate_random_data(data_type, data_size):
    print(data_type, data_size)
    return [0,1,2,3]

app = Flask(__name__, static_folder='../client/build', static_url_path='/')

def get_new_graphs(old_graphs, new_sort_name, data_size):
    '''
    Функция принимает на вход
    old_graphs - массив объектов которые нужно поместить на график (не нужно пересчитывать только отобразить)
    new_sort_name  - имя сортировки время работы которой нужно получить и поместить на общий график
    size - количество элементов в массиве который будем сортровать


    На выходе должна быть картинка, график содержащий старые сортировки и один новый 
    + 
    обновленная информация и графике (новый объект в массиве объектов old_graphs)
    '''
    fig = Figure()
    ax = fig.subplots()
    print("old_graphs" , old_graphs)
    for i in old_graphs["value"]:
       ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), list(i.values())[0])


    dir_path = os.path.dirname(os.path.realpath(__file__))
    lib = ctypes.cdll.LoadLibrary(dir_path + "/libc/build/libsorts.dylib")
    lib.bubble_sort_with_timer.restype = ctypes.c_double
    lib.insertion_sort_with_timer.restype = ctypes.c_double
    lib.quick_sort_with_timer.restype = ctypes.c_double
    info_about_new_sort = []

    if (new_sort_name == "quick_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.quick_sort_with_timer(arr_1, len(arr_1)))
        old_graphs = [{"quick_sort" : info_about_new_sort}]

    if (new_sort_name == "insertion_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.insertion_sort_with_timer(arr_1, len(arr_1)))

        #old_graphs["value"] = old_graphs["value"].append({"insertion_sort" : info_about_new_sort})
        print("-------------------------", old_graphs)
        old_graphs = [*(old_graphs["value"]), {"insertion_sort" : info_about_new_sort}]

    if (new_sort_name == "bubble_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.bubble_sort_with_timer(arr_1, len(arr_1)))

    ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), info_about_new_sort)
    buf = BytesIO()
    fig.savefig(buf, format="png")

    return {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}

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

@app.route('/server/get_new_graphs/<new_sort_name>/<data_size>', methods=["POST"])
def generate_new_graphs(new_sort_name, data_size):
    old_graphs = request.get_json()
    return get_new_graphs(old_graphs, new_sort_name, int(data_size))

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
    time.sleep(2)
    return {"data" : "10"}


@app.route('/get_image', methods = ["POST"])
def get_image():
    time.sleep(2)
    filename = "img/bogom_dan.jpg"
    img_in_bytes = str(base64.b64encode(open(filename, "rb").read()))[2:-6]
    return {"img_in_bytes" : img_in_bytes}


if __name__ == "__main__":
    app.run(debug=True)
