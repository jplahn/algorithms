# bucket sort will sort an array of numbers that can be split into individual
# buckets based on their first digit, and then we use selection sort to sort
# within each bucket
def bucket_sort(array, n):
    # create n empty buckets (i.e. list of length n with nested lists)
    buckets = list()
    for i in range(0, n):
        buckets.append(list())

    # place array elements in bucket
    for i in range(0, n):
        bucket_index = int(n * array[i])
        buckets[bucket_index].append(array[i])

    # sort individual buckets
    for i in range(0, n):
        buckets[i].sort()

    # concatenate all buckets into one list
    index = 0
    for i in range(0, n):
        for j in range(0, len(buckets[i])):
            array[index] = buckets[i][j]
            index = index + 1

def main():
    array = [.13, .44, .22, .61, .32, .34, .31, .81, .93, .52, .49, .51]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    bucket_sort(array, n)
    print 'Sorted array {}'.format(array)

main()
