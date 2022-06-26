array = [1, 2, 3]

"""
# 1. 从前向后遍历
# 从0 开始index遍历,
# 三种遍历方式
"""

for index in range(len(array)):
    print(index, array[index])

for item in array:
    print(item)

for index, item in enumerate(array):
    print(index, item)

index = 0
s = 0
while index < len(array):
    print(index, array[index])
    s += array[index]
    index += 1

print(s)
print(sum(array))
print("*" * 50)

"""
 +++++e.g. 求所有的连续增长的子序列
"""

array_1 = [1, 2, 3, 1, 2, 1, 4]

# 索引的方式需要考虑越界：
# for i in range(len(array_1)):
#     if array_1[i + 1] > array_1[i]:
#

# 3个（连续增长的子序列）
# （1）两层for遍历 O(N^2)
res = []
for i in range(1, len(array_1)):
    if array_1[i - 1] >= array_1[i]:
        if res:
            res.append((res[-1][-1], i))
        else:
            res.append((0, i))
res.append((res[-1][-1], len(array_1)))
r = []
for first, last in res:
    r.append(array_1[first:last])
print(r)
print("*" * 50)

"""
当涉及到两辆比较的问题，
就可以使用first和second来处理
 O(N)复杂度
"""
result = list()
if array_1:
    # 首个元素已经处理
    first = array_1[0]
    result.append([first])
    # 然后。处理后面的元素
    for second in array_1[1:]:
        if second >= first:
            result[-1].append(second)
        else:
            result.append([second])
        first = second
print(result)

"""
=================================
2. 数组从后向前遍历
"""
# reversed(array_1)
# array_1[::-1]
array = [1, 2, 5, 10, 20, 50, 100]
number = 2517
# 25 个100，一个10，一个5，一个2
n = number
index = len(array) - 1
while index >= 0:
    money = array[index]
    a, n = divmod(n, money)
    #  a 取整，n取余数
    if a > 0:
        print(money, a)
    index -= 1

print("=====----------")
print(array, n)
while array:
    money = array.pop()
    a, n = divmod(n, money)
    #  a 取整，n取余数
    if a > 0:
        print(money, a)
print(array)

"""
3. 有序数组的插入
如果一个数组是有序的，
1，2，4，5，6
"""
import bisect


def insertOrderArray(order_array, num):
    '''
    数组插入一个元素
    1. 最好是O(1)
    2. 最坏是O(n)
    '''
    if order_array:
        # 判断是否比第0个小
        if num <= order_array[0]:
            order_array.insert(0, num)
        elif num >= order_array[-1]:
            # 判断是否比最后一个大
            order_array.append(num)
        else:
            """待插入数值属于中间位置"""
            """1. 遍历原数组"""
            for i in range(len(order_array) - 1):
                # 如果满足这样的条件
                if order_array[i] <= num <= order_array[i + 1]:
                    order_array.insert(i + 1, num)
                    break
            """2.使用二分查找"""


def binary_search_recursion(order_array, num, lo, hi):
    """
    使用递归的方式，
    # target = 2
    # index
    # 0。1。2。3。4。5。6。7。8
    # 1。2。3。4。5。6。7。9。10
    # lo = 0， hi = 8， mid = 4
    """
    if lo > hi:
        """终止条件"""
        return
    mid = lo + (hi - lo) // 2
    if order_array[mid] == num:
        print(f"{num} found")
    elif num > order_array[mid]:
        binary_search_recursion(order_array, num, mid + 1, hi)
    else:
        binary_search_recursion(order_array, num, lo, mid-1)


def binary_search_iteration(order_array, num, lo, hi):
    """
    使用迭代的方式
    """
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if order_array[mid] == num:
            print(f"{num} found")
            break
        elif num > order_array[mid]:
            lo = mid + 1
        else:
            hi = mid - 1


a = [1, 2, 4, 5, 6]
num = 2
insertOrderArray(a, num)
print(a)

"""
============================================================================================
"""
#
# --------------------------
#  town distance    fish kg
# 1. 20              300(鱼的量)
# 2. 40              400
# 3. 340             700
# 4. 360             600
# 最大重量415？？？
# 2 ->1 = (415-300+20) = 135
# 2:265, 3-->2 = (415-265+300) = 450

# 从第2个往第一个上面，运输fish，运输100kg（有损失），收到100-（40-20）= 80kg
# 从第3个往第一个上面，运输fish，运输400， 收到400-（340-20）=80kg

# 最好的情况：没有损失：(300+400+700+600)/4
# hi = (300+400+700+600)/4 = 500
# lo = min(300,400,700,600) = 300
# min = (hi+lo)//2， 中间值

#  lo = 300, hi = 500, mid = 400
# 判断mid = 400 是否都能让每个town都保留400的重量，
# 如果是：
#       low = mid+1= 401
# 如果不是：
#       hi = mid-1= 399


#    check 如果每个town都满足中间的fish的kg，
#       lo = mid+1
#    else:
#       hi = mid -1
#    答案是：最后一次满足所有的town的mid值

# 5             70
# 15            100
# 1200          20
# 最大重量是20？？

# 求所有town都有最大的fish重量

# 5     1000
# 105   100

# mid = 300
# lost = 100

# # 1000 - 300 -100
#  5    300
#  105  100+600
from copy import copy

towns = [20, 40, 340, 360]
fish = [300, 400, 700, 600]
hi = int(sum(fish) / len(towns))
lo = min(fish)

result = {}
#  二分查找O(logn)
while lo <= hi:
    mid_kg = lo + (hi - lo) // 2
    # check_fish = fish[::]
    check_fish = copy(fish)
    # 全部遍历，O(n)
    for i in range(len(check_fish) - 1):
        # 运输损失
        lost = towns[i + 1] - towns[i]
        if check_fish[i] > mid_kg + lost:
            check_fish[i + 1] = check_fish[i + 1] + ((check_fish[i] - mid_kg) - lost)
            check_fish[i] = mid_kg
        #  如果当前的town不满足，把下一个town的fish运输过来
        elif check_fish[i] < mid_kg:
            check_fish[i + 1] = check_fish[i + 1] - (mid_kg - check_fish[i] + lost)
            check_fish[i] = mid_kg

    if check_fish[-1] >= mid_kg:
        result[mid_kg] = True
        lo = mid_kg + 1
    else:
        result[mid_kg] = False
        hi = mid_kg - 1
print(sorted(result.items()))
print(max(key for key, value in result.items() if value))

"""
============================================================================================
"""

"""
============================================================================================
有序数组的合并
有序的交集交集

利用双指针

"""
array1 = [1, 2, 3, 4]
array2 = [1, 1, 2, 3]


# 双指针合并
# 求并集
def union_ordered(array1, array2):
    """求两个数组的并集"""
    first_index = 0
    second_index = 0
    array3 = []
    # O(m+n)
    # 空间复杂度 O(m+n)，如果考虑答案所在的空间
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



















