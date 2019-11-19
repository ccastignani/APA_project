import pytest

import numpy as np

from morphocell import kd_tree
from morphocell import compound

class TestKDTree(object):
    def test_nearest_neighbour(self):
        id1 = compound.Compound("ID-1", np.array([1,1,1]))
        id2 = compound.Compound("ID-2", np.array([1,1,2]))
        id3 = compound.Compound("ID-3", np.array([1,2,2]))
        id4 = compound.Compound("ID-4", np.array([2,2,2]))
        id5 = compound.Compound("ID-5", np.array([2,2,3]))

        init_dict = {
            "ID-1": id1,
            "ID-2": id2,
            "ID-3": id3,
            "ID-4": id4,
            "ID-5": id5
        }
        tree = kd_tree.KDTree(init_dict)

        #assert tree.group(id4,2, 2) == [id3, id2]

    def test_compare(self):
        id1 = compound.Compound("ID-1", np.array([1,1,1]))
        id5 = compound.Compound("ID-5", np.array([2,2,2]))

        init_dict = {
            "ID-1": id1,
            "ID-5": id5
        }
        tree = kd_tree.KDTree(init_dict)

        assert tree.compare(id1.get_dimensions(), id5.get_dimensions(), 1) == "LEFT"

