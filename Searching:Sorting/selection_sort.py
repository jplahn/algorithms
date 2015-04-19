# works by moving minimum element of unsorted portion of array into the
# sorted portion of the array [sorted, unsorted]
def selection_sort(array, n):
    # increment boundary of unsorted array
    for i in range(0, n):
        # find minimum element in unsorted array
        min_elem = i
        for j in range(i+1, n):
            if (array[j] < array[min_elem]):
                min_elem = j
        # swap two elements
        array[min_elem], array[i] = array[i], array[min_elem]

def main():
    array = [3, 2, 6, 8, 1, 4, 5]
    n = len(array)
    print 'Unsorted array: {}'.format(array)
    selection_sort(array, n)
    print 'Sorted array: {}'.format(array)

main()
