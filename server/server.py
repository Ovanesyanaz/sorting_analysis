import matplotlib.pyplot as plt
import numpy as np
import platform
import ctypes
import random
import base64
import os

from matplotlib.figure import Figure
from flask import request
from flask import Flask
from io import BytesIO


app = Flask(__name__, static_folder='../client/build', static_url_path='/')


def _test():
    """
    Задача - красиво оформить координаты с 4 графиками
    (настроить цвета, сделать шапку, легенду)
    """
    # Рандомно сгенерированные массивы, чтобы посмтреть на график
    abscissa = np.arange(1, 100)
    b_sort = np.array(abscissa) ** 2 + np.random.randint(0, np.max(abscissa) * 2, len(abscissa))
    m_sort = np.array(abscissa * np.log2(abscissa)) + np.random.randint(0, np.max(abscissa) * 2, len(abscissa))
    q_sort = np.array(abscissa * np.log2(abscissa)) + np.random.randint(0, np.max(abscissa) * 2, len(abscissa))
    i_sort = np.array(abscissa) ** 2 + np.random.randint(0, np.max(abscissa) * 2, len(abscissa))

    sorts = {"Bubble": b_sort, "Quick": q_sort, "Merge": m_sort, "Insertion": i_sort}


    fig, axis = plt.subplots(figsize=(14, 8))

    # Размещаем масссивы на графике
    for key in sorts:
        print(key)
        axis.plot(
            abscissa,
            sorts[key],
            label=f"{key}",
        )
    
    # Названия, подписи и тд
    axis.set_title("Time from size", fontsize="24", fontweight="17")
    axis.set_ylabel("Time", fontsize="14")
    axis.set_xlabel("Size", fontsize="14")

    axis.set_xticks(np.arange(0, 101, 5))
    axis.set_yticks(np.arange(0, np.max(b_sort) + 1, 1000))

    axis.set_xlim(np.min(abscissa), np.max(abscissa) + 1)

    plt.legend()
    plt.show()


def get_old_graphs(mask, arr , data_size):
    fig = Figure()
    ax = fig.subplots()
    for i in mask:
        ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), arr[i])
    
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
    lib = ctypes.cdll.LoadLibrary(dir_path + "/libc/build/libsorts.dylib")
    lib.bubble_sort_with_timer.restype = ctypes.c_double
    lib.insertion_sort_with_timer.restype = ctypes.c_double
    lib.quick_sort_with_timer.restype = ctypes.c_double
    lib.merge_sort_with_timer.restype = ctypes.c_double

    fig = Figure()
    ax = fig.subplots()
    for i in old_graphs:
       ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), old_graphs[i])

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
    
    ax.semilogy(range(10, data_size, int((data_size - 10) / 200)), info_about_new_sort)
    buf = BytesIO()
    fig.savefig(buf, format="png")

    return {"img":base64.b64encode(buf.getbuffer()).decode("ascii"), "info_about_sort": old_graphs}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/server/get_new_graphs/<new_sort_name>/<data_size>', methods=["POST"])
def generate_new_graphs(new_sort_name, data_size):
    old_graphs = request.get_json()
    return get_new_graphs(old_graphs, new_sort_name, int(data_size))

@app.route('/server/get_old_graphs/<data_size>', methods={"POST"})
def generate_old_graphs(data_size):
    old_graphs = request.get_json()
    mask = old_graphs["a"]
    arr2 = old_graphs["value"]
    return get_old_graphs(mask, arr2, int(data_size))


if __name__ == "__main__":
    app.run(debug=True)
