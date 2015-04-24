def interpolation_search(array, n, value):
    low = 0
    high = n - 1

    while (not(array[high] == array[low] or value < array[low] or array[high] < value)):
        mid = low + (value - array[low]) * ((high - low) / (array[high] - array[low]))

        if (array[mid] < value):
            low = mid + 1
        elif (value < array[mid]):
            high = mid - 1
        else:
            return mid


    if (key == array[low]):
        return low

    return -1

def main():
    array = [1, 2, 4, 8, 12, 13, 17]
    n = len(array)
    value = 13
    print 'Location of {} is {}'.format(value, interpolation_search(array, n, value))

main()
