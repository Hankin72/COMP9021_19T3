from collections import deque


def person_is_seller(name):
    '''
    这里判断 被 监察人 的姓名是否以"m"结尾
    '''
    return name[-1] == 'm'


def dfs_search(name):
    # 创建一个队列
    search_queue = deque()
    # 将邻居都加入到这个搜索队列中
    search_queue += graph[name]
    searched = []
    while search_queue:
        #  左边弹出，先进先出
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    # 实现图
    graph = {}
    # 一度关系
    graph['you'] = ['alice', 'bob', 'clarie']
    # 二度关系
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['clarie'] = ['jonny', 'thom']

    # 三度关系
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    dfs_search('you')
