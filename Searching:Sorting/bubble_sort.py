# sorts by swapping adjacent elements, making N^2 passes over array
def bubble_sort(array, n):
    for i in range(0, n):
        for j in range(0, n - i - 1): # last i elements in place already
            if array[j] > array[j + 1]:
                # swap adjacent elements
                array[j], array[j + 1] = array[j + 1], array[j]

def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    bubble_sort(array, n)
    print 'Sorted array {}'.format(array)

main()
