import numpy as np


class Node:
    """ Node class of the kd tree """

    def __init__(self, id=None, left_child=None, right_child=None):
        """ Creator of a node """
        self.id = id
        self.left_child = left_child
        self.right_child = right_child


class KDTree:
    """ KD Tree data structure """

    def __init__(self, data_dictionary, normalize=False):
        """ Creator of a kd tree from the given data_dictionary """
        self.data_dictionary = data_dictionary
        self.data_matrix = self.__create_data_matrix(data_dictionary, normalize)
        self.root = self.__build(self.data_matrix)

    def __create_data_matrix(self, data_dictionary, normalize):
        """ Convert the data dictionary to a matrix """
        data_matrix = []
        for key, value in data_dictionary.items():
            row = value.get_dimensions()
            row = np.append(row, np.array(key))
            data_matrix.append(row)

        # Normalize if needed and return
        if not normalize:
            return data_matrix
        else:
            data_matrix = np.array(data_matrix)
            data_matrix = data_matrix.transpose()
            # skip last row, all the IDs
            row_sum = row_sums = data_matrix[:-1, ].astype(float).sum(axis=1)
            # add one dimension more, for zip
            row_sum = np.append(row_sum, np.array(None))
            new_matrix = np.zeros((data_matrix.shape))

            # Normalization
            for i, (row, row_sum) in enumerate(zip(data_matrix, row_sum)):
                try:
                    new_matrix[i, :] = row.astype(float) / row_sum
                    # last row with IDs, do not normalize
                except:
                    new_matrix = np.row_stack([new_matrix[:-1, ], row])
            # Update the dictionary
            for key, value in self.data_dictionary.items():
                self.data_dictionary[key].set_features(np.array(self.data_dictionary[key].get_dimensions().astype(float))/np.array(row_sums))
            new_matrix = new_matrix.transpose()
            return new_matrix.tolist()

    def __build(self, data_matrix, depth=0):
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
        node.left_child = self.__build(data_matrix[:median], depth + 1)
        node.right_child = self.__build(data_matrix[median + 1:], depth + 1)
        return node

    def print_tree(self):
        """ Print tree traversing it in inorder """
        self.__print_tree_i(self.root)

    def __print_tree_i(self, node):
        """ Insider function for print recursion """
        if(node is not None):
            self.__print_tree_i(node.left_child)
            print("%s - %s" % (node.id, self.data_dictionary[node.id]))
            self.__print_tree_i(node.right_child)

    def group(self, x, d, k, *argv):
        """ Method to retrieve the k nearest neighbours at most d distance """
        near_nodes_list = self.__nearest_neighbor(x.get_id(), d, *argv)
        near_nodes_list.sort(key=lambda x: x[1])

        result_nodes = []
        for node in near_nodes_list[:k]:
            result_nodes.append((self.data_dictionary[node[0]], node[1]))
        return result_nodes

    def __nearest_neighbor(self, node_id, d, *dimensions):
        node_data = self.data_dictionary[node_id].get_dimensions()
        # Defines the radius (distance)
        min_values = node_data - d
        max_values = node_data + d

        # Flag to see if the node itself already has been visited
        self_visited = False

        result_node_id = []

        # Nodes to still be checked added in the queue
        # 0 is the depth at the beginning
        node_queue = [(self.root, 0)]
        while node_queue:
            current_node = node_queue.pop(0)
            # If we are not in a leaf
            if current_node[0] is not None:
                # When we find the node, change the flag!
                if node_id == current_node[0].id:
                    self_visited = True
                # Extract the feature vector from the current node
                data_current_node = self.data_dictionary[current_node[0].id].get_dimensions()
                # We now check if we are in the radius
                if (data_current_node >= min_values).all() and (data_current_node <= max_values).all():
                    # Add both of the children
                    nodes_to_add = [current_node[0].left_child,
                                    current_node[0].right_child]
                    # if the distance is less than threshold - save
                    distance_to_node = self.data_dictionary[node_id].distance(self.data_dictionary[current_node[0].id], *dimensions)
                    if distance_to_node <= d:
                        result_node_id.append((current_node[0].id,
                                               distance_to_node))
                    # Check if we can exclude a path
                    if self.__compare(min_values,
                                      data_current_node,
                                      current_node[1]) == "RIGHT":
                        # Discard left path
                        nodes_to_add[0] = None
                    if self.__compare(max_values,
                                      data_current_node,
                                      current_node[1]) == "LEFT":
                        # Discard right path
                        nodes_to_add[1] = None

                    # here
                    if not self_visited:
                        if self.__compare(node_data, data_current_node, current_node[1]) == "RIGHT":
                            nodes_to_add[1] = current_node[0].right_child
                        else:
                            nodes_to_add[0] = current_node[0].left_child
                    for child in nodes_to_add:
                        if child is not None:
                            node_queue.append((child, current_node[1]+1))

                # If the node is still not found - forced to continue in the
                # Correct direction
                elif not self_visited:
                    if self.__compare(node_data, data_current_node, current_node[1]) == "RIGHT":
                        node_queue.append((current_node[0].right_child, current_node[1]+1))
                    else:
                        node_queue.append((current_node[0].left_child, current_node[1]+1))

        return result_node_id

    def __compare(self, data_node_p, data_node_q, depth):
        """ Method that returns child of node_q to that belongs node_p """
        # Length of dimensions minus 1, as we added the id
        # as another dimension in the matrix
        k = len(self.data_matrix[0])-1
        # Check the current dimension to be evaluated
        current_dimension = depth % k
        if data_node_p[current_dimension] < data_node_q[current_dimension]:
            return "LEFT"
        return "RIGHT"
