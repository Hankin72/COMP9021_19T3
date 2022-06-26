import copy

# -----------
print()
print()
x = [1, 2, 3, 4, ['x', 'y', [1, 2, 3]]]  # 原始对象

y = x  # #赋值，传对象的引用
m = copy.copy(x)  # 对象拷贝，浅拷贝
n = copy.deepcopy(x)  # 对象拷贝，深拷贝

x.append(5)  # 修改对象a
x[4].append('m')  # 修改对象a中的['a', 'b']数组对象
x[4][-2].append(10000)

print('x = ', x)
print('y = ', y)
print('m = ', m)
print('n = ', n)

print()






















