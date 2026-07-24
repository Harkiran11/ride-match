class MinHeap:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, priority, item):
        self._data.append((priority, item))
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if not self._data:
            raise IndexError("pop from an empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def peek(self):
        if not self._data:
            raise IndexError("peek on an empty heap")
        return self._data[0]

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i][0] < self._data[parent][0]:
                self._data[i], self._data[parent] = self._data[parent], self._data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self._data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self._data[left][0] < self._data[smallest][0]:
                smallest = left
            if right < n and self._data[right][0] < self._data[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
            i = smallest


def heapify_max(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)


def heap_sort(arr):
    a = list(arr)
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify_max(a, n, i)

    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify_max(a, end, 0)

    return a
