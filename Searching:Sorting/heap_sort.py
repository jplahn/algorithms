# create a Max Heap class to store the array and size
class MaxHeap:
    def __init__(self, array, size):
        self.size = size
        self.array = array

def max_heapify(maxheap, idx):
    largest = idx
    # calculating positions in the array. Left child of node is at 2*index + 1
    # right child of node is at 2*index + 2
    left = 2*idx + 1
    right = 2*idx + 2

    # check if left child exists and is greater than root
    if (left < maxheap.size and maxheap.array[left] > maxheap.array[largest]):
        largest = left

    # check if right child exists and is greater than root
    if (right < maxheap.size and maxheap.array[right] > maxheap.array[largest]):
        largest = right

    # change root, if needed
    if (largest != idx):
        maxheap.array[largest], maxheap.array[idx] = maxheap.array[idx], maxheap.array[largest]

        max_heapify(maxheap, largest)

def create_and_build_heap(array, size):
    max_heap = MaxHeap(array, size)

    # start from bottom-rightmost internal node and heapify all internal
    # nodes in bottom up way
    for i in range((max_heap.size - 2) / 2, -1):
        max_heapify(max_heap, i)

    return max_heap

def heap_sort(array, size):
    # build heap from input data
    max_heap = create_and_build_heap(array, size)

    # repeat following steps while heap size is greater than 1
    # the last element in max heap will be the minimum element
    while (max_heap.size > 1):
        # the largest item in heap is stored at the root
        # replace it with the last item of the heap followed by reducing
        # the size of the heap by 1
        max_heap.array[0], max_heap.array[max_heap.size - 1] = max_heap.array[max_heap.size - 1], max_heap.array[0]

        max_heap.size = max_heap.size - 1

        # heapify root of tree
        max_heapify(max_heap, 0)


def main():
    array = [1, 4, 2, 6, 3, 8, 9, 5]
    n = len(array)
    print 'Unsorted array {}'.format(array)
    heap_sort(array, n)
    print 'Sorted array {}'.format(array)

main()
