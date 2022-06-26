import re


def read(filename):
    contents = []
    with open(filename, 'r') as obj:
        lines = obj.readlines()
        for line in lines:
            contents.append(line.strip('\n').replace(" ", '').split(","))
    return contents


def solution(contents):
    favorites = {}
    for a, b, c, d in contents:
        if d not in favorites:
            favorites[d] = [[a, b, c]]
        favorites[d].append([a, b, c])

    for key, values in favorites.items():
        values = sorted(values, key=lambda x: int(x[2]))
        print('favorite:', key, ' name1:', values[-1][1], ' age1:', values[-1][-1], ' name2:', values[-2][1], ' age2:',
              values[-2][-1])


if __name__ == '__main__':

    # contents = read('data.txt')
    # solution(contents)

    with open('ut_test.txt', 'r') as f:
        data = f.readlines()
        temp = ''
        for line in data:
            line = line.strip("\n")
            temp += line
    res = []
    t = []
    for i in range(len(temp)):
        if temp[i] == '"':
            t.append(i)
    for i in range(0, len(t), 2):
        print(temp[t[i]:t[i + 1] + 1])

