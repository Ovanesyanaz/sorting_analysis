#ifndef __SORTS_PYTHON_H__
#define __SORTS_PYTHON_H__

#include <stddef.h>
#include "utils/timer/timer.h"

void bubble_sort(int *array, size_t size);
void insertion_sort(int *array, size_t size);
void selection_sort(int *array, size_t size);
void quick_sort(int *array, size_t size);
void merge_sort(int *array, size_t size);
void heap_sort(int *array, size_t size);
void shell_sort(int *array, size_t size);

double bubble_sort_with_timer(int *array, size_t size) { TIME_IT(bubble_sort, array, size); }
double insertion_sort_with_timer(int *array, size_t size) { TIME_IT(insertion_sort, array, size); }
double selection_sort_with_timer(int *array, size_t size) { TIME_IT(selection_sort, array, size); }
double quick_sort_with_timer(int *array, size_t size) { TIME_IT(quick_sort, array, size); }
double merge_sort_with_timer(int *array, size_t size) { TIME_IT(merge_sort, array, size); }

#endif // __SORTS_PYTHON_H__