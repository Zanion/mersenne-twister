import pytest
from mt_random_type import MT


def test_same_seed():
    """ Assert independent instances """
    # Given two instances of MT with same seed
    mt1, mt2 = MT(0), MT(0)

    # When I call rand(), then I observe they have independent state (same result)
    for i in range(1000):
        assert mt1.rand() == mt2.rand()

