
import numpy as np
from collections import defaultdict

class Compound:


    def __init__(self, broad_id, featureVector):
        self.id = broad_id
        self.featureVector = featureVector

    # def distance(self, x, *argv):
    #     # argv is a list of the names of the features which have to be used
    #     # for the calculation of the distance
    #     # Distance: eucledian
    #     return



class Node:

    def __init__(self, compound_id, left_child, right_child):
        self.compound_id = compound_id
        self.left_child = left_child
        self.right_child = right_child

class KDtree:
    """ Implementation of a KDtree """

    def __init__(self, compound_dict):
        self.compound_dict = compound_dict
        self.compound_matrix = self.create_compound_matrix(compound_dict)
        self.root = self.build_tree(self.compound_matrix)

    def create_compound_matrix(compound_dict):
        compound_matrix = []
        for key, value in compound_dict.items():
            row = value.featureVector
            row.append(key)
            compound_matrix.append(row)
        return compound_matrix

    def build_tree(self, compound_matrix, depth=0):

        # Last case (Leaf nodes)
        if not compound_matrix:
            return None

        # Length of dimensions, equal for all the elements, pick the first one
        k = len(compound_matrix[0])-1
        # Check which is the current dimension being considered
        current_dimension = depth % k
        # Sort the elements based on the current_dimension
        compound_matrix.sort(key=lambda x: x[current_dimension])
        median = len(compound_matrix) // 2

        # Create node and construct subtrees
        node = Node()
        node.compound_id = compound_matrix[median][-1]
        node.left_child = self.build_tree(compound_matrix[:median], depth + 1)
        node.right_child = self.build_tree(compound_matrix[median + 1:],
                                           depth + 1)
        return node

    def print_tree(self):
        nodes = [self.root]
        while len(nodes) != 0:
            current_node = nodes.pop()
            print(current_node.compound_id)
            nodes.append(current_node.left_child)
            nodes.append(current_node.right_child)




def parse_file(imaging_profile, feature_names_file, feature_list= ["Cells_AreaShape_Area", "Cells_AreaShape_Compactness", "Cells_AreaShape_Eccentricity", "Cells_AreaShape_Perimeter", "Cytoplasm_AreaShape_Area", "Cytoplasm_AreaShape_Eccentricity", "Cytoplasm_AreaShape_Perimeter", "Nuclei_AreaShape_Area", "Nuclei_AreaShape_Eccentricity", "Nuclei_AreaShape_Perimeter"]):
	
	f = open(feature_names_file, "r")

	feature_index = []
	for line in f.readlines():
		line= line.strip().split('\t')
		if line[1] in feature_list:
			feature_index.append(line[0])


	with open(imaging_profile) as fp:
		first_line = fp.readline()


	index_list= []
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
					mean_feature_vector = (all_compounds_dict[line.strip().split('\t')[0]].featureVector + np.array(compound_vector))/2

					all_compounds_dict[line.strip().split('\t')[0]] = Compound(line.strip().split('\t')[0], mean_feature_vector)


				else:
					all_compounds_dict[line.strip().split('\t')[0]] = Compound(line.strip().split('\t')[0], np.array(compound_vector))

	return all_compounds_dict




if __name__ == '__main__':
	
	imaging_profile= "/Users/carla/Downloads/Broad.HG005032.ProfilingData/imaging/cdrp.imaging.profiles.txt"
	feature_names_file= "/Users/carla/Downloads/Broad.HG005032.ProfilingData/imaging/cdrp.imaging.feature.names.txt"

	all_compounds_dict = parse_file(imaging_profile, feature_names_file)
	print(all_compounds_dict.keys())


