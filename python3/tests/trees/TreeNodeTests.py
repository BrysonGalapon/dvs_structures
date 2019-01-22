"""
Test Suite for TreeNode class. 

Do NOT run this file by hand -- instead run the "[path-to-dvs_structures]/dvs_structures/python3/tests/run_all.sh" script
"""

from TreeNode import TreeNode
import unittest

class TreeNodeTests(unittest.TestCase):
    def testNoChildrenOnInit(self):
        treeNode = TreeNode(key=1, val=3)
        self.assertEqual(len(treeNode.getChildren()), 0, "Expected 0 children for newly created TreeNode")

if __name__ == "__main__":
    unittest.main(verbosity=2)

