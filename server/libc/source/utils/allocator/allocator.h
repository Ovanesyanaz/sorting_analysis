#ifndef __ALLOCATOR_H__
#define __ALLOCATOR_H__

#include <stddef.h>
#include <stdlib.h>

#define BAD_ALLOC_MESSAGE "Memory was not allocated\n"

void *allocate(size_t size);
void deallocate(void* p);

#endif // __ALLOCATOR_H__
