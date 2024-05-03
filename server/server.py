import matplotlib.pyplot as plt
import numpy as np
import platform
import ctypes
import random
import base64
import os
import time

from matplotlib.figure import Figure
from flask import request
from flask import Flask
from io import BytesIO
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='../client/build', static_url_path='/')
socketio = SocketIO(cors_allowed_origins=[
    "http://127.0.0.1:5000"
])

origins = "*"

socketio = SocketIO(cors_allowed_origins=origins)

socketio.init_app(app)
@app.route('/')
def index():
    return app.send_static_file('index.html')

def get_old_graphs(mask, arr , data_size):
    fig = Figure()
    ax = fig.subplots()
    for i in mask:
        if i not in arr:
            continue
        ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), arr[i], label=f"{i}")
    ax.set_title("Sorting analysis", fontsize="24", fontweight="17")
    ax.set_ylabel("Time", fontsize="14")
    ax.set_xlabel("Size", fontsize="14")
    ax.legend()
    buf = BytesIO()
    fig.savefig(buf, format="png")

    return {"img":base64.b64encode(buf.getbuffer()).decode("ascii")}

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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lib_path = ""
    match platform.system():
        case "Linux": lib_path = "/build/libsorts.so"
        case "Darwin": lib_path = "/build/libsorts.dylib"
        case "Windows": lib_path = "\\build\\libsorts.dll"
        case _: raise RuntimeError("undefined platform")
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lib = ctypes.cdll.LoadLibrary(dir_path + "/libc/" + lib_path)
    lib.bubble_sort_with_timer.restype = ctypes.c_double
    lib.insertion_sort_with_timer.restype = ctypes.c_double
    lib.quick_sort_with_timer.restype = ctypes.c_double
    lib.merge_sort_with_timer.restype = ctypes.c_double

    fig = Figure()
    ax = fig.subplots()
    for i in old_graphs:
       ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i], label=f"{i}")

    info_about_new_sort = []

    if (new_sort_name == "quick_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.quick_sort_with_timer(arr_1, len(arr_1)))
        old_graphs["quick_sort"] = info_about_new_sort

    if (new_sort_name == "merge_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.merge_sort_with_timer(arr_1, len(arr_1)))

        old_graphs["merge_sort"] = info_about_new_sort

    if (new_sort_name == "insertion_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.insertion_sort_with_timer(arr_1, len(arr_1)))

        old_graphs["insertion_sort"] = info_about_new_sort

    if (new_sort_name == "bubble_sort"):
        for i in range(10, data_size, int((data_size - 10) / 200)):
            py_values = [random.randint(1, 1000) for _ in range(i)]
            arr_1 = (ctypes.c_int * len(py_values))(*py_values)
            info_about_new_sort.append(lib.bubble_sort_with_timer(arr_1, len(arr_1)))

        old_graphs["bubble_sort"] = info_about_new_sort
    
    ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), info_about_new_sort, label=f"{new_sort_name}")
    ax.set_title("Sorting analysis", fontsize="24", fontweight="17")
    ax.set_ylabel("Time", fontsize="14")
    ax.set_xlabel("Size", fontsize="14")
    ax.legend()
    plt.style.use('seaborn-v0_8-colorblind')
    buf = BytesIO()
    fig.savefig(buf, format="png")

    return {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}

@app.route('/server/get_new_graphs/<new_sort_name>/<data_size>', methods=["POST"])
def generate_new_graphs(new_sort_name, data_size):
    old_graphs = request.get_json()
    return get_new_graphs(old_graphs, new_sort_name, int(data_size))

@app.route('/server/get_old_graphs/<data_size>', methods=["POST"])
def generate_old_graphs(data_size):
    old_graphs = request.get_json()
    mask = old_graphs["a"]
    arr2 = old_graphs["value"]
    return get_old_graphs(mask, arr2, int(data_size))

@socketio.on("server/ws/get_new_graphs")
def generate_ws_new_graphs(data):
    print(data)

@socketio.on("chat")
def handle_chat(data):
    print(data)
    data_size = int(data["dataSize"])
    old_graphs = dict()
    for new_sort_name in data["sorts"]:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lib_path = ""
        match platform.system():
            case "Linux": lib_path = "/build/libsorts.so"
            case "Darwin": lib_path = "/build/libsorts.dylib"
            case "Windows": lib_path = "\\build\\libsorts.dll"
            case _: raise RuntimeError("undefined platform")
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lib = ctypes.cdll.LoadLibrary(dir_path + "/libc/" + lib_path)
        lib.bubble_sort_with_timer.restype = ctypes.c_double
        lib.insertion_sort_with_timer.restype = ctypes.c_double
        lib.quick_sort_with_timer.restype = ctypes.c_double
        lib.merge_sort_with_timer.restype = ctypes.c_double
        fig = Figure()
        ax = fig.subplots()
        ax.set_title("Sorting analysis", fontsize="24", fontweight="17")
        ax.set_ylabel("Time", fontsize="14")
        ax.set_xlabel("Size", fontsize="14")
        plt.style.use('seaborn-v0_8-colorblind')
        info_about_new_sort = []
        amount = 0
        if (new_sort_name == "quick_sort"):
            for i in old_graphs:
                ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i], label=f"{i}")
            
            for i in range(10, data_size, int((data_size - 10) / 200)):
                amount += 1
                py_values = [random.randint(1, 1000) for _ in range(i)]
                summ = 0
                for k in range(3):
                    arr_1 = (ctypes.c_int * len(py_values))(*py_values)
                    summ += (lib.quick_sort_with_timer(arr_1, len(arr_1)))
                info_about_new_sort.append(summ / 3)
                
                if amount % 20 == 0:
                    if amount == 20:
                        ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
                        ax.legend()
                    ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort)
                    buf = BytesIO()
                    fig.savefig(buf, format="png")
                    emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)        
            old_graphs["quick_sort"] = info_about_new_sort
            ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
            buf = BytesIO()
            fig.savefig(buf, format="png")
            emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)
        if (new_sort_name == "merge_sort"):
            for i in old_graphs:
                ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i], label=f"{i}")
            for i in range(10, data_size, int((data_size - 10) / 200)):
                amount += 1
                py_values = [random.randint(1, 1000) for _ in range(i)]
                summ = 0
                for k in range(3):
                    arr_1 = (ctypes.c_int * len(py_values))(*py_values)
                    summ += (lib.merge_sort_with_timer(arr_1, len(arr_1)))
                info_about_new_sort.append(summ / 3)
                if amount % 20 == 0:
                    if amount == 20:
                        ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
                        ax.legend()
                    ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort)
                    buf = BytesIO()
                    fig.savefig(buf, format="png")
                    emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)        
            old_graphs["merge_sort"] = info_about_new_sort
            ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
            buf = BytesIO()
            fig.savefig(buf, format="png")
            emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)
        if (new_sort_name == "insertion_sort"):
            for i in old_graphs:
                ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i], label=f"{i}")
            for i in range(10, data_size, int((data_size - 10) / 200)):
                amount += 1
                py_values = [random.randint(1, 1000) for _ in range(i)]
                summ = 0
                for k in range(3):
                    arr_1 = (ctypes.c_int * len(py_values))(*py_values)
                    summ += lib.insertion_sort_with_timer(arr_1, len(arr_1))
                info_about_new_sort.append(summ / 3)
                if amount % 5 == 0:
                    if amount == 5:
                        ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
                        ax.legend()
                    ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort)
                    buf = BytesIO()
                    fig.savefig(buf, format="png")
                    emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)        
            old_graphs["insertion_sort"] = info_about_new_sort
            ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
            buf = BytesIO()
            fig.savefig(buf, format="png")
            emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)

        if (new_sort_name == "bubble_sort"):
            amount = 0
            for i in old_graphs:
                ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i], label=f"{i}")
            for i in range(10, data_size, int((data_size - 10) / 200)):
                amount += 1
                py_values = [random.randint(1, 1000) for _ in range(i)]
                summ = 0
                for k in range(3):
                    arr_1 = (ctypes.c_int * len(py_values))(*py_values)
                    summ += lib.bubble_sort_with_timer(arr_1, len(arr_1))
                info_about_new_sort.append(summ / 3)
                if amount % 5 == 0:
                    if amount == 5:
                        ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
                        ax.legend()
                    ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort)
                    buf = BytesIO()
                    fig.savefig(buf, format="png")
                    emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)        
            old_graphs["bubble_sort"] = info_about_new_sort
            ax.semilogy(list(range(10, data_size, int((data_size - 10) / 200)))[:len(info_about_new_sort)], info_about_new_sort, label=f"{new_sort_name}")
            ax.legend()
            buf = BytesIO()
            fig.savefig(buf, format="png")
            emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}, broadcast=True)
    fig.clf()
    fig = Figure()
    ax = fig.subplots()
    ax.set_title("Sorting analysis", fontsize="24", fontweight="17")
    ax.set_ylabel("Time", fontsize="14")
    ax.set_xlabel("Size", fontsize="14")
    plt.style.use('seaborn-v0_8-colorblind')
    for i in old_graphs:
            ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i], label=f"{i}")
    ax.legend()
    buf = BytesIO()
    fig.savefig(buf, format="png")
    emit("chat", {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs, "isEnd": 1}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
    app.run(debug=True)
