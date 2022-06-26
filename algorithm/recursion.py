def recursion(n):
    """
    # fibonacci
    # 递归的形式：
    #  f(n) =  f(n-1) + f(n-2)
    """
    # 1. base case/stop case
    if n == 1 or n == 2:
        return 1
    # 2. recursive case
    return recursion(n - 1) + recursion(n - 2)


"""
DFS: 深度优先搜索
 
BFS: 广度优先搜索 
"""
import numpy as np

dim = 4
grid = [[1, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 1, 0],
        ]

print(grid)


def dfs_recursion(cur_x, cur_y):
    print(cur_x, cur_y)
    grid[cur_y][cur_x] = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    valid_points = []
    for dir_x, dir_y in directions:
        next_x, next_y = cur_x + dir_x, cur_y + dir_y
        if 0 <= next_x < dim and 0 <= next_y < dim and grid[next_y][next_x] == 1:
            valid_points.append((next_x, next_y))

    # stop case / base case
    if len(valid_points) == 0:
        return
    # recursive case
    else:
        for next_x, next_y in valid_points:
            dfs_recursion(next_x, next_y)


def dfs_recursion01(cur_x, cur_y):
    print(cur_x, cur_y)
    # 访问过的，不再访问, 改变原图，设置为0
    grid[cur_y][cur_x] = 0

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    valid_points = []
    for dir_x, dir_y in directions:
        next_x, next_y = cur_x + dir_x, cur_y + dir_y
        if 0 <= next_x < dim and 0 <= next_y < dim and grid[next_y][next_x] == 1:
            dfs_recursion01(next_x, next_y)
            valid_points.append((next_x, next_y))


def dfs_recursion_visited(cur_x, cur_y, visited):
    # 访问过的，不再访问
    visited.append((cur_x, cur_y))
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dir_x, dir_y in directions:
        next_x, next_y = cur_x + dir_x, cur_y + dir_y
        if 0 <= next_x < dim and 0 <= next_y < dim \
                and grid[next_y][next_x] == 1 \
                and (next_x, next_y) not in visited:
            dfs_recursion_visited(next_x, next_y, visited)


"""
------------------------------------------------
"""


def number_of_component(cur_x, cur_y, component_id, ):
    # 访问过的，不再访问
    grid[cur_y][cur_x] = component_id
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dir_x, dir_y in directions:
        next_x, next_y = cur_x + dir_x, cur_y + dir_y
        if 0 <= next_x < dim and 0 <= next_y < dim \
                and grid[next_y][next_x] == 1:
            number_of_component(next_x, next_y, component_id)


def check_components():
    component_id = 2
    for y in range(dim):
        for x in range(dim):
            if grid[y][x] == 1:
                number_of_component(x, y, component_id)
                component_id += 1
    print(" number of components: ", component_id - 2)


"""
------------------------------------------------
"""

# dfs_recursion(0, 0)
# dfs_recursion01(0,0)
print(grid)
all_visited = []
components = []
for y in range(dim):
    for x in range(dim):
        if grid[y][x] == 1 and (x, y) not in all_visited:
            cur_visited = []
            dfs_recursion_visited(x, y, cur_visited)
            print('start points: ', cur_visited)
            all_visited.extend(cur_visited)
            components.append(cur_visited)

print(components)
print(len(components))

print("----------------------------")


# check_components()


def iteration():
    """使用非递归的方式实现dfs"""
    all_visited = []
    for y in range(dim):
        for x in range(dim):
            if grid[y][x] == 1 and (x, y) not in all_visited:
                stack = [(x, y)]
                while stack:
                    cur_x, cur_y = stack.pop()
                    all_visited.append((cur_x, cur_y))
                    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                    for dir_x, dir_y in directions:
                        next_x, next_y = cur_x + dir_x, cur_y + dir_y
                        if 0 <= next_x < dim and 0 <= next_y < dim \
                                and grid[next_y][next_x] == 1:
                            stack.append((next_x, next_y))


# bfs
# queue

def bfs_iteration():
    """
    queue 实现 bfs
    """
    visited = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for y in range(dim):
        for x in range(dim):
            if grid[y][x] == 1 and (x, y) not in visited:
                queue = [(x, y)]
                visited.append((x, y))
                while queue:
                    # queue从左边弹出
                    cur_x, cur_y = queue.pop(0)
                    for dir_x, dir_y in directions:
                        next_x, next_y = cur_x + dir_x, cur_y + dir_y
                        if 0 <= next_x < dim and 0 <= next_y < dim \
                                and grid[next_y][next_x] == 1 and (next_x, next_y) not in visited:
                            visited.append((next_x, next_y))
                            queue.append((next_x, next_y))
                print(visited)
                return

bfs_iteration()


