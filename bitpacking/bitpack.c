/**************************************************************
 *
 *                     bitpack.c
 *
 *     Author:  Vedant Modi (vedantmodi.com)
 *     Date:     30 Aug 2024
 *
 *     Summary:
 *     bitpack implementation file
 *
 **************************************************************/

#include "bitpack.h"
#include <assert.h>

bool Bitpack_unsigned_fit(uint64_t n, unsigned width)
{
    assert(width <= 64);
    return (width == 64) ? 0 : n << width;
}
