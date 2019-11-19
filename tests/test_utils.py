import pytest

from morphocell import utils

class TestUtils(object):
    def test_euclidean_distance(self):
        vector_a = [1, 1, 1]
        vector_b = [2, 2, 2]
        assert round(utils.euclidean_distance(vector_a, vector_b),5) == 1.73205
