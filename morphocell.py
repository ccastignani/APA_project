#!/usr/bin/env python3

import argparse

from morphocell.compound import Compound
from morphocell.kd_tree import KDTree


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This programs do an aproximate neighbour search of an imagin file unsing a KD tree structure.")
    parser.add_argument('-i', '--imaging_profile',
                        dest="imaging_profile",
                        action="store",
                        required=True,
                        help="The imaging profile file")
    parser.add_argument('-f', '--featues_name',
                        dest="featues_name",
                        action="store",
                        required=True,
                        help="The featues name file")
    parser.add_argument('-c', '--compound_id',
                        dest="compound_id",
                        action="store",
                        required=True,
                        help="The compound id to look for neighbour")
    parser.add_argument('-d', '--distance',
                        dest="distance",
                        action="store",
                        type=int,
                        required=True,
                        help="The distance treshold for neighbour search")
    parser.add_argument('-k', '--max_neighbours',
                        dest="max_neighbours",
                        action="store",
                        type=int,
                        required=True,
                        help="The maximum number of neighbours")
    parser.add_argument('-l', '--feature_list',
                        dest="feature_list",
                        action="store",
                        nargs="*",
                        help="The featues list to evaluate")
    parser.add_argument('--normalize',
                        dest="normalize",
                        action="store_true",
                        help="Use if you want to normalize the data")

    options = parser.parse_args()

    imaging_filename = options.imaging_profile
    feature_filename = options.featues_name
    compound_id = options.compound_id
    distance = options.distance
    max_neighbours = options.max_neighbours
    feature_list = options.feature_list
    normalize_flag = options.normalize

    if not feature_list:
        feature_list = [
        "Cells_AreaShape_Area",
        "Cells_AreaShape_Compactness",
        "Cells_AreaShape_Eccentricity",
        "Cells_AreaShape_Perimeter",
        "Cytoplasm_AreaShape_Area",
        "Cytoplasm_AreaShape_Eccentricity",
        "Cytoplasm_AreaShape_Perimeter",
        "Nuclei_AreaShape_Area",
        "Nuclei_AreaShape_Eccentricity",
        "Nuclei_AreaShape_Perimeter"
        ]

    print("\n\n")
    print("==================================")
    print(" Cell Morphology Analysis Package")
    print("==================================")
    print("\n\n")
    import numpy as np
    from morphocell import compound
    from morphocell import kd_tree
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

    exit()
    print("===== Reading imaging file =====")
    compounds_dict = Compound.parse_file(imaging_filename,
                                         feature_filename, feature_list)
    print("===== File readed succesfully =====")
    print("===== Creating KD Tree structure from imaging file ====")
    kd_tree = KDTree(compounds_dict, normalize_flag)
    print("===== Kd tree created succesfully =====")
    kd_tree.print_tree()
    print("==== Group function over compound id ====")
    selected_compound = compounds_dict[compound_id]
    print("\n")
    print("Compound selected for neighbour searches: %s - (%s)" % (selected_compound.broad_id, selected_compound.get_features()))
    print("\n")
    print("Nearest neighbours:")
    nearest_neighbour = kd_tree.group(selected_compound, distance, max_neighbours+1, *feature_list)
    for compound, distance in nearest_neighbour:
        print("%s - %s, distance -> %s" % (compound.get_id(), compound.get_features(), distance))
