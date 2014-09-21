"""
Properties
    Stable
    O(1) extra space
    O(n2) comparisons and swaps
    Adaptive: O(n) time when nearly sorted
    Very low overhead
"""

"""
Although it is one of the elementary sorting algorithms
with O(n2) worst-case time, insertion sort is the algorithm
of choice either when the data is nearly sorted
(because it is adaptive) or when the problem size is small
(because it has low overhead).

For these reasons, and because it is also stable,
insertion sort is often used as the recursive base case
(when the problem size is small) for higher overhead
divide-and-conquer sorting algorithms, such as
merge sort or quick sort.
"""

import sys
import cProfile


def insertion_sort_ascending(aList):
    """
    Given a unsorted list of integers other comparable types,
    it rearrange the integers in natural order in place in an
    ascending order.
    Example: Input:  [8,5,3,1,7,6,0,9,4,2,5]
             Output: [0,1,2,3,4,5,5,6,7,8,9]
    """
    for i in range(1, len(aList)):
        j = i
        atHand = aList[i]
        while j > 0 and atHand < aList[j - 1]:
            aList[j] = aList[j - 1]
            j -= 1
        aList[j] = atHand

    return aList


def insertion_sort_descending(dList):
    """
    Given a unsorted list of integers other comparable types,
    it rearrange the integers in natural order in place in an
    descending order.
    Example: Input:  [8,5,3,1,7,6,0,9,4,2,5]
             Output: [9,8,7,6,5,5,4,3,2,1,0]
    """
    n = len(dList)
    for i in range(n-2, -1, -1):
        j = i
        atHand = dList[i]
        while j < n-1 and atHand < dList[j + 1]:
            dList[j] = dList[j + 1]
            j += 1
        dList[j] = atHand

    return dList


def run_test_ascending():
    """
    Test function.
    """
    aList = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    aList = insertion_sort_ascending(aList)
    print "---------------------"
    print "aList Sorted. Ascending = {}\n".format(aList)


def run_test_escending():
    """
    Test function.
    """

    dList = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    dList = insertion_sort_descending(dList)
    print "---------------------"
    print "dList Sorted. Descending = {}\n".format(dList)

if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test_ascending()')
    cProfile.run('run_test_escending()')
