##### Author: Bryson Galapon
##### Email: brysongalapon@gmail.com

# Library of Common Data Structures and Algorithms

This repo provides a library of various commonly used data structures and algorithms. This is useful for junior developers (such as myself) to look and play around with working code instead of pseudocode, as a learning experience. This library is also useful for practical scenarios in which one quickly needs a data structure / algorithm and doesn't want to bother implementing it by hand.

Data structures like Queues/Stacks, Heaps, LinkedLists, HashTables/HashSets, etc. either exist as an already built-in library in your programming language, or are trivial to implement and are thus exempted from this library.

## Performance: 
  The functions and data-structures provided have been only designed to meet asymptotic runtime and space requirements as documented. **NO** special effort was made to optimize implementation, so performance may vary.  

Supported Languages:
  - Python3

## Data Structures:
  - Trees
    - Balanced Binary Search Tree (BST)
    - Segment Tree
    - Trie

  - Union-Find

  - Van Embde Boas

## Algorithms:
  - Graphs
    - Breadth First Search (BFS)
    - Depth First Search (DFS)

  - Trees
    - Binary Tree Traversals
      1. In Order
      2. Pre Order
      3. Post Order

    - Euler Tour

  - Sorting:
    - Merge Sort
    - Quick Sort
    - Counting Sort
    - Radix Sort

  - Range Minimum Query (RMQ)
  - Z algorithm

## Testing Framework:
  - unittest
    - Invariant:
      All test file names must be in the format [srcFileName]Tests.py, and the test path should be the same relative to its corresponding src path. For example, if a src file named __myFile.py__ has path src/foo/bar/myFile.py, its corresponding test file must have the path tests/foo/bar/myFileTests.py 
    - If file myFileA.py depends on another file myFileB.py (e.g. myFileA.py calls "import myFileB"), then if myFileA.py has a test file, myFileB.py **must also** have a test file, even if that test file is empty (contains no unit tests).


