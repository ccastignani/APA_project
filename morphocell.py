#!/usr/bin/env python3

import argparse

from morphocell.compound import Compound
from morphocell.kd_tree import KDTree


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This programs does an aproximate neighbour search of an imaging file using a KD-tree structure.")
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

    print("\n")
    print("==================================")
    print(" Cell Morphology Analysis Package")
    print("==================================")
    print("\n\n")
    print("===== Reading imaging file =====")
    compounds_dict = Compound.parse_file(imaging_filename,
                                         feature_filename, feature_list)
    print("===== File readed succesfully =====")
    print("===== Creating KD Tree structure from imaging file ====")
    kd_tree = KDTree(compounds_dict, normalize_flag)
    print("===== Kd tree created succesfully =====")
    #kd_tree.print_tree()
    print("===== Group function over compound id =====")
    selected_compound = compounds_dict[compound_id]
    print("\n")
    print("Compound selected for neighbour searches: %s - (%s)" % (selected_compound.broad_id, selected_compound.get_features()))
    print("\n")
    print("Nearest neighbours:")
    nearest_neighbour = kd_tree.group(selected_compound, distance, max_neighbours+1, *feature_list)
    for compound, distance in nearest_neighbour:
        print("%s - %s, distance -> %s" % (compound.get_id(), compound.get_features(), distance))
    print("\n\n")
