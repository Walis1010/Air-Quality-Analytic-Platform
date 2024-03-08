# Test the utility functions

import pytest
from utils import sumvalues, maxvalue, minvalue, meanvalue, countvalue

def test_sumvalues():
    assert sumvalues([1, 2, 3]) == 6
    assert sumvalues([-1, 0, 1]) == 0
    with pytest.raises(ValueError, match="The input list is empty, this operation cannot be performed."):
        sumvalues([])
    with pytest.raises(ValueError):
        sumvalues(['a', 2, 3])


def test_maxvalue():
    assert maxvalue([1, 2, 3]) == 3
    assert maxvalue([-1, 0, 1]) == 1
    with pytest.raises(ValueError, match="The input list is empty, this operation cannot be performed."):
        maxvalue([])
    with pytest.raises(ValueError):
        maxvalue(['a', 2, 3])


def test_minvalue():
    assert minvalue([1, 2, 3]) == 1
    assert minvalue([-1, 0, 1]) == -1
    with pytest.raises(ValueError, match="The input list is empty, this operation cannot be performed."):
        minvalue([])
    with pytest.raises(ValueError):
        minvalue(['a', 2, 3])


def test_meanvalue():
    assert meanvalue([1, 2, 3]) == 2
    assert meanvalue([-1, 0, 1]) == 0
    with pytest.raises(ValueError, match="The input list is empty, this operation cannot be performed."):
        meanvalue([])
    with pytest.raises(ValueError):
        meanvalue(['a', 2, 3])


def test_countvalue():
    assert countvalue([1, 2, 2, 3, 2], 2) == 3
    assert countvalue([-1, 0, 1, 0, 0], 0) == 3
    with pytest.raises(ValueError, match="The input list is empty, this operation cannot be performed."):
        countvalue([], 1)
    with pytest.raises(ValueError):
        countvalue(['a', 2, 'b', 3, 'c'], 'a')
