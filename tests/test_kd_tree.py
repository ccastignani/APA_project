import pytest

import numpy as np

from morphocell import kd_tree
from morphocell import compound


class TestKDTree(object):

    def test_build(self):
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
        assert (tree.root.id == "ID-3")
        assert (tree.root.left_child.id == "ID-2")
        assert (tree.root.left_child.left_child.id == "ID-1")
        assert (tree.root.right_child.id == "ID-5")
        assert (tree.root.right_child.left_child.id == "ID-4")

    def test_group(self):
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

        assert tree.group(id4,2, 2) == [(id4, 0), (id3, 1)]

    def test_compare(self):
        id1 = compound.Compound("ID-1", np.array([1,1,1]))
        id5 = compound.Compound("ID-5", np.array([2,2,2]))

        init_dict = {
            "ID-1": id1,
            "ID-5": id5
        }
        tree = kd_tree.KDTree(init_dict)

        assert tree._KDTree__compare(id1.get_dimensions(), id5.get_dimensions(), 1) == "LEFT"

    def test_data_matrix(self):
        id1 = compound.Compound("ID-1", np.array([1,10]))
        id2 = compound.Compound("ID-2", np.array([1,10]))
        id3 = compound.Compound("ID-3", np.array([1,20]))
        id4 = compound.Compound("ID-4", np.array([1,20]))
        id5 = compound.Compound("ID-5", np.array([1,40]))

        init_dict = {
            "ID-1": id1,
            "ID-2": id2,
            "ID-3": id3,
            "ID-4": id4,
            "ID-5": id5
        }
        tree = kd_tree.KDTree(init_dict)
        matrix_non_normalized = tree._KDTree__create_data_matrix(init_dict, False)
        matrix_normalized = tree._KDTree__create_data_matrix(init_dict, True)
        assert(float(matrix_non_normalized[0][1]) == 10)
        assert(float(matrix_normalized[0][1]) == 0.1)
        assert(float(matrix_non_normalized[0][0]) == 1)
        assert(float(matrix_normalized[0][0]) == 0.2)
