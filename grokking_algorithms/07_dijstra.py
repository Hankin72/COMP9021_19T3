# graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['fin'] = {}

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# the costs table
# start到其邻居以及其他所有点cost的初始化设置
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# the parents table， 表格父节点的初始化
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 记录处理过的节点vertices
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # 遍历costs table中所有的节点 ['a', 'b', 'fin']
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理节点中找到开销最小的节点
node = find_lowest_cost_node(costs)
# while循环，在所有节点都被处理之后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]  # b的邻居： {"a":3, "fin":5}， neighbors是一个散列表

    for n in neighbors.keys():  # 遍历当前节点所有的邻居 ， # b的邻居 a 和 fin
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 如果经过当前节点前往其邻居更近
            costs[n] = new_cost  # 就更新该邻居的开销
            parents[n] = node  # 同时将该邻居父节点设置为当前节点

    processed.append(node)
    node = find_lowest_cost_node(costs)  # 找出来接下来要处理的节点， 并循环


node = 'fin'
res = []
res.append('fin')
while parents[node] != 'start':
    res.append(parents[node])
    node = parents.pop(node)
res.append('start')
res.reverse()
print("-->".join(res))






