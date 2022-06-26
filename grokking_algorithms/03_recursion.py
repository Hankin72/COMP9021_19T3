


"""
找钥匙
"""
def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


countdown(3)
print()


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))
