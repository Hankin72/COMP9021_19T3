def bubbleSort(array):
    n = len(array)
    # 遍历所有数组元素
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))


def bubbleSort_2(array):
    n = len(array)

    for i in range(n):
        j = n - 2
        while j >= i:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
    return array


test = [1, 5, 9, 3, 2, 4, 8, 6, 7]
print(bubbleSort_2(test))

