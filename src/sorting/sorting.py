# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # *Merges two sorted lists*
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    left = 0
    right = 0
    data = []

    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            data.append(arrA[left])
            left += 1
        else:
            data.append(arrB[right])
            right += 1
    while left < len(arrA):
        data.append(arrA[left])
        left += 1
    while right < len(arrB):
        data.append(arrB[right])
        right += 1

    return data

# The first thing you will notice is that we will have two pointers for each lists and they start at 0.
# We then designate an empty output list, in this case named res
# We loop as long as both pointers have not reached the end of their lists
# We compare the values corresponding at each pointer, starting off with the zero index
# If the value of the left index is smaller, we add it to our output. 
# Conversely, we do the same for the other side. We increase the pointer of the smaller side also by one each time
# We repeat this process until one lists finishes
# We then add the remaining values of the unfinished list into the end result

import math
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # *Sorts a list using recursion and helper merge function*
    if len(arr) < 2:
        return arr
    mid = int(math.floor(len(arr) / 2))
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    return merge(merge_sort(left), merge_sort(right))

    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
