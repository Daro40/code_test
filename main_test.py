import numpy as np
import pytest
from main import zeros_to_end

arr0 = [0,1,0,0]
expected0 = [1,0,0,0]
arr = [0, 3, 4, 6, 21, 0, 3, 0, 0, 2, 4, 1, 5, 7, 8, 0, 3234, 2534, 0, 524, 65, 42, 1, 6, 0, 788, 65, 7, 7]
arr2 = [0, 3, 4, 6, 21, 0, 3, 2, 4, 1, 5, 7, 8, 0, 0, 524, 65, 42, 1, 6, 0, 788, 65, 7, 7]
expected = [3, 4, 6, 21, 3, 2, 4, 1, 5, 7, 8, 3234, 2534, 524, 65, 42, 1, 6, 788, 65, 7, 7, 0, 0, 0, 0, 0, 0, 0]
expected2 = [3, 4, 6, 21, 3, 2, 4, 1, 5, 7, 8, 524, 65, 42, 1, 6, 788, 65, 7, 7, 0, 0, 0, 0, 0]

@pytest.mark.parametrize("test_input,expected", [(arr0, expected0),(arr, expected), (arr2, expected2)])

def test_zeros_to_end(test_input,expected):
    # Given an array of numbers, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
    #arr = [0, 3, 4, 6, 21, 0, 3, 0, 0, 2, 4, 1, 5, 7, 8, 0, 3234, 2534, 0, 524, 65, 42, 1, 6, 0, 788, 65, 7, 7]
    #expected = [3, 4, 6, 21, 3, 2, 4, 1, 5, 7, 8, 3234, 2534, 524, 65, 42, 1, 6, 788, 65, 7, 7, 0, 0, 0, 0, 0, 0, 0]
    processed_array = zeros_to_end(test_input, len(test_input))
    assert np.array_equal(np.array(processed_array), np.array(expected))
