#include "swap.h"

#include "stdlib.h"
#include "memory.h"

void swap_three(void *a, void *b, void *tmp, int size_t);
void swap_alloca(void *a, void *b, int size_t);
void swap_malloc(void *a, void *b, int size_t);

void __attribute__( (noinline) ) swap(void *a, void *b, int size_t) 
{
    if (size_t <= 16) {
        swap_alloca(a, b, size_t);
        return;
    }

    swap_malloc(a, b, size_t);
}

void swap_alloca(void *a, void *b, int size_t)
{
    void *tmp = alloca(size_t);
    swap_three(a, b, tmp, size_t);
}

void swap_malloc(void *a, void *b, int size_t)
{
    void *tmp = malloc(size_t);
    swap_three(a, b, tmp, size_t);
}

void swap_three(void *a, void *b, void *tmp, int size_t)
{
    memcpy(tmp, a, size_t);
    memcpy(a, b, size_t);
    memcpy(b, tmp, size_t);
}