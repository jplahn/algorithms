# sorts an array by choosing an element after the sorted part of the array
# and inserting it into the sorted part of the array, shifting elements
# forward that come after the newly inserted element
def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        # move elements of array[0, i - 1] that are greater than key
        # one spot forward
        while (j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    insertion_sort(array, n)
    print 'Sorted array {}'.format(array)

main()
