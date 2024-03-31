import ctypes
import random


if __name__ == "__main__":
    try:
        lib = ctypes.cdll.LoadLibrary("build/libsorts.so")
        lib.bubble_sort_with_timer.restype = ctypes.c_double
        lib.insertion_sort_with_timer.restype = ctypes.c_double
        py_values = [random.randint(1, 1000) for _ in range(1_000_000)]

        arr_1 = (ctypes.c_int * len(py_values))(*py_values)
        arr_2 = (ctypes.c_int * len(py_values))(*py_values)

        print(lib.bubble_sort_with_timer(arr_1, len(arr_1)))
        print(lib.insertion_sort_with_timer(arr_2, len(arr_2)))
    except Exception as ex:
        print(ex)
    