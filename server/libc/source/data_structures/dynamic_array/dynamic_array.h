#ifndef __DYNAMIC_ARRAY_H__
#define __DYNAMIC_ARRAY_H__

#include <stddef.h>

#define EMPTY_DA_MESSAGE "Dynamic array is empty!"

typedef struct da_int {
    size_t _capacity;
    size_t _size;
    int *_elem;
} da_int;

da_int *da_int_create(size_t size, size_t capacity);
da_int *da_int_from_array(da_int *da, int *array, size_t size);
size_t da_int_size(da_int *da);
size_t da_int_capacity(da_int *da);
int *da_int_start(da_int *da);
int *da_int_at(const da_int *da, int index);
int *da_int_unsafe_at(const da_int *da, int index);
int da_int_pop(da_int *da);
da_int *da_int_push_back(da_int *da, int value);
void da_int_destroy(da_int *da);

#endif // __DYNAMIC_ARRAY_H__