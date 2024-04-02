
#ifndef __TIMER_H__
#define __TIMER_H__

#include <time.h>
#include <stdio.h>
#include <stddef.h>

#define TIME_IT(func, ...) do { clock_t start = clock(); func(__VA_ARGS__); return ((double) (clock() - start)) / CLOCKS_PER_SEC; } while (0)

#endif // __TIMER_H__