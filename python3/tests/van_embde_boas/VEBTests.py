"""
Test Suite for VEB class. 

Do NOT run this file by hand -- instead run the "[path-to-dvs_structures]/dvs_structures/python3/tests/run_all.sh" script
"""

from VEB import VEB
import unittest

class VEBTests(unittest.TestCase):
    def testSuccessor(self):
        veb = VEB(u=2**64)

        veb.insert(0)
        veb.insert(2)
        veb.insert(7)

        self.assertEqual(veb.successor(0), 2, "Expected successor of 0 to be 2")
        self.assertEqual(veb.successor(1), 2, "Expected successor of 1 to be 2")
        self.assertEqual(veb.successor(2), 7, "Expected successor of 2 to be 7")
        self.assertEqual(veb.successor(3), 7, "Expected successor of 3 to be 7")
        self.assertEqual(veb.successor(6), 7, "Expected successor of 6 to be 7")
        self.assertEqual(veb.successor(7), -1, "Expected no successor of 7, return -1")
        self.assertEqual(veb.successor(8), -1, "Expected no successor of 8, return -1")

    def testPredecessor(self):
        veb = VEB(u=2**32)

        veb.insert(0)
        veb.insert(1000)
        veb.insert(2000)

        self.assertEqual(veb.predecessor(0), -1, "Expected no predecessor of 0, return -1")
        self.assertEqual(veb.predecessor(1), 0, "Expected predecessor of 1 to be 0")
        self.assertEqual(veb.predecessor(2), 0, "Expected predecessor of 2 to be 0")
        self.assertEqual(veb.predecessor(600), 0, "Expected predecessor of 600 to be 0")
        self.assertEqual(veb.predecessor(1000), 0, "Expected predecessor of 1000 to be 0")
        self.assertEqual(veb.predecessor(1001), 1000, "Expected predecessor of 1001 to be 1000")
        self.assertEqual(veb.predecessor(1303), 1000, "Expected predecessor of 1303 to be 1000")
        self.assertEqual(veb.predecessor(2000), 1000, "Expected predecessor of 2000 to be 1000")
        self.assertEqual(veb.predecessor(2009), 2000, "Expected predecessor of 2009 to be 2000")
        self.assertEqual(veb.predecessor(2023391), 2000, "Expected predecessor of super large number to be maximum element")

    def testInsertAllPredecessor(self):
        veb = VEB(u=2**32)

        A = list(range(0, 100))
        veb.insertAll(A)
#        print(veb)

        for a in A[1:]:
            self.assertEqual(veb.predecessor(a), a-1, "Expected predecessor of {} to be {}".format(a, a-1))

    def testInsertAllSuccessor(self):
        veb = VEB(u=2**32)

        A = list(range(0, 100))
        veb.insertAll(A)

        for a in A[:-1]:
            self.assertEqual(veb.successor(a), a+1, "Expected successor of {} to be {}".format(a, a+1))

    def testInsert(self):
        veb = VEB(u=2**32)

        self.assertEqual(veb.successor(12), -1, "Expected no successor of 12, return -1")
        self.assertEqual(veb.predecessor(40), -1, "Expected no predecessor of 12, return -1")

        veb.insert(38)

        self.assertEqual(veb.successor(12), 38, "Expected successor of 12 to be 38")
        self.assertEqual(veb.predecessor(40), 38, "Expected predecessor of 40 to be 38")

    def testDelete(self):
        veb = VEB(u=2**32)

        veb.insert(38)

        # deleting a number that doesn't exist in VEB should not crash the DS
        veb.delete(80)

        self.assertEqual(veb.successor(12), 38, "Expected successor of 12 to be 38")
        self.assertEqual(veb.predecessor(40), 38, "Expected predecessor of 40 to be 38")

        veb.delete(38)

        self.assertEqual(veb.successor(12), -1, "Expected no successor of 12, return -1")
        self.assertEqual(veb.predecessor(40), -1, "Expected no predecessor of 12, return -1")

if __name__ == "__main__":
    unittest.main(verbosity=2)

