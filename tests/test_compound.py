import pytest
import numpy as np

from morphocell import compound

class TestCompound(object):
    def test_distance(self):
        id1 = compound.Compound("ID-1", np.array([1,1,1]))
        id2 = compound.Compound("ID-2", np.array([1,1,2]))

        assert id1.distance(id2) == 1