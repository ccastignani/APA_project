import numpy as np

class Node:
    """ Node class of the kd tree """
    
    def __init__(self, id = None, left_child = None, right_child = None):
        """ Creator of a node """
        self.id = id
        self.left_child = left_child
        self.right_child = right_child

class KDTree:
    """ KD Tree data structure """

    def __init__(self, data_dictionary):
        """ Creator of a kd tree from the given data_dictionary """
        self.data_dictionary = data_dictionary
        self.data_matrix = self.create_data_matrix(data_dictionary)

        self.root = self.build(self.data_matrix)

    def create_data_matrix(self, data_dictionary):
        """ Convert the data dictionary to a matrix """
        data_matrix = []
        for key, value in data_dictionary.items():
            row = value.get_dimensions()
            row = np.append(row, np.array(key))
            data_matrix.append(row)
        return data_matrix

    def build(self, data_matrix, depth=0):
        """ Recursive funtion to create the kd tree """
        # Last case (Leaf nodes)
        if not data_matrix:
            return None

        # Length of dimensions minus 1, as we added the id as another dimension in the matrix
        k = len(data_matrix[0])-1

        # Check the current dimension to be evaluated
        current_dimension = depth % k
        # Sort the elements based on the current_dimension and get the median
        data_matrix.sort(key=lambda x: x[current_dimension])
        median = len(data_matrix) // 2

        # Create node and construct subtrees
        node = Node()
        node.id = data_matrix[median][-1]
        node.left_child = self.build(data_matrix[:median], depth + 1)
        node.right_child = self.build(data_matrix[median + 1:], depth + 1)
        return node

    def print_tree(self):
        """ Print tree traversing it in inorder """
        self.__print_tree_i(self.root)

    def __print_tree_i(self, node):
        """ Insider function for print recursion """
        if(node is not None):
            self.__print_tree_i(node.left_child)
            print("%s - %s" %(node.id, self.data_dictionary[node.id]))
            self.__print_tree_i(node.right_child)

    # TODO: this is only a draft version
    def group(self, node, d, k):
        """ Method to retrieve the k nearest neighbours at most d distance """
        nodes = [self.root]
        while len(nodes) != 0:
            current_node = nodes.pop(0)
            if(current_node is not None):
                print(current_node.id)
                print(self.data_dictionary[current_node.id])

                if not self.compare(node.left_child, node, d, True) == "RIGHT":
                    nodes.append(current_node.left_child)
                if not self.compare(node.right_child, node,d) == "LEFT":
                    nodes.append(current_node.right_child)

    # TODO: this is only a draft version
    def compare(self, child, node, d, subtract = False):
        """ Method to compare two nodes """
        return child



