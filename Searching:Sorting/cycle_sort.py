# cycle sort is the write optimal sorting algorithm
# it only writes a value in the array if it is at the correct position, otherwise
# it doesn't move an alement. it operates using cycles whereby it rotates
# them around the elements that it writes
def cycle_sort(array, n):
    for cycle_start in range(0, n - 1):
        value = array[cycle_start]

        # find where to put the value
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if array[i] < value:
                pos = pos + 1

        # if the value is already in right place, there is no cycle
        if pos == cycle_start:
            continue

        # put value in current spot, or after any duplicates
        while value == array[pos]:
            pos = pos + 1
        array[pos], value = value, array[pos]

        # rotate the rest of the cycle
        while pos != cycle_start:
            # find where to put value
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if array[i] < value:
                    pos = pos + 1

            # put value in current spot, or after duplicates
            while value == array[pos]:
                pos = pos + 1
            array[pos], value = value, array[pos]


def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    cycle_sort(array, n)
    print 'Sorted array {}'.format(array)

main()
