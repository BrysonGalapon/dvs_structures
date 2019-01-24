"""
Python implementation of UnionFind datastructure. Solves disjoint set problem.

Let alpha be the inverse Ackermann function (https://en.wikipedia.org/wiki/Ackermann_function),
    which is a super super super ... super slow growing function -- basically constant in
    all practical applications. 

    Proof: alpha(2^2^2^2^2^2) = alpha(2^65536) = 4

* Let n be the number of elements in the datastructure

Runtimes:
    - union: O(alpha(n)) amortized
    - find: O(alpha(n)) amortized
    - getRoots: O(1)
    - getSize: O(1)
    - getRootSizes: O(1)

Space:
    - O(n)
"""
class UnionFind(object):
    """
    Sets up Union-Find data structure

    :type elements: List[Undefined], where each element is a unique hashable object
    """
    def __init__(self, elements):
        n = len(elements)

        # save the elements for return
        self.elements = elements

        # maintain all the roots
        self.roots = set(elements)

        # maps each element to a unique id
        self.map = {}
        for i, el in enumerate(elements):
            self.map[el] = i

        # maintains number of elements in group for every root (only valid for root nodes)
        self.counts = [1]*n

        # self.parent[i] is the parent of i -- if i == self.parent[i] then i is a root
        self.parent = [i for i in range(n)]

    """
    Unions the sets of two distinct elements

    :type x: Undefined -- x must be an element of the constructor input list
    :type y: Undefined -- y must be an element of the constructor input list
    :rtype: void
    """
    def union(self, x, y):
        # check for valid input
        assert x in self.elements
        assert y in self.elements

        # obain representatives of each set
        root_x = self.find(x)
        root_y = self.find(y)

        # transform into indices
        rx = self.map[root_x]
        ry = self.map[root_y]

        if rx != ry:
            # must merge the two groups -- merge smaller group into larger group

            if self.counts[rx] < self.counts[ry]:
                self.parent[rx] = ry
                self.counts[ry] += self.counts[rx]
                if root_x in self.roots:
                    self.roots.remove(root_x)
            else:
                self.parent[ry] = rx
                self.counts[rx] += self.counts[ry]
                if root_y in self.roots:
                    self.roots.remove(root_y)

    """
    Obtains the representative element of the set corresponding to the given element

    :type x: Undefined -- x must be an element of the constructor input list
    :rtype: Undefined -- an element of the constructor input list
    """
    def find(self, x):
        # transform into indices
        x_id = self.map[x]

        # find the root of the group
        root = x_id
        while self.parent[root] != root:
            root = self.parent[root]

        # go back and make each node in the path point to root
        # AKA path compression
        curr = x_id
        while curr != root:
            # save the next parent
            par = self.parent[curr]

            # set new parent to the root
            self.parent[curr] = root

            # go to next parent
            curr = par

        return self.elements[root]

    """
    Obtains the set of representative elements for all sets in datastructure

    :rtype: Set[Undefined] -- elements must be elements of the constructor input list
    """
    def getRoots(self):
        return set(self.roots)

    """
    Obtains the size of the set containing this element
    :type x: Undefined -- x must be an element of the constructor input list
    """
    def getSize(self, x):
        assert x in self.elements
        return self.counts[self.map[self.find(x)]]

    """
    Obtains a mapping of set representative elements to the number of elements in each set (including the representative element)

    :rtype: Map[Undefined, int] -- each key is an element of the constructor input list, and the mapped integer is the number of elements in the disjoint set represented by the key
    """
    def getRootSizes(self):
        root_sizes = {}
        for root in self.roots:
            root_sizes[root] = self.counts[self.map[root]]
        return root_sizes
