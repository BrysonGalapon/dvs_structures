from TreeNode import TreeNode

class BinaryTreeNode(TreeNode):
    def __init__(self, key, val):
        super().__init__(key, val)

        # initialize left and right subtree pointers to None
        #   left = children[0]
        #   right = children[1]
        self.children.extend([None, None])

    """
    Get left subtree pointer for this BinaryTreeNode
    :rtype BinaryTreeNode:
    """
    def left(self):
        return self.children[0]
    
    """
    Get right subtree pointer for this BinaryTreeNode
    :rtype BinaryTreeNode:
    """
    def right(self):
        return self.children[1]


