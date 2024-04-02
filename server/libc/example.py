import ctypes
import random
import os

from typing import Callable


def test_sort(sort: Callable, data: list[int], name: str) -> None:
    size = len(data)
    c_array = (ctypes.c_int * size)(*data)

    print(f"\n==={name}_sort===\n")

    print(f"{size=}")
    print(f"array before: {c_array[size - 10:]}")
    print(f"time: {sort(c_array, size)}")
    print(f"array after: {c_array[size - 10:]}")

    print("\n===\n")


if __name__ == "__main__":
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lib = ctypes.cdll.LoadLibrary(dir_path + "/build/libsorts.so")

        lib.bubble_sort_with_timer.restype = ctypes.c_double
        lib.insertion_sort_with_timer.restype = ctypes.c_double
        lib.selection_sort_with_timer.restype = ctypes.c_double
        lib.quick_sort_with_timer.restype = ctypes.c_double
        lib.merge_sort_with_timer.restype = ctypes.c_double

        py_values = [random.randint(1, 1000) for _ in range(10_000)]

        test_sort(lib.bubble_sort_with_timer, py_values, "bubble")
        test_sort(lib.insertion_sort_with_timer, py_values, "insertion")
        test_sort(lib.selection_sort_with_timer, py_values, "selection")
        test_sort(lib.quick_sort_with_timer, py_values, "quick")
        test_sort(lib.merge_sort_with_timer, py_values, "merge")

    except Exception as ex:
        print(ex)

