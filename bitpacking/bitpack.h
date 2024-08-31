/**************************************************************
 *
 *                     bitpack.h
 *
 *     Author:  Vedant Modi (vedantmodi.com)
 *     Date:     30 Aug 2024
 *
 *     Summary:
 *     Bitpack header file
 *
 **************************************************************/
#ifndef BITPACK_INCLUDED
#define BITPACK_INCLUDED
#include <stdbool.h>
#include <stdint.h>

bool Bitpack_unsigned_fit(uint64_t n, unsigned width);
bool Bitpack_signed_fit(int64_t n, unsigned width);
uint64_t Bitpack_unsigned_get(uint64_t word, unsigned width, unsigned lsb);
int64_t Bitpack_signed_get(uint64_t word, unsigned width, unsigned lsb);
uint64_t Bitpack_unsigned_set(uint64_t word, unsigned width, unsigned lsb,
                              uint64_t value);
uint64_t Bitpack_signed_set(uint64_t word, unsigned width, unsigned lsb,
                            int64_t value);

#endif
