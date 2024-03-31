#include "sorts.h"

// #include "data_structures/dynamic_array/dynamic_array.h"
#include <stddef.h>
#include <stdio.h>
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

// void selection_sort(da_int *da)
// {
     
// }

// void quick_sort(da_int *da)
// {

// }

// void merge_sort(da_int *da)
// {

// }

// void heap_sort(da_int *da)
// {

// }

// void shell_sort(da_int *da)
// {

// }