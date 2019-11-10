

class Compound:

    def __init__(self, id, name,featureVector):
        self.id = id
        self.name = name
        self.featureVector = featureVector

    def distance(self, x, *argv):
        # argv is a list of the names of the features which have to be used
        # for the calculation of the distance
        # Distance: eucledian
        return


class KDtree:
    """
    Implementation of a KDtree
    """
    global root

    def __init__(self, root, *argv):
        self.root = root
        self.features = *argv

    def insert(self, node):
        return

    def remove(self, node):
        return

    def group(self, x, d, k, *argv):
        return
