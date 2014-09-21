"""
Properties
    O(1) extra space (see discussion)
    O(n lg(n)) time
    Not stable: (original ordering is lost during the heap creation, that comes first)
    Not really adaptive: (doesn't takes advantage of existing order in its input)
"""

"""
Heap sort is simple to implement, performs an O(n lg(n)) in-place sort,
but is not stable as any information about the ordering of the items
in the original sequence was lost during the heap creation stage, which came first.

Heapsort is not stable because operations on the heap can change the
relative order of equal items.


The first loop, the O(n) "heapify" phase, puts the array into heap order.
The second loop, the O(n lg(n)) "sortdown" phase, repeatedly extracts
the maximum and restores heap order.

The sink function is written recursively for clarity. Thus, as shown,
the code requires O(lg(n)) space for the recursive call stack. However,
the tail recursion in sink() is easily converted to iteration,
which yields the O(1) space bound.

Both phases are slightly adaptive, though not in any particularly
useful manner. In the nearly sorted case, the heapify phase destroys
the original order. In the reversed case, the heapify phase is as fast
as possible since the array starts in heap order, but then the sortdown
phase is typical. In the few unique keys case, there is some speedup
but not as much as in shell sort or 3-way quicksort.
"""

import sys
import math
import cProfile


def swap(aList, iIndex, jIndex):
    """
    Given a `list` and two indices, it swaps the contents.
    """
    aList[iIndex], aList[jIndex] = aList[jIndex], aList[iIndex]

def get_left_child(iIndex):
    """
    Given an index it returns it's left child's index.
    """
    return 2 * iIndex + 1

def get_right_child(iIndex):
    """
    Given an index it returns it's right child's index.
    """
    return 2 * iIndex + 2

def get_parent(iIndex):
    """
    Given an index, it returns the index of it's parent.
    """
    return int(math.floor((iIndex - 1) / 2))

def heapify(aList, iEnd, iIndex):
    """
    Given a list, and its size and an index, this function
    ensures all items are in descending order (children < parent)
    """
    iLeft = get_left_child(iIndex)
    iRight = get_right_child(iIndex)
    iLargest = iIndex

    if iLeft < iEnd and aList[iLeft] > aList[iLargest]:
        iLargest = iLeft
    if iRight < iEnd and aList[iRight] > aList[iLargest]:
        iLargest = iRight
    if iLargest != iIndex:
        swap(aList, iIndex, iLargest)
        heapify(aList, iEnd, iLargest)

def build_heap(aList):
    """
    Given a list, it builds a heap using the list.
    """
    iEnd = len(aList)
    iStart = iEnd / 2 - 1 #  Root of a tree is @ size/2-1
    for iIndex in range(iStart, -1, -1):
        heapify(aList, iEnd, iIndex)


def heap_sort(aList):
    """
    Given a unsorted list of integers other comparable types,
    it rearrange the integers in natural order in place in an
    ascending order.
    Example: Input:  [8,5,3,1,7,6,0,9,4,2,5]
             Output: [0,1,2,3,4,5,5,6,7,8,9]
    """
    iEnd = len(aList)
    build_heap(aList)
    for iIndex in range(iEnd-1, 0, -1):
        swap(aList, iIndex, 0)
        heapify(aList, iIndex, 0)
    return aList


def run_test():
    """
    Test function.
    """
    print "---------------------"
    aList = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    aList = heap_sort(aList)
    print "aList Sorted. Ascending = {}\n".format(aList)


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')
