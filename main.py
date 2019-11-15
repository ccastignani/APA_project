import argparse

from compound import Compound
from kd_tree import KDTree

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This programs creates a KD tree from imaging profiling files.")
    parser.add_argument('-i', '--imaging_profile',
                        dest="imaging_profile",
                        action="store",
                        default="./test_data/profiles.txt",
                        help="The imaging profile file")
    parser.add_argument('-f', '--featues_name',
                        dest="featues_name",
                        action="store",
                        default="./test_data/features.txt",
                        help="The featues name file")
    parser.add_argument('-l', '--featue_list',
                        dest="feature_list",
                        action="store",
                        nargs="*",
                        default=[
                            "Cells_AreaShape_Area", 
                            "Cells_AreaShape_Compactness", 
                            "Cells_AreaShape_Eccentricity"
                            ],
                        help="The featues list to evaluate")

    options = parser.parse_args()

    imaging_profile = options.imaging_profile
    feature_names_file = options.featues_name
    feature_list = options.feature_list
    
    # Read files
    compounds_dict = Compound.parse_file(imaging_profile, feature_names_file, feature_list)

    # Get two compounds and print the requested dimensions and distance
    compound_one = compounds_dict["BRD-K98301999-001-01-1"]
    compound_two = compounds_dict["BRD-K05686172-001-01-6"]

    requested_features = [
        "Cells_AreaShape_Area",
        "Cells_AreaShape_Eccentricity"
    ]

    print("=== Distance from two compounds ===")
    print("Compound one: %s - %s" %(compound_one.broad_id, compound_one.get_features(requested_features)))
    print("Compound two: %s - %s" %(compound_two.broad_id, compound_two.get_features(requested_features)))
    print("Distance: %s" %compound_one.distance(compound_two, "Cells_AreaShape_Area", "Cells_AreaShape_Eccentricity"))

    print("=== Creation of KD Tree and print in inorder ===")
    # Create and print kd tree in inorder
    kd_tree = KDTree(compounds_dict)
    kd_tree.print_tree()