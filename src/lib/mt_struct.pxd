cdef extern from "mt19937ar-struct.h":
    ctypedef struct mt_state
    mt_state *make_mt(unsigned long s)
    void free_mt(mt_state *state)
    int genrand_int32(mt_state *state)
    long genrand_int31(mt_state *state)
    double genrand_real1(mt_state *state)
    double genrand_real2(mt_state *state)
    double genrand_real3(mt_state *state)
    double genrand_res53(mt_state *state)
