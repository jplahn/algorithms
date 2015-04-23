# we select the last element as the pivot and place it at the correct position
# in the sorted array. It then places all elements smaller than the pivot
# to the left of the pivot and larger elements to the right of the pivot
def partition(array, left, end_index):
    x = array[end_index] # pivot element
    i = left - 1 # index of smaller element

    for j in range(left, end_index):
        # if current element is smaller than or equal to pivot
        if (array[j] <= x):
            i = i + 1
            array[i], array[j] = array[j], array[i]
        print array

    array[i + 1], array[end_index] = array[end_index], array[i + 1]
    return i + 1

def quick_sort(array, left, end_index):
    if (left < end_index):
        partition_index = partition(array, left, end_index)
        quick_sort(array, left, partition_index - 1)
        quick_sort(array, partition_index + 1, end_index)

def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    quick_sort(array, 0, n - 1)
    print 'Sorted array {}'.format(array)

main()
