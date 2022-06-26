class LinkedNode:
    """
    单个节点
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # 第一个
        self.header = None
        # 最后一个
        self.last = None
        self.total = 0

    def insert(self, data):
        """
        链表， 插入insert到末尾
        """
        if self.header:
            self.last.next = LinkedNode(data)
            self.last = self.last.next
        else:
            self.header = self.last = LinkedNode(data)

        self.total += 1

    def __repr__(self):
        """
        打印，转化
        :return:
        """
        result = []
        temp_node = self.header
        while temp_node:
            result.append(str(temp_node.data))
            temp_node = temp_node.next
        return '-->'.join(result)

    def __len__(self):
        return self.total

    def show(self, node):
        result = []
        temp = node
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print("-->".join(result))

    def split_linked_list(self):
        # 快慢指针
        if self.header:
            first = self.header
            second = first.next

            while second and second.next:
                first = first.next
                second = second.next.next

            first_part = self.header
            #  first 的next 打断
            first.next = None
            second_part = first.next

            self.show(first_part)
            self.show(second_part)
            first.next = second_part

    def reversed_list(self):
        """
        反转链表
        :return:
        """
        first = None
        second = self.header
        while second:
            # 记录下一个节点
            # temp = 2->3->4->5
            temp = second.next
            # 交换 first 和  second
            second.next = first
            first = second
            second = temp
        self.header = first


    def union(self, other):
        """

        和另外一个链表进行合并
        :param other:
        :return:
        """
        new_list = LinkedList()
        first = self.header
        second = other.header

        while first and second:
            if first.data < second.data:
                new_list.insert(first.data)
                first =first.next
            elif first.data < second.data:
                new_list.insert(second.data)
                second = second.next
            else:
                new_list.insert(first.data)
                first = first.next
                new_list.insert(second.data)
                second = second.next
        print(new_list)

    def intersection(self, other):
        """和另外一个链表进行求交集的操作"""
        new_list = LinkedList()
        first = self.header
        second = other.header
        while first and second:
            if first.data < second.data:
                first = first.next
            elif first.data > second.data:
                second = second.next
            else:
                new_list.insert(first.data)
                first = first.next
                second = second.next
        print(new_list)

    def insert_order_list(self, data):
        if not self.header:
            self.insert(data)
        else:
            # 比较第一个
            if data < self.header.data:
                new_node =LinkedNode(data)
                new_node.next =self.header
                self.header = new_node

            elif data > self.last.data:
                new_node = LinkedNode(data)
                self.last.next = new_node
                self.last = self.last.next
            else:
                first = self.header
                second = first.next

                while second:
                    if first.data <= data <= second.data:
                        new_node = LinkedNode(data)
                        new_node.next = second
                        first.next = new_node
                        break
                    first = first.next
                    second = second.next



if __name__ == '__main__':
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5)
    list1.insert(6)
    list1.insert(7)

    print(list1)
    print(f'total linked nodes: {len(list1)}')
    print()
    list1.split_linked_list()
    print()

    print(list1)
    
