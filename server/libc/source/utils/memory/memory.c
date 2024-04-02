#include "memory.h"

#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include "utils/error/error.h"

void copy(void* d, size_t dest_size,
          const void* s, size_t source_size)
{
    if (dest_size != source_size) {
        printf("%s %s", BAD_ARG_MESSAGE, "Destination size is not equal source size\n");
        exit(2);
    }

    memcpy(d, s, source_size);
}