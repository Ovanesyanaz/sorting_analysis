#include "sorts.h"

#include <stddef.h>
#include <stdio.h>
#include "data_structures/dynamic_array/dynamic_array.h"
#include "utils/memory/memory.h"
#include "utils/swap/swap.h"

void bubble_sort(int *array, size_t size)
{
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size - 1; ++j) {
            int *a = array + j;
            int *b = array + j+1;

            if (*a > *b) {
                swap(a, b, sizeof(int));
            }
        }
    }
}

void insertion_sort(int *array, size_t size)
{
    for (int i = 1; i < size; ++i) {
        for (int j = i; j > 0; --j) {
            int *a = array + j;
            int *b = array + j - 1;

            if (*a < *b) {
                swap(a, b, sizeof(int));
            }
        }
    }
}

void selection_sort(int *array, size_t size)
{
    int first_elem_index = 0;

    for (int i = 0; i < size; ++i) {
        int *mn = array + first_elem_index;

        for (int j = first_elem_index + 1; j < size; ++j) {
            int *num = array + j;

            if (*num < *mn) {
                mn = num;
            }
        }

        swap(array + first_elem_index, mn, sizeof(int));
        ++first_elem_index;
    }    
}

void quick_sort(int *array, size_t size)
{
    if (size <= 0) {
        return;
    }

    int partition(int *array, size_t size, const int pivot) {
        const int pivot_val = array[pivot];
        swap(array + pivot, array + size - 1, sizeof(int));

        int less = 0;
        for (int i = 0; i < size - 1; ++i) {
            if (array[i] <= pivot_val) {
                swap(array + i, array + less, sizeof(int));
                ++less;
            }
        }

        swap(array + less, array + size - 1, sizeof(int));
        return less;
    }

    int pivot = partition(array, size, size - 1);
    quick_sort(array, pivot);
    quick_sort(array + pivot + 1, size - pivot - 1);
}

void merge_sort(int *array, size_t size)
{
    if (size <= 1) {
        return;
    }

    void merge(int *array, int median, size_t size) {
        da_int *buffer = da_int_create(0, 0);
        int i = 0;
        int j = median;

        while (i < median && j < size) {
            if (array[i] <= array[j]) {
                buffer = da_int_push_back(buffer, array[i]);
                ++i;
                continue;
            }

            buffer = da_int_push_back(buffer, array[j]);
            ++j;
        }

        while (i < median) {
            buffer = da_int_push_back(buffer, array[i]);
            ++i;
        }

        while (j < size) {
            buffer = da_int_push_back(buffer, array[j]);
            ++j;
        }

        copy(array, size * sizeof(int), da_int_start(buffer), size * sizeof(int));
        da_int_destroy(buffer);
    }

    size_t median = size / 2;

    merge_sort(array, median);
    merge_sort(array + median, size - median);
    merge(array, median, size);
}

// void heap_sort(da_int *da)
// {

// }

// void shell_sort(da_int *da)
// {

// }