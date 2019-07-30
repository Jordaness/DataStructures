# File of all common sorting functions

# Insertion Sort


def insertionSort(arr):
    '''Sorts the input interger array in place, taking worst case O(n**2) time.'''
    if arr is None:
        return None
    if len(arr) == 0 or len(arr) == 1:
        return arr

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

# Bubble Sort


def bubbleSort(arr):
    '''Sorts the input interger array in place, taking at worst case O(n**2) time.'''
    if arr is None:
        return None
    if len(arr) == 0 or len(arr) == 1:
        return arr

    for i in range(len(arr)):
        swap = False
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swap = True if swap == False else True
        if swap == False:
            break

# Selection Sort

def selectionSort(arr):
    '''sorts an integer array in place at worst case O(n**2) time.'''
    if arr is None:
        return None
    if len(arr) < 2:
        return arr

    # Finds the min in the array and moves it into the lowest index spot each iteration until the array is sorted
    for i in range(len(arr)):
        minIdx = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

# Merge Sort


def mergeSort(arr):
    '''Sorts the input interger array using O(n) space, but will do so in an average of O(n*lg(n)) time.'''
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)  # breaking up left half
        mergeSort(R)  # breaking up right half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort


def quickSort(arr, low: int = 0, high: int = None):
    if high == None:
        high = len(arr)-1

    if low < high:
        # move all nums less than pivot to the right of pivot and all nums less than pivot to the left fo pivot
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high) 


def partition(arr, low, high):
    if low >= high:
        return high

    pivot = arr[(low+high)//2]  # pivot on element
    i, j = low, high

    while i < j:
        while arr[i] < pivot:  # find first element greater than pivot element on left side
            i += 1
        while arr[j] > pivot:  # find first element less than pivot element on right side
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # return the pivot's position
    return j


testarr = [5, 18, 44, 20, 28, 6, 19, 33, 4, 23, 27, 55, 30, 25, 3]

quickSort(testarr)
print("Quick Sort")
print(testarr)
