# loop sum
def sum(arr):
    total = 0
    for x in arr:
        total += x

    return total


print(sum([1, 2, 3, 4]))


def recursive_sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])


print(recursive_sum([2, 4, 6]))


def count(list):
    if len(list) == 0:
        return 0
    return 1 + count(list[1:])


print(count([1, 1, 223]))


def max_element(list):
    if list == []:
        return None
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_element(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max_element([1, 2, 3]))


def quick_sort_1(array):
    '''
    最坏的情况也是 0(n^2)
    平均情况： O(nlogn)
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # 选择基准值
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]
        return quick_sort_1(less) + [pivot] + quick_sort_1(greater)


print(quick_sort_1([10, 5, 2, 3]))
