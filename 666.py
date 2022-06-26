from queue import Queue, LifoQueue, PriorityQueue


"""
queue
"""
# maxsize maxsize 是一个整数，用于设置可放入队列中的项目数的上限。
# 一旦达到此大小，插入将阻塞，直到队列项目被消耗。如果 maxsize 小于或等于零，则队列大小为无限。

q = Queue(maxsize= 5)

# 写入队列数据
q.put(0)
q.put(1)
q.put(2)
q.put(100)
q.put(100091709)
# 输出当前队列所有的数据
print(q.queue)
print(q.qsize())
print(q.empty())
print(q.full())

# 删除队列数据，并返回该数据
q.get()
# 输出当前剩余队列
print(q.queue)
print("*"*50)

"""
LifoQueue
"""
# LIFO即Last in First Out,后进先出。与栈stack的类似，使用也很简单,maxsize用法同上
lq = LifoQueue(maxsize=0)

# 队列写入数据
lq.put('a')
lq.put('b')
lq.put('c')

#输出队列
print(lq.queue)
print(lq.qsize())
print(lq.full())
print(lq.empty())

# 出队，删除队尾的数据
lq.get()
print(lq.queue)
print("*"*50)


"""
优先队列
：
PriorityQueue
"""

pq = PriorityQueue(maxsize=0)

# 写入队列， 设置优先级

pq.put((9, 'a'))
pq.put((7,'c'))
pq.put((1,'d'))

# 输出队列全部数据
print(pq.queue)

# 取出队列数据，可以看到，是按照优先级取的。
pq.get()
print(pq.queue)
pq.get()
print(pq.queue)
print("*"*50)



"""
双端队列：
deque
"""
from  collections import deque

dq = deque(['a','b'])

# 增加数据到队尾
dq.append('c')

# 增加数据到 队列左侧

dq.appendleft('d')

# 输出队列所有数据
print(dq)

# 弹出队尾的数据，并返回
print(dq.pop(), dq)

# 弹出队列左侧数据，并返回
print(dq.popleft(), dq)
