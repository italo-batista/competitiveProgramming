def count(array):

    if len(array) == 1:
        return 0

    else:

        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        x = count(left)
        y = count(right)
        z = count_split(left, right)
        return z + x + y

def count_split(left, right):

    i = 0
    j = 0
    k = 0
    z = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            z = z + len(left) - i
            j = j + 1

        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        z = z + len(left) - i
        j = j + 1
        k = k + 1

    return z

array = map(int, raw_input().split())
print count(array)
