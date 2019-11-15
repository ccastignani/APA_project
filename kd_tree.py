import numpy as np

class Node:
    """ """
    def __init__(self, compound_id = None, left_child = None, right_child = None):
        """ """
        self.compound_id = compound_id
        self.left_child = left_child
        self.right_child = right_child

class KDTree:
    """ Implementation of a KDtree """

    def __init__(self, compound_dict):
        """ """
        self.compound_dict = compound_dict
        self.compound_matrix = self.create_compound_matrix(compound_dict)
        self.root = self.build_tree(self.compound_matrix)


    def create_compound_matrix(self, compound_dict):
        """ """
        compound_matrix = []
        for key, value in compound_dict.items():
            row = value.featureVector
            row = np.append(row, np.array(key))
            compound_matrix.append(row)
            #print(row)
        return compound_matrix

    def build_tree(self, compound_matrix, depth=0):
        """ """
        # Last case (Leaf nodes)
        if not compound_matrix:
            return None

        # Length of dimensions, equal for all the elements, pick the first one
        k = len(compound_matrix[0])-1
        # Check which is the current dimension being considered
        current_dimension = depth % k
        # Sort the elements based on the current_dimension
        compound_matrix.sort(key=lambda x: x[current_dimension])
        #print(compound_matrix)
        #print("----")
        median = len(compound_matrix) // 2

        # Create node and construct subtrees
        node = Node()
        node.compound_id = compound_matrix[median][-1]
        node.left_child = self.build_tree(compound_matrix[:median], depth + 1)
        node.right_child = self.build_tree(compound_matrix[median + 1:],
                                           depth + 1)
        return node

    def print_tree(self):
        """ """
        nodes = [self.root]
        while len(nodes) != 0:
            current_node = nodes.pop(0)
            if(current_node is not None):
                print(current_node.compound_id)
                print(self.compound_dict[current_node.compound_id].featureVector)
                nodes.append(current_node.left_child)
                nodes.append(current_node.right_child)
            else:
                print("None")

    # TODO: this is only a draft version
    def group(self, node, d, k):
        """ """
        nodes = [self.root]
        while len(nodes) != 0:
            current_node = nodes.pop(0)
            if(current_node is not None):
                print(current_node.compound_id)
                print(self.compound_dict[current_node.compound_id].featureVector)

                if not self.KDcompare(node.left_child, node, d, True) == "RIGHT":
                    nodes.append(current_node.left_child)
                if not self.KDcompare(node.right_child, node,d) == "LEFT":
                    nodes.append(current_node.right_child)

    # TODO: this is only a draft version
    def KDcompare(self, child, node, d, subtract = False):
        """ """
        return child



