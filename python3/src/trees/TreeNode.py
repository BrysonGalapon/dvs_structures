class TreeNode(object):
    """
    Constructs a new TreeNode object

    :type key: Immutable type (e.g. int, string, double, etc.)
    :type val: Undefined (e.g. None, list of ints, set of strings, etc.)
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.children = []

    """
    Obtain a (internal reference) to a list of children of this TreeNode
    :rtype: List[TreeNode]
    """
    def getChildren(self):
        return self.children
