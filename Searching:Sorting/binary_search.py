# Performs a binary search on a sorted array. Checks the midpoint to see if
# it is the desired value, otherwise it checks the left or right portion
# of array depending on comparison
def bin_search(array, left, right, value):
    if (right >= left):
        mid = left + (right - left) / 2;

        # found value
        if (array[mid] == value):
            return mid

        # search left half if mid value is greater than value
        if (array[mid] > value):
            return bin_search(array, left, mid - 1, value)

        # search right half of array
        return bin_search(array, mid + 1, right, value)

    return -1

def main():
    array = [1, 2, 4, 8, 12, 13, 17]
    n = len(array)
    value = 13
    print 'Location of {} is {}'.format(value, bin_search(array, 0, n - 1, value))

main()
