import ctypes
import random
import os


if __name__ == "__main__":
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lib = ctypes.cdll.LoadLibrary(dir_path + "/build/libsorts.so")
        lib.bubble_sort_with_timer.restype = ctypes.c_double
        lib.insertion_sort_with_timer.restype = ctypes.c_double
        py_values = [random.randint(1, 1000) for _ in range(10_000)]

        arr_1 = (ctypes.c_int * len(py_values))(*py_values)
        arr_2 = (ctypes.c_int * len(py_values))(*py_values)

        print(lib.bubble_sort_with_timer(arr_1, len(arr_1)))
        print(lib.insertion_sort_with_timer(arr_2, len(arr_2)))
    except Exception as ex:
        print(ex)
    