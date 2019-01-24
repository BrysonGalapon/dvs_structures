from math import sqrt
from math import log

"""
Python implementation of Van-Embde-Boas datastructure. Solves the predecessor/successor problem.

For explanation of the following runtimes and space complexities, as well as 
    motivation for the DS and method implementations, see:
        https://www.youtube.com/watch?v=hmReJCupbNU

* Let u be the integer passed to the constructor of the VEB
* Let n be the number of integers currently in datastructure

Runtimes: 
    - successor: O( lg(lg(u)) )
    - predecessor: O( lg(lg(u)) )
    - insert: O( lg(lg(u)) )
    - delete: O( lg(lg(u)) )

Space: 
    - O(n * lg(lg(u)))
    * There is an implementation that utilizes O(n) space that uses the current implementation
        as a starting point. Please see final minutes of the video in the above link
        for more details.
"""
class VEB(object):
    """
    Creates a new Van-Embde-Boas structure where each int is contained in the range
        {0, 1, ... u-1}
    :type u: int, such that u = 2^2^k where k is a NONNEGATIVE integer
                Examples of valid u:
                    - u = 2 = 2^2^0
                    - u = 256 = 2^2^3
                    - u = 2^32 = 2^2^5
    """
    def __init__(self, u=2**32):
        validInput, err_msg = self._validU(u)
        assert (validInput), err_msg
        
        # smallest possible input for VEB
        self.SMALLEST_U = 2

        self.u = u
        self.min = None
        self.max = None

        # only store non-empty clusters
        self.cluster = {}
        
        if self.u == self.SMALLEST_U:
            # summary vec is just a list for base case
            self.summary = [-1,-1]
        else:
            self.summary = VEB(int(sqrt(u)))

    """
    Insert all integers in a list into the datastructure

    :type A: List[int], where each int x in A has 0 <= x <= u-1 
    :rtype: void
    """
    def insertAll(self, A):
        for a in A:
            self.insert(a)

    """
    Obtain the smallest element (not including x) in the structure that is greater than x
       - if the successor does not exist, return -1

    :type x: int, where 0 <= x <= u-1
    :rtype: int
    """
    def successor(self, x):
        validInput, err_msg = self._validX(x)
        assert (validInput), err_msg

        if self.min is not None and x < self.min:
            return self.min

        # base case
        if self.u == self.SMALLEST_U:
            # only return 1 if input is 0 and 1 exists in summary
            if x == 0 and 1 in self.summary:
                return 1
            else:
                return -1

        # recursive case
        i = self._high(x)

        # check if successor exists in cluster i
        if i in self.cluster and self.cluster[i].max is not None and self._low(x) < self.cluster[i].max:
            # if so, get it
            j = self.cluster[i].successor(self._low(x))
        else:
            # find correct cluster index for successor
            i = self.summary.successor(self._high(x))

            if i not in self.cluster: # couldn't find correct successor cluster
                return -1

            # found successor cluster, so get smallest element in that
            j = self.cluster[i].min

        return self._index(i, j)

    """
    Obtain the largest element (not including x) in the structure that is smaller than x
        - if the predecessor does not exist, return -1

    :type x: int, where 0 <= x <= u-1
    :rtype: int
    """
    def predecessor(self, x):
        validInput, err_msg = self._validX(x)
        assert (validInput), err_msg

        # if bigger than max, then predecessor is max
        if self.max is not None and x > self.max:
            return self.max

        # base case
        if self.u == self.SMALLEST_U:
            # only return 0 if input is 1 and 0 exists in summary
            if x == 1 and 0 in self.summary:
                return 0
            else:
                return -1

        # recursive case
        i = self._high(x)

        # check if predecessor exists in cluster i
        if i in self.cluster and self.cluster[i].min is not None and self._low(x) > self.cluster[i].min:
            # if so, get it
            j = self.cluster[i].predecessor(self._low(x))
        else: # predecessor not in cluster i, so look for correct cluster in summary
            i = self.summary.predecessor(i)

            if i not in self.cluster: # couldn't find correct predecessor cluster
                # possible that predecessor is self.min (since it's not stored recursively)
                if self.min is not None and x > self.min:
                    return self.min
                else:
                    return -1
            
            # found predecessor cluster, so get largest element in that
            j = self.cluster[i].max

        return self._index(i, j)

    """
    Insert a new integer x into the datastructure

    :type x: int, where 0 <= x <= u-1
    :rtype: void
    """
    def insert(self, x):
        validInput, err_msg = self._validX(x)
        assert (validInput), err_msg

        # update max normally
        if self.max is None or x > self.max:
            self.max = x
      
        # only update min/max flag when inserting into empty structure
        if self.min is None:
            self.min = x
            self.max = x

            # ... except if we are in the base case, in which case we must update
            #   the summary structure
            if self.u != self.SMALLEST_U:
                return

        # base case
        if self.u == self.SMALLEST_U:
            # simply add x to summary list
            self.summary[x] = x
            return

        # don't recursively store minimums, by swapping out current minimum with x
        if x < self.min:
            # swap places of x and self.min
            tmp = self.min
            self.min = x
            x = tmp

        # recursive case
        i = self._high(x)
        j = self._low(x)

        # inserting into cluster i, so create it if it doesn't already exist
        if i not in self.cluster:
            self.cluster[i] = VEB(int(sqrt(self.u)))

        if self.cluster[i].min is None:
            # update summary when i's cluster is empty
            self.summary.insert(i)

        # insert into cluster
        self.cluster[i].insert(j)

    """
    Deletes an integer x from the datastructure. If x is not in the datastructure, then 
        does nothing

    :type x: int, where 0 <= x <= u-1
    :rtype: void
    """
    def delete(self, x):
        validInput, err_msg = self._validX(x)
        assert (validInput), err_msg

        if x == self.min:
            i = self.summary.min
            if i is None: # check if all clusters are empty, and if so
                # set min and max flags to None (deleted last element)
                self.min = None
                self.max = None
                return
            # not all clusters are empty, so find next minimum element in DS, and set it to new min
            self.min = self._index(i, self.cluster[i].min)
            # that new minimum was stored recursively, but it's our invariant that the min isn't stored recursively. So set x to be the new minimum, and fall off to rest of delete code
            x = self.min

        # recursively delete x from it's cluster, if it exists
        if self._high(x) in self.cluster:
            self.cluster[self._high(x)].delete(self._low(x))

            # check if we deleted the last item in cluster
            if self.cluster[self._high(x)].min is None:
                # if we did, have to update the summary structure
                self.summary.delete(self._high(x))

        # possible that we recursively deleted the max, and must find new max
        if x == self.max:
            # check if there is any new max to find
            if self.summary.max is None:
                # if not, then max is simply self.min
                self.max = self.min
            else:
                # if so, get the max element in DS and set it to max
                i = self.summary.max
                self.max = self._index(i, self.cluster[i].max)

    """
    Obtain a representation of the VEB
    """
    def __str__(self):
        return self._toStringUtil(tab=0)

    """
    Helper function to get a representation of the VEB state
    Uses tabs to show deeper levels of recursion

    :type tab: int
    """
    def _toStringUtil(self, tab=0):
        s = ""

        s += "\t"*tab + "u: {}\n".format(self.u)
        s += "\t"*tab + "min: {}\n".format(self.min)
        s += "\t"*tab + "max: {}\n".format(self.max)
        s += "\t"*tab + "summary:\n"
 
        if self.u == self.SMALLEST_U:
            s += "\t"*(tab+1) + "{}\n".format(str(self.summary))
        else:
            s += self.summary._toStringUtil(tab+1)

        for cluster_id in self.cluster:
            s += "\t"*tab + "cluster {}:\n".format(cluster_id)
            s += "{}\n".format(self.cluster[cluster_id]._toStringUtil(tab+1))
        return s

    """
    Extract the first log(sqrt(u)) bits of x, interpreted as a number

    For example (x = 9, u = 16):
        - 9's bit representation is 1001
        - log(sqrt(16)) = 2, so the first 2 bits is 10
        - 10 is binary for 2, so this function will return 2

    :type x: int
    :rtype: int
    """
    def _high(self, x):
        if x == 0:
            return 0
        return x // int(sqrt(self.u))

    """
    Extract the last log(sqrt(u)) bits of x, interpreted as a number

    For example (x = 9, u = 16):
        - 9's bit representation is 1001
        - log(sqrt(16)) = 2, so the last 2 bits is 01
        - 01 is binary for 1, so this function will return 1

    :type x: int
    :rtype: int
    """
    def _low(self, x):
        if x == 0:
            return 0
        return x % int(sqrt(self.u))

    """
    Recombine the high and low parts of the number into its original value, given that
        they were split with current u

    If h or l is invalid (-1), return -1

    For example (h = 2, l = 1, u = 16)
        - index = h*sqrt(u)+l = 2*sqrt(16)+1 = 9
        - so this function will return 9

    :type h: int
    :type l: int
    :rtype: int
    """
    def _index(self, h, l):
        if h == -1 or l == -1:
            return -1
        return int(h * sqrt(self.u) + l)

    """
    Check if u is an int where u = 2^2^k for some nonnegative int k

    :type u: Undefined
    :rtype: bool, string -- where string is the error message if bool is False
    """
    def _validU(self, u):
        # check if u is an int
        if type(u) is not int:
            err_msg = "{} is not an integer".format(x)
            return False, err_msg

        # check if u is a power of 2
        if not self._isPowerOf2(u):
            err_msg = "{} is not a power of 2".format(u)
            return False, err_msg

        # check if exponent is a power of 2
        exponent = int(log(u, 2))
        if not self._isPowerOf2(exponent):
            err_msg = "{} is not a power of 2".format(exponent)
            return False, err_msg

        # passed all checks
        return True, ""
        
    """
    Check if x has x = 2^k for some nonnegative int k
    :type x: int
    :rtype: bool
    """
    def _isPowerOf2(self, x):
        # power of 2 is defined by having exactly 1 set bit in binary representation
        return bin(x).count("1") == 1
    
    """
    Check if x is an int in the range {0, 1, ... u-1}
    :type x: Undefined
    :rtype: bool, string -- where string is the error message if bool is False
    """
    def _validX(self, x):
        # check if x is an int
        if type(x) is not int:
            err_msg = "{} is not an integer".format(x)
            return False, err_msg

        # check if x is in the valid range
        if x < 0 or self.u <= x:
            err_msg = "{} is not in the range 0...{}".format(x, self.u-1)
            return False, err_msg

        # passed all checks
        return True, ""

