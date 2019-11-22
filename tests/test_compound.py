import pytest
import numpy as np

from morphocell import compound


class TestCompound(object):
    def test_distance(self):
        id1 = compound.Compound("ID-1", np.array([1, 1, 1]))
        id2 = compound.Compound("ID-2", np.array([1, 1, 2]))

        assert id1.distance(id2) == 1

    def test_parse(self):
        feature_list = ["Cells_AreaShape_Area"]
        dict = compound.Compound.parse_file("tests/test_data/profiles.txt",
                                            "tests/test_data/features.txt",
                                            feature_list)
        assert(dict["BRD-K13714335-001-01-0"].get_dimensions()[0] == 3965.396)
