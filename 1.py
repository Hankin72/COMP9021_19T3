"""
3. 有序数组的插入
如果一个数组是有序的，
1，2，4，5，6
"""
import bisect


def insertOrderArray(order_array, num):
    """
    数组插入一个元素
    1。 最好的是 o(1)
    2. 最坏的是O(N)
    :param order_arrary:
    :param num:
    :return:
    """
    if order_array:
        # 判断是否比第0个小
        if num <= order_array[0]:
            order_array.insert(0, num)
        elif num >= order_array[-1]:
            order_array.append(num)
        else:
            """
            待插入的数值属于中间位置
            1。 方法一： 遍历愿数组
            2。二分查找
            """
            # for i in range(len(order_array) - 1):
            #     if order_array[i] <= num <= order_array[i + 1]:
            #         order_array.insert(i + 1, num)
            #         break

            for i in range(1, len(order_array)):
                if order_array[i - 1] <= num <= order_array[i]:
                    order_array.insert(i, num)
                    break


def binary_search_recusion(order_array, num, lo, hi):
    """
    使用递归的方式

    :param order_array:
    :param num:
    :param lo:
    :param hi:
    :return:
    """
    if lo > hi:
        # 终止条件
        return
    mid = (lo + hi) // 2
    if order_array[mid] == num:
        print(f'{num} found')
    elif num > order_array[mid]:
        binary_search_recusion(order_array, num, mid + 1, hi)
    else:
        binary_search_recusion(order_array, num, lo, mid - 1)


a = [1, 2, 4, 5, 6]
num = 2
insertOrderArray(a, num)
print(a)

"""
============================================================================================
有序数组的合并
有序的交集交集

利用双指针

"""
array1 = [1, 2, 3, 4]
array2 = [1, 1, 2, 3]


def union_ordered(array1, array2):
    """
    求两个数组的并集
    :param array1:
    :param array2:
    :return:
    """
    first_index = 0
    second_index = 0
    array3 = []

    while first_index < len(array1) and second_index < len(array2):
        if array1[first_index] < array2[second_index]:
            array3.append(array1[first_index])
            first_index += 1
        elif array1[first_index] > array2[second_index]:
            array3.append(array2[second_index])
            second_index += 1
        else:
            array3.append(array1[first_index])
            first_index += 1
            array3.append(array2[second_index])

            second_index += 1

    while first_index < len(array1):
        array3.append(array1[first_index])
        first_index += 1
    while second_index < len(array2):
        array3.append(array2[second_index])
        second_index += 1
    return array3


print(list(sorted(array1 + array2)))
print(union_ordered(array1, array2))


def intersection_ordered(array1, array2):
    """求两组的交集"""
    first_index = 0
    second_index = 0
    array3 = []
    # O(m+n)
    # 空间复杂度 O(m+n)，如果考虑答案所在的空间

    while first_index < len(array1) and second_index < len(array2):
        if array1[first_index] < array2[second_index]:
            first_index += 1
        elif array1[first_index] > array2[second_index]:
            second_index += 1
        else:
            array3.append(array1[first_index])
            first_index += 1
            second_index += 1

    return array3


print(array1, array2)
print(intersection_ordered(array1, array2))
