"""
  Contains InsertionSort and MergeSort implementations.
  
  Also contains a timing comparison against TimSort using a common
  situation from practice, namely, adding a collection of items to
  an already sorted list.
"""
import timeit

def insertionSort (A):
    """ Apply INSERTION SORT on A."""
    for i in range(1,len(A)):
        pos = i-1
        val = A[i]
        while pos >= 0 and A[pos] > val:
            A[pos+1] = A[pos]
            pos -= 1
        A[pos+1] = val


def mergeSort (A):
    """
    Apply MERGE SORT on A using helper method. Uses auxiliary storage and
    leaves result in A.
    """
    msort (A, [None] * len(A), 0, len(A)-1)

def msort(A, aux, lo, hi):
    """Mergesort array in memory with given range."""
    if hi > lo:
        mid = (lo + hi) // 2

        msort(A, aux, lo, mid)
        msort(A, aux, mid+1, hi)
        
        merge(A, aux, lo, mid, hi)

def merge(A, aux, lo, mid, hi):
    """Merge A[lo:hi+1] and leave result in A using aux for storage."""
    for k in range(lo, hi+1):
        aux[k] = A[k]

    i = lo
    r = mid+1

    # merge is now ready. Merge from aux back into A
    for k in range(lo, hi+1):
        if i > mid:            
            A[k] = aux[r]
            r += 1
        elif r > hi:
            A[k] = aux[i]
            i += 1
        elif aux[r] < aux[i]:
            A[k] = aux[r]
            r += 1
        else:
            A[k] = aux[i]
            i += 1

def outputTiming():
    """
    Generate timing report for the three different approaches.
    Create a sorted list of N elements. Then create a new list
    that appends N/4 random integers to this sorted list of N
    elements. Time the result of sorting this new list on three
    different algorithms, for T=100 trials.
    """
    iSort = {}
    mSort = {}
    tSort = {}

    print (f'N\tInsert\tMerge\tTim')
    trials = []
    for i in range(4,16):
        n = 2 ** i
        trials.append(n)
        if n > 2048:
            iSort[n] = 0
        else:
            iSort[n] = timeit.timeit(stmt=f'insertionSort(oldSortedData + newData)', number=100,
                setup=f'import random\nfrom __main__ import insertionSort\noldSortedData = list(range(0, {n}))\nnewData=random.sample(range({n}//4), {n}//4)')
        mSort[n] = timeit.timeit(stmt=f'mergeSort(newData + oldSortedData)', number=100,
                setup=f'import random\nfrom __main__ import mergeSort\noldSortedData = list(range(0, {n}))\nnewData=random.sample(range({n}//4), {n}//4)')
        tSort[n] = timeit.timeit(stmt=f'sorted(oldSortedData + newData)', number=100,
                setup=f'import random\noldSortedData = list(range(0, {n}))\nnewData=random.sample(range({n}//4), {n}//4)')
        
    for t in trials:
        print (f'{t}\t{iSort[t]:.4f}\t{mSort[t]:.4f}\t{tSort[t]:.4f}')

if __name__ == '__main__':
    print ("Quick Validation of working MergeSort and InsertionSort.")
    x = list(range(16))
    x.reverse()
    mergeSort(x)
    print (x)

    x = list(range(16))
    x.reverse()
    insertionSort(x)
    print (x)
    
    outputTiming()
