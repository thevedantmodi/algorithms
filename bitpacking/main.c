/**************************************************************
 *
 *                     main.c
 *
 *     Author:  Vedant Modi (vedantmodi.com)
 *     Date:     30 Aug 2024
 *
 *     Summary:
 *     Bitpack module
 *
 **************************************************************/

#include "bitpack.h"
#include <assert.h>
#include <stdio.h>

int main()
{

    assert(Bitpack_unsigned_fit(1, 2));

    return 0;
}