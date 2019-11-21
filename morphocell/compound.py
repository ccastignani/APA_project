import numpy as np
from collections import defaultdict

import morphocell.utils as utils


class Compound:
    """ Class representing a compound """

    feature_list = []

    def __init__(self, broad_id, feature_vector, feature_list=None):
        """ Creator of a compound """
        self.broad_id = broad_id
        self.feature_vector = feature_vector

    def __str__(self):
        """ Magic method to print a node """
        return "%s - %s" % (self.broad_id, str(self.feature_vector))

    def get_id(self):
        """ 'Interface method' to be compatible with kd tree """
        return self.broad_id

    def get_dimensions(self):
        """ 'Interface method' to be compatible with kd tree """
        return self.get_features()

    def set_features(self,features):
        """ 'Interface method' to be compatible with kd tree """
        self.feature_vector = features

    def get_features(self, *feature_names):
        """ Method that returns the features listed in argv """
        if not feature_names:
            return self.feature_vector
        else:
            features_requested = []
            for feature in feature_names:
                try:
                    feature_index = Compound.feature_list.index(feature)
                    features_requested.append(self.feature_vector[feature_index])
                except ValueError as e:
                    print("Unrecognized feature: %s" % e)
            return features_requested

    def distance(self, x, *argv):
        """ Return the distance between two compounds """
        # argv is a list of the names of the features which have to be used
        # for the calculation of the distance
        return utils.euclidean_distance(self.get_features(*argv), x.get_features(*argv))

    @staticmethod
    def parse_file(imaging_profile, feature_names_file, feature_list):
        """ Static method that returns a dictionary of compounds from a file"""
        Compound.feature_list = feature_list

        f = open(feature_names_file, "r")

        # Collect the indexes of the Input Features and save them in a List
        feature_index = []
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[1] in feature_list:
                feature_index.append(line[0])

        # Read the file with the morphological information line per line
        with open(imaging_profile) as fp:
            first_line = fp.readline()

        index_list = []
        for i in first_line.strip().split('\t'):
            if i in feature_index:
                index_list.append(first_line.strip().split('\t').index(i))

        all_compounds_dict = defaultdict(dict)
        with open(imaging_profile) as fp:
            for line in fp.readlines()[1:]:
                compound_vector = []
                if line.strip().split('\t')[0] != 'DMSO':
                    for i in index_list:
                        compound_vector.append(float(line.strip().split('\t')[i]))

                    if line.strip().split('\t')[0] in all_compounds_dict.keys():
                        mean_feature_vector = (all_compounds_dict[line.strip().split('\t')[0]].feature_vector + np.array(compound_vector))/2
                        all_compounds_dict[line.strip().split('\t')[0]] = Compound(line.strip().split('\t')[0], mean_feature_vector)
                    else:
                        all_compounds_dict[line.strip().split('\t')[0]] = Compound(line.strip().split('\t')[0], np.array(compound_vector))

        return all_compounds_dict
