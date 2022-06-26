from math import sqrt
import sys
import os
from timeit import timeit
from itertools import compress

## 二进制 bin() 返回十进制 int('xx', 2)
## 十六进制hex()  ---int('f',16)
## 八进制 oct() --- int('', 8)
## a.isalnum()  判断是字母或者数字


## 任意进制
a = 100
result = ''
while a > 0:
    a, b = divmod(a, 3)
    result += str(b)
print(int(result))


## 返还十进制 int('', base)

## 获取给定数字所有的除数，***重点

def get_all_divisor(n):
    if n == 1:
        return {1}
    result = set()
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result


## 求prime
####利用byte求质数
def get_primes_3(n):
    # return a list of primes < n , for n >2
    if n <= 2:
        return []
    if n < 3:
        return [2]

    sieve = bytearray([True]) * (n // 2)
    # print(sieve)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


print(get_primes_3(10))


##判断某一个值是不是质数

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return False
    # only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n) + 1), 2))













