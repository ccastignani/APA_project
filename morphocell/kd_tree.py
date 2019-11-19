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

    def group(self, x, d, k, *argv):
        """ Method to retrieve the k nearest neighbours at most d distance """
        near_nodes_list = self.nearest_neighbor(x.get_id(), d, argv)
        near_nodes_list.sort(key=lambda x: x[1])

        result_nodes = []
        for node in near_nodes_list[:k]:
            result_nodes.append(self.data_dictionary[node[0]])
        return result_nodes

    def nearest_neighbor(self, node_id, d, dimension_names=None):
        node_data = self.data_dictionary[node_id].get_dimensions()
        min_values = node_data - d
        max_values = node_data + d

        result_node_id = []

        node_queue = [(self.root,0)]
        while node_queue:
            current_node = node_queue.pop(0)
            if current_node[0] is not None:
                data_current_node = node_data = self.data_dictionary[current_node[0].id].get_dimensions()
                if (data_current_node >= min_values).all() and (data_current_node <= max_values).all():
                    nodes_to_add = [current_node[0].left_child, current_node[0].right_child]
                    distance_to_node = self.data_dictionary[node_id].distance(self.data_dictionary[current_node[0].id])
                    if distance_to_node <= d:
                        result_node_id.append((current_node[0].id, distance_to_node))
                    if self.compare(min_values, data_current_node, current_node[1]) == "RIGHT":
                        #Discard left path
                        nodes_to_add[0] = None
                    if self.compare(max_values, data_current_node, current_node[1]) == "LEFT":
                        #Discard right path
                        nodes_to_add[1] = None
                    for child in nodes_to_add:
                        if child is not None:
                            node_queue.append((child, current_node[1]+1))
        return result_node_id

    def compare(self, data_node_p, data_node_q, depth):
        """ Method that returns child of node_q that belongs node_p """
        # Length of dimensions minus 1, as we added the id as another dimension in the matrix
        k = len(self.data_matrix[0])-1
        # Check the current dimension to be evaluated
        current_dimension = depth % k

        if data_node_p[current_dimension] < data_node_q[current_dimension]:
            return "RIGTH"
        return "LEFT"

