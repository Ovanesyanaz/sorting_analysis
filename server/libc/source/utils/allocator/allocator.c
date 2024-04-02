#include "allocator.h"

#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

void *allocate(size_t size) 
{
    void *p = malloc(size);
    if (!p) {
        printf(BAD_ALLOC_MESSAGE);
        exit(1);
    }

    return p;
}

void deallocate(void* p) { free(p); }