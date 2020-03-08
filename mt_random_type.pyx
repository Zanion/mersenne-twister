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
        return mt_struct.genrand_real1(self._thisptr)
