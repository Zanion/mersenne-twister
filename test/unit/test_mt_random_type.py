import pytest
from mt_random_type import MT


def test_same_seed_rand():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand() == mt2.rand()


def test_same_seed_rand_int():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand_int() == mt2.rand_int()


def test_same_seed_rand_int31():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand_int31() == mt2.rand_int31()


def test_same_seed_rand_real1():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand_real1() == mt2.rand_real1()


def test_same_seed_rand_real2():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand_real2() == mt2.rand_real2()


def test_same_seed_rand_real3():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand_real3() == mt2.rand_real3()


def test_same_seed_rand_res53():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand_res53() == mt2.rand_res53()

