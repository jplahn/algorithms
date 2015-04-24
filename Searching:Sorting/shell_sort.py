def shell_sort(array, n):
    # start with large gap to swap elements, then reduce it
    gap = n / 2
    while gap > 0:
        # do gapped insertion sort for current gap size
        # the first gap elements array[0..gap - 1] are already in gap order
        # keep adding one more element until entire array is gap sorted
        for i in range(gap, n):
            # add array[i] to the elements that have been gap sorted
            # save array[i] in temp array and leave space at index i
            temp = array[i]

            # shift earlier gap sorted elements until correct location
            # for temp is found
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j = j - gap

            # put temp in correct location
            array[j] = temp
        gap = gap / 2

def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    shell_sort(array, n)
    print 'Sorted array {}'.format(array)

main()
