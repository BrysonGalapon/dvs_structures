"""
Test Suite for UnionFind class. 

Do NOT run this file by hand -- instead run the "[path-to-dvs_structures]/dvs_structures/python3/tests/run_all.sh" script
"""

from UnionFind import UnionFind
import unittest

class UnionFindTests(unittest.TestCase):
    def testFind(self):
        elements = [1,2,3,4,5,6,7]
        uf = UnionFind(elements)

        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(6), 6)
        self.assertNotEqual(uf.find(7), 5)

    def testUnion(self):
        elements = [1,2,3,4,5,6,7]
        uf = UnionFind(elements)

        self.assertEqual(uf.find(6), 6)
        
        uf.union(6, 7)
        self.assertTrue(uf.find(6) in set([6,7]))
        self.assertTrue(uf.find(7) in set([6,7]))
        self.assertFalse(uf.find(3) in set([6,7]))

        uf.union(5,3)
        self.assertFalse(uf.find(3) in set([6,7]))
        self.assertTrue(uf.find(5) in set([5,3]))

        uf.union(3, 6)
        self.assertTrue(uf.find(5) in set([3,5,6,7]))
        self.assertTrue(uf.find(7) in set([3,5,6,7]))
        self.assertTrue(uf.find(3) in set([3,5,6,7]))
        self.assertTrue(uf.find(6) in set([3,5,6,7]))

    def testGetRoots(self):
        elements = ["2", 1, "tomato", 6, 9, 5.2]
        uf = UnionFind(elements)

        self.assertTrue(set(elements), uf.getRoots())

        uf.union("tomato", 1)

        self.assertEqual(5, len(uf.getRoots()), "Expected number of roots to go down by 1")
        self.assertTrue(uf.getRoots().issubset(set(elements)), "Expected roots to be subset of original set of elements")

        uf.union(1, "2")

        self.assertEqual(4, len(uf.getRoots()), "Expected number of roots to go down by 1 after 1 extra union")

        uf.union(1, "tomato")

        self.assertEqual(4, len(uf.getRoots()), "Expected number of roots to not go down when unioning elements of the same set")

    def testUnionNotIntegers(self):
        elements = ["bye", "a", "80", "cat"]
        uf = UnionFind(elements)

        uf.union("a", "80")
        uf.union("80", "cat")

        self.assertFalse(uf.find("bye") in set(["80", "a", "cat"]))
        self.assertTrue(uf.find("a") in set(["80", "a", "cat"]))
        self.assertTrue(uf.find("cat") in set(["80", "a", "cat"]))
        self.assertTrue(uf.find("80") in set(["80", "a", "cat"]))

    def testGetRootSizes(self):
        elements = ["bye", "a", "80", "cat"]
        uf = UnionFind(elements)

        root_sizes = uf.getRootSizes()
        for root in root_sizes:
            self.assertEqual(1, root_sizes[root], "Expected each root to have 1 element on init")

        uf.union("bye", "cat")
        uf.union("a", "80")

        root_sizes = uf.getRootSizes()
        for root in root_sizes:
            self.assertEqual(2, root_sizes[root], "Expected each root to have 2 elements based on paired unions")

        uf.union("a", "cat")

        root_sizes = uf.getRootSizes()
        for root in root_sizes:
            self.assertEqual(4, root_sizes[root], "Expected single root to have size 4")

    def testGetSize(self):
        elements = list(range(2, 200))
        uf = UnionFind(elements)

        # union all ints in range {90, 91, ... 140} inclusive
        for i in range(90, 140):
            uf.union(i, i+1) 
            
        # union all ints in range {180, 181 ... 195} inclusive
        for i in range(180, 195):
            uf.union(i, i+1) 

        self.assertEqual(51, uf.getSize(90), "Expected any int in range [90, 140] inclusive to have size 51")
        self.assertEqual(51, uf.getSize(93), "Expected any int in range [90, 140] inclusive to have size 51")
        self.assertEqual(51, uf.getSize(140), "Expected any int in range [90, 140] inclusive to have size 51")

        self.assertEqual(16, uf.getSize(180), "Expected any int in range [180, 195] inclusive to have size 16")
        self.assertEqual(16, uf.getSize(186), "Expected any int in range [180, 195] inclusive to have size 16")
        self.assertEqual(16, uf.getSize(195), "Expected any int in range [180, 195] inclusive to have size 16")

        self.assertEqual(1, uf.getSize(8), "Expected any int outside any range to have size 1")
        self.assertEqual(1, uf.getSize(89), "Expected any int outside any range to have size 1")
        self.assertEqual(1, uf.getSize(141), "Expected any int outside any range to have size 1")
        self.assertEqual(1, uf.getSize(179), "Expected any int outside any range to have size 1")
        self.assertEqual(1, uf.getSize(196), "Expected any int outside any range to have size 1")

        uf.union(92, 181)

        self.assertEqual(67, uf.getSize(90), "Expected any int in either range to have size 51+16=67")
        self.assertEqual(67, uf.getSize(91), "Expected any int in either range to have size 51+16=67")
        self.assertEqual(67, uf.getSize(139), "Expected any int in either range to have size 51+16=67")
        self.assertEqual(67, uf.getSize(140), "Expected any int in either range to have size 51+16=67")
        self.assertEqual(67, uf.getSize(180), "Expected any int in either range to have size 51+16=67")
        self.assertEqual(67, uf.getSize(186), "Expected any int in either range to have size 51+16=67")
        self.assertEqual(67, uf.getSize(195), "Expected any int in either range to have size 51+16=67")

        self.assertEqual(1, uf.getSize(8), "Expected any int outside any range to still have size 1")
        self.assertEqual(1, uf.getSize(89), "Expected any int outside any range to still have size 1")
        self.assertEqual(1, uf.getSize(141), "Expected any int outside any range to still have size 1")
        self.assertEqual(1, uf.getSize(179), "Expected any int outside any range to still have size 1")
        self.assertEqual(1, uf.getSize(196), "Expected any int outside any range to still have size 1")

if __name__ == "__main__":
    unittest.main(verbosity=2)

