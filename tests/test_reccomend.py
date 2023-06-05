import pytest
from backend.reccomend import build_user_arr
import numpy as np

def test_build_user_arr():
    string = '110110'
    length = 6
    arr = build_user_arr(string, length)
    ass_arr = np.array([1, 1, 0, 1, 1, 0])  # it stands for 'assert array'

    assert np.array_equal(arr, ass_arr)
