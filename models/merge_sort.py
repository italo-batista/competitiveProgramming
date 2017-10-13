def merge_sort(array):

    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)

def merge(array, left, right):

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            array[k] = left[i]
                i = i + 1
        else:
            array[k]=right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1

array = map(int, raw_input().split())
merge_sort(array)
print array
