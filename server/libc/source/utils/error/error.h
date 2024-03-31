#ifndef __ERROR_H__
#define __ERROR_H__

#include <stdbool.h>
#include <stddef.h>

typedef struct error {
    bool ok;
    char message[];
} error_t; 

#define BAD_ARG_MESSAGE "Not valid value!"
#define NULLPTR_MESSAGE "Null pointer is received!"

#endif // __ERROR_H__