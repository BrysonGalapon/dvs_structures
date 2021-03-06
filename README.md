##### Author: Bryson Galapon
##### Email: brysongalapon@gmail.com

# Library of Common Data Structures and Algorithms

This repo provides a library of various commonly used data structures and algorithms. This library is useful for practical scenarios in which one quickly needs a data structure / algorithm and doesn't want to bother implementing it by hand. This is also useful for junior developers (such as myself) to look and play around with real, working code instead of pseudocode. The devil is in the details! 

Special focus was given to data structures that are "annoying" to implement by hand, or in other words require some minimum threshold of thinking to implement correctly. Data structures like Queues/Stacks, Heaps, LinkedLists, HashTables/HashSets, etc. are **exempted** from this library, since either they exist as an already built-in or imported library (most modern languages), or are trivial to implement. The only exception to this rule are algorithms (e.g. BFS and MergeSort) that are pivotal building blocks of Computer Science, and will be included!

Each module will be completely self-contained. In other words, all dependencies (if any) will be included as files within that module, even if it results in copied files across modules. For example, since BFS and DFS are both graph search algorithms, both must have access to some (possibly equivalent) Graph representation, which is implemented in (say) _Graph.py_. The BFS and DFS module will have their **own** _Graph.py_ file, even though the contents of the file might be equivalent. Repeated code is often considered bad coding practice, but for this application I wanted these modules to be as "plug-n-play" as much as possible; by making these modules self-contained, one is able to simply copy the folder of the module of interest into one's project without worrying about tracking down all the other file dependencies.   

## Performance: 
  The functions and data-structures provided have been only designed to meet _asymptotic_ runtime and space requirements, as documented within the corresponding source file. Beyond that, **NO** special effort was made to optimize constant factors, so performance may vary.  

Supported Languages:
  - Python3

## Data Structures:
  - Trees\*
    - AVL Tree (Balanced BST)
    - Splay Tree (Pseudo-Balanced BST with great performance)
    - Segment Tree
    - Trie

  - Union-Find

  - Van Embde Boas

## Algorithms:
  - Graphs\*
    - Breadth First Search (BFS)
      1. Iterative
      2. Recursive
    - Depth First Search (DFS)
      1. Iterative
      2. Recursive
    - Topological Sort
      1. Iterative
      2. Recursive

  - Trees\*
    - Euler Tour

  - Sorting\*
    - Merge Sort
    - Quick Sort
    - Counting Sort
    - Radix Sort

  - Range Minimum Query (RMQ)\*
  
  - Z algorithm\*

## Testing Framework:
  - unittest
    - All test file names must be in the format [srcFileName]Tests.py, and the test path should be the same relative to its corresponding src path. For example, if a src file named 'myFile.py' has path 'src/foo/bar/myFile.py', its corresponding test file must have the path 'tests/foo/bar/myFileTests.py' 
    - If file myFileA.py depends on another file myFileB.py (e.g. myFileA.py calls "import myFileB"), then if myFileA.py has a test file, myFileB.py **must also** have a test file, even if that test file is empty (contains no unit tests).

## Special Notes:
  - An asterisk (\*) next to a modules name means that the module is in progress, and is not yet fully implemented/tested.

