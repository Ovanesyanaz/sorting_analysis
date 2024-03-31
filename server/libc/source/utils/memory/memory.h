#ifndef __MEMORY_H__
#define __MEMORY_H__

#include <stddef.h>

void copy(void* p, size_t dest_size,
          const void* s, size_t source_size);

#endif // __MEMORY_H__