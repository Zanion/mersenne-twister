cimport mt_struct

cdef class MT:
    """ MT Wrapper """
    cdef mt_struct.mt_state *_thisptr


    def __cinit__(self, unsigned long s):
        self._thisptr = mt_struct.make_mt(s)
        if self._thisptr == NULL:
            raise MemoryError()


    def __dealloc__(self):
        mt_struct.free_mt(self._thisptr)


    cpdef double rand(self):
        """ Convenience wrapper for rand_real1 """
        return mt_struct.genrand_real1(self._thisptr)


    cpdef int rand_int(self):
        """ Generates a random number on interval [0, 0xFFFFFFFF] """
        return mt_struct.genrand_int32(self._thisptr)


    cpdef long rand_int31(self):
        """ Generates a random number on interval [0, 0x7FFFFFFF] """
        return mt_struct.genrand_int31(self._thisptr)


    cpdef double rand_real1(self):
        """ Generates a random number on real interval [0, 1] """
        return mt_struct.genrand_real1(self._thisptr)


    cpdef double rand_real2(self):
        """ Generates a random number on real interval [0, 1) """
        return mt_struct.genrand_real2(self._thisptr)


    cpdef double rand_real3(self):
        """ Generates a random number on real interval (0, 1) """
        return mt_struct.genrand_real3(self._thisptr)


    cpdef double rand_res53(self):
        """ Generates a random 53-bit number on interval [0, 1) """
        return mt_struct.genrand_res53(self._thisptr)

