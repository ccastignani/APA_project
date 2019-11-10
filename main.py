

class Compound:

    def __init__(self, id, name, featureVector):
        self.id = id
        self.name = name
        self.featureVector = featureVector

    def distance(self, x, *argv):
        # argv is a list of the names of the features which have to be used
        # for the calculation of the distance
        # Distance: eucledian
        return


class Node:

    def __init__(self, compound_index, left_child, right_child):
        self.compound_index = compound_index
        self.left_child = left_child
        self.right_child = right_child

class KDtree:
    """ Implementation of a KDtree """

    def __init__(self, compound_dict):
        self.compound_dict = compound_dict
        self.compound_matrix = self.create_compound_matrix(compound_dict)
        self.root = self.build_tree(self.compound_matrix)

    def create_compound_matrix():
        return

    def build_tree(self, compound_matrix, depth=0):

        # Last case (Leaf nodes)
        if not compound_matrix:
            return None

        # Length of dimensions, equal for all the elements, pick the first one
        k = len(compound_matrix[0])
        # Check which is the current dimension being considered
        current_dimension = depth % k
        # Sort the elements based on the current_dimension
        compound_matrix.sort(key=lambda x: x[current_dimension])
        median = len(compound_matrix) // 2

        # Create node and construct subtrees
        node = Node()
        node.compound_index = compound_matrix[median]
        node.left_child = self.build_tree(compound_matrix[:median], depth + 1)
        node.right_child = self.build_tree(compound_matrix[median + 1:],
                                           depth + 1)
        return node

    def group(self, x, d, k, *argv):
        return
