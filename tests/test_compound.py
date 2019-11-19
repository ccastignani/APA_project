import pytest

from morphocell import compound

class TestCompound(object):
    def test_parse_file(self):
        imaging_profile = "./tests/test_data/profiles.txt"
        feature_names_file = "./tests/test_data/features.txt"
        feature_list = [
            "Cells_AreaShape_Area", 
            "Cells_AreaShape_Compactness", 
            "Cells_AreaShape_Eccentricity"
        ]

        compounds_dict = compound.Compound.parse_file(imaging_profile, feature_names_file, feature_list)
