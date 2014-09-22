"""
Properties
    Not stable
    O(lg(n)) extra space
    O(n^2) time worst case
        - typically O(n * lg(n)) time
    Not adaptive
    Great for large inputs
    Good cache performance (sequential check)
    Good parallel performance
"""

"""
When carefully implemented, quick sort is robust and has low overhead.
When a stable sort is not needed, quick sort is an excellent general-purpose
sort -- although the 3-way partitioning version should always be used instead.

The 2-way partitioning code shown above is written for clarity rather than
optimal performance; it exhibits poor locality, and, critically, exhibits
O(n2) time when there are few unique keys.

With both sub-sorts performed recursively, quick sort requires O(n) extra
space for the recursion stack in the worst case when recursion is not balanced.
This is exceedingly unlikely to occur, but it can be avoided by sorting the smaller
sub-array recursively first; the second sub-array sort is a tail recursive call,
which may be done with iteration instead. With this optimization, the algorithm
uses O(lg(n)) extra space in the worst case.
"""

import sys
import math
import cProfile

def quick_sort(aList):
    """
    Given a unsorted list of integers other comparable types,
    it rearrange them in natural order in an ascending order.
    Example: Input:  [8,5,3,1,7,6,0,9,4,2,5]
             Output: [0,1,2,3,4,5,5,6,7,8,9]
    """
    left = []
    middle = []
    right = []

    if not len(aList):
        return aList

    pivot = aList[0]
    for x in aList:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

def run_test():
    """
    Test function.
    """
    print "---------------------"
    aList = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    aList = quick_sort(aList)
    print "aList Sorted. Ascending = {}\n".format(aList)

if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
