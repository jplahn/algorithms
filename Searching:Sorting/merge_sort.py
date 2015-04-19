# this function merges two halves of the array by iterating across each half,
# comparing elements
def merge(array, left, middle, right):
    left_size = middle - left + 1
    right_size = right - middle

    # create temporary arrays
    L = [0] * left_size
    R = [0] * right_size

    # copy data from array into temp arrays
    for i in range(0, left_size):
        L[i] = array[left_size + i]
    for i in range(0, right_size):
        R[i] = array[middle + 1 + i]

    # now step through each array, comparing elements, and merging them
    i, j, k = 0, 0, left
    while (i < left_size and j < right_size):
        if (L[i] <= R[j]):
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1
        k = k + 1

    # now copy remaining elements of L, if they exist
    while (i < left_size):
        array[k] = L[i]
        i = i + 1
        k = k + 1

    # now copy remaining elements of R, if they exist
    while (j < right_size):
        array[k] = R[j]
        j = j + 1
        k = k + 1


# recursively call mergesort to break down the array into smaller elements
# until they eventually are 1 element each, then merge them together
def merge_sort(array, left, right):
    if (left < right):
        middle = left + (right - left) / 2 # avoids overflow
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)

def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    merge_sort(array, 0, n - 1)
    print 'Sorted array {}'.format(array)

main()
