#include "dynamic_array.h"

#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include "utils/allocator/allocator.h"
#include "utils/memory/memory.h"
#include "utils/error/error.h"

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

    new_da->capacity = capacity;
    new_da->size = size;
    new_da->elem = elem;

    return new_da;
}

da_int *da_int_from_array(da_int *da, int *array, size_t size)
{
    da_int *new_da = da_int_create(0, size);
    copy(new_da->elem, size * sizeof(int), array, size * sizeof(int));
    new_da->size = size;

    return new_da;
}

int *da_int_at(const da_int *da, int index)
{
    if (da->size <= index) {
        printf("%s %s", BAD_ARG_MESSAGE, "invalid index\n");
        exit(4);
    }

    return da->elem + index;
}

int *da_int_unsafe_at(const da_int *da, int index)
{
    return da->elem + index;
}

int da_int_pop(da_int *da)
{
    if (da->size < 1) {
        printf("%s%s", EMPTY_DA_MESSAGE, "\n");
        exit(5);
    }

    --da->size;
    return da->elem[da->size + 1];
}

da_int *da_int_push_back(da_int *da, int value)
{
    if (da->capacity > da->size) {
        ++da->size;
        da->elem[da->size] = value;

        return da;
    }

    da_int *new_da = da_int_reserve(da, da->capacity * 2);
    ++new_da->size;
    new_da->elem[new_da->size] = value;

    return new_da;
}

da_int *da_int_reserve(da_int *da, size_t new_capacity)
{
    if (new_capacity <= da->capacity) {
        return da;
    }

    da_int *new_da = da_int_create(0, new_capacity);
    copy(da->elem, da->size * sizeof(int), new_da->elem, da->size * sizeof(int));
    new_da->size = da->size;

    da_int_destroy(da);

    return new_da;
}

void da_int_destroy(da_int *da)
{
    if (!da) {
        printf("%s%s", NULLPTR_MESSAGE, "\n");
        exit(6);
    }

    if (da->elem) {
        deallocate(da->elem);
    }

    deallocate(da);
}