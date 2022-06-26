# fibonacci
# 线性动态规划

"""从后往前的推导/从底向上"""
# 方程： f(n) =  f(n-1) + f(n-2)

"""从前向后的推导/从顶向下"""
# f(n-1) + f(n-2) = f(n)


#  1。 可以用递归来实现
#  O(2^n)
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


#  2。 一维数组来实现
def fib_array(n):
    array = [1,1]
    while len(array) < n:
        a, b = array[-1], array[-2]
        array.append(a+b)
    return array[-1]


def fib_array01(n):
    # 算法复杂度： O(n)
    # 空间复杂度； O(n)
    array = [1] * n
    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]
    return array[-1]


def final_fib(n):
    # 算法复杂度： O(n)
    # 空间复杂度； O(1)
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a+b
    return b



"""
 最长的自序列（数组里面最长的）
 [1,2,1,2,2,3,4,5,1,2,6,2]

"""
# [1,2,1,2,2,3,4,5,1,2,6,2]
# 求连续的最长的升序子序列

#        f[i-1] < f[i]  继续求解
#
# f[i] = f[i-1] = f[i]  继续求解
#
#        f[i-1] > f[i]  重新归0



"""
杨辉三角
            1
          1   1
        1   2    1    
      1    3    3   1
    1    4    6   4    1  
    
1                   row = 0
1   1               row = 1
1   2   1           row = 2
1   3   3   1       row = 3 
1   4   6   4    1    row = k
c(k,0), c(k,1), c(k,2),  ..... , c(k,k)
二项式的系数 
col1col2
"""
# 初始化的状态：
# f[0]  = [1]
# f[1] = [1,1]
# f[2] = [1]*(2+1)
# f[row] = [1] * (row+1)
#
#  动态规划dp的方程
#  f[row][column] = f[row-1][column-1] + f[row-1][column]
result = []
n = 10
# O(n^2)
for row in range(n):
    result.append([1]*(row+1))
    if row > 1:
        for column in range(1, row):
            result[row][column] = result[row - 1][column - 1] + result[row - 1][column]

for line in result:
    # O(n)
    print(" ".join((str(x) for x in line)))


"""
LCS  算法

求最长公共子序列
ABCABCD  （n）
ABFD      （m）

"""
# 1. 暴力解法：
str1 = 'ABCABCD'  # n , i
str2 = 'ABFD'   # m, j


# 2. 动态规划
# i = 0, j=0
# dp[i=0][j]
# dp[i][j=0]

# 0   dp[i=0][j]     dp[i][j=0]

#  dp[i][j] = dp[i-1, j-1] + 1                    str1[i]= str2[j]
#  dp[i][j] = MAX(dp[i-1, j], dp[i, j-1])         str1[i] != str2[j]
n = len(str1)
m = len(str2)
lcs=[]
for i in range(n+1):
    lcs.append([0]*(m+1))
print(lcs)
for i in range(n):
    for j in range(m):
        if str1[i] == str2[j]:
            lcs[i+1][j+1] = lcs[i][j]+1
        else:
            lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])

print()
for line in lcs:
    print(" ".join(str(x) for x in line))

# for index1 in range(len(str1)):
#     count = 0
#     for index2 in range(index1+1, len(str1)):
#         index3 = 0
#         while index3 < len(str2):

#         for index3 in range(len(str2)):


"""
背包问题：
1。 0-1背包问题
    一共有n件物品，第i（i从1开始）件物品的重量为w[i]，价值为v[i]
    在总重量不超过背包承载上限w的情况下，能够装入背包的最大价值是多少
    
    1）暴力解法：
        某一个重量要么放入，要么不放入
        复杂度 O(2^n)
    2) 动态编程
        
2。 完全背包问题
3。 多重背包问题

"""