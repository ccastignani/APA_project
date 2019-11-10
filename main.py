
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



# class KDtree:
#     """
#     Implementation of a KDtree
#     """
#     global root

#     def __init__(self, root, *argv):
#         self.root = root
#         self.features = *argv

#     def insert(self, node):
#         return

#     def remove(self, node):
#         return

#     def group(self, x, d, k, *argv):
#         return
