#include "dynamic_array.h"

#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include "utils/allocator/allocator.h"
#include "utils/memory/memory.h"
#include "utils/error/error.h"

size_t da_int_size(da_int *da) { return da->_size; }
size_t da_int_capacity(da_int *da) { return da->_capacity; }
int *da_int_start(da_int *da) { return da->_elem; }
da_int *da_int_reserve(da_int *da, size_t new_capacity);

da_int *da_int_create(size_t size, size_t capacity)
{
    if (size > capacity) {
        printf("%s %s", BAD_ARG_MESSAGE, "Size more than capacity\n");
        exit(3);
    }

    da_int *new_da = (da_int*)allocate(sizeof(da_int));
    int *elem = (int*)allocate(capacity*sizeof(int));

    for (int i = 0; i < size; ++i) {
        elem[i] = 0;
    }

    new_da->_capacity = capacity;
    new_da->_size = size;
    new_da->_elem = elem;

    return new_da;
}

da_int *da_int_from_array(da_int *da, int *array, size_t size)
{
    da_int *new_da = da_int_create(0, size);
    copy(new_da->_elem, size * sizeof(int), array, size * sizeof(int));
    new_da->_size = size;

    return new_da;
}

int *da_int_at(const da_int *da, int index)
{
    if (da->_size <= index) {
        printf("%s %s", BAD_ARG_MESSAGE, "invalid index\n");
        exit(4);
    }

    return da->_elem + index;
}

int *da_int_unsafe_at(const da_int *da, int index)
{
    return da->_elem + index;
}

int da_int_pop(da_int *da)
{
    if (da->_size < 1) {
        printf("%s%s", EMPTY_DA_MESSAGE, "\n");
        exit(5);
    }

    --da->_size;
    return (da->_elem)[da->_size + 1];
}

da_int *da_int_push_back(da_int *da, int value)
{
    if (da->_capacity > da->_size) {
        (da->_elem)[da->_size] = value;
        ++da->_size;

        return da;
    }

    da_int *new_da = da_int_reserve(da, da->_capacity * 2 + 1);
    (new_da->_elem)[new_da->_size] = value;
    ++new_da->_size;

    return new_da;
}

da_int *da_int_reserve(da_int *da, size_t new_capacity)
{
    if (new_capacity <= da->_capacity) {
        return da;
    }

    da_int *new_da = da_int_create(0, new_capacity);
    copy(new_da->_elem, da->_size * sizeof(int), da->_elem, da->_size * sizeof(int));
    new_da->_size = da->_size;

    da_int_destroy(da);

    return new_da;
}

void da_int_destroy(da_int *da)
{
    if (!da) {
        printf("%s%s", NULLPTR_MESSAGE, "\n");
        exit(6);
    }

    if (da->_elem) {
        deallocate(da->_elem);
    }

    deallocate(da);
}