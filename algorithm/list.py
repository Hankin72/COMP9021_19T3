"""
链表的总结：

"""


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # 第一个
        self.header = None
        # 最后一个
        self.last = None
        # 个数
        self.total = 0

    def insert(self, data):
        """链表：插入insert到末尾"""
        if self.header:
            self.last.next = LinkedNode(data)
            self.last = self.last.next
        else:
            self.header = self.last = LinkedNode(data)
        self.total += 1

    def __repr__(self):
        """打印，转化"""
        result = []
        temp_node = self.header
        while temp_node:
            result.append(str(temp_node.data))
            # print(temp_node.data)
            temp_node = temp_node.next
        return "-->".join(result)

    def __len__(self):
        return self.total

    def show(self, node):
        result = []
        temp_node = node
        while temp_node:
            result.append(str(temp_node.data))
            temp_node = temp_node.next
        print("-->".join(result))

    # 1-->      2-->        3-->        4-->        5-->        6-->        None
    # first
    #           second
    #           first                   second
    #                       first                               second
    # 将一个链表从中间分开

    def split_linked_list(self):
        # 快慢指针
        if self.header:
            first = self.header
            second = first.next

            while second and second.next:
                first = first.next
                second = second.next.next

            first_part = self.header
            second_part = first.next
            first.next = None
            self.show(first_part)
            self.show(second_part)
            first.next = second_part

    def reversed_list(self):
        """反转链表"""
        # None-->       1-->        2-->        3-->        4-->        5-->        None
        # first
        #               second
        #                           temp
        #               first
        #                           second
        #                                       temp
        #                           first
        #                                       second
        #                                                   temp
        #                                       first       second      temp
        #                                                   first       second      temp
        #                                                               first       second
        # 5-->4-->3-->2-->1--> None

        first = None
        second = self.header
        while second:
            # 记录下一个节点
            # temp = 2-->3-->4-->5
            temp = second.next
            # 交换first和second的位置
            second.next = first

            # 继续向后
            first = second
            second = temp
        self.header = first

    def union(self, other):
        """和另外一个链表进行合并"""
        new_list = LinkedList()
        first = self.header
        second = other.header

        while first and second:
            if first.data < second.data:
                new_list.insert(first.data)
                first = first.next
            elif first.data > second.data:
                new_list.insert(second.data)
                second = second.next
            else:
                new_list.insert(first.data)
                first = first.next
                new_list.insert(second.data)
                second = second.next
        while first:
            new_list.insert(first.data)
            first = first.next
        while second:
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
            #  比较第一个
            if data < self.header.data:
                new_node = LinkedNode(data)
                new_node.next = self.header
                self.header = new_node

            # 比较最后一个
            elif data > self.last.data:
                new_node = LinkedNode(data)
                self.last.next = new_node
                self.last = self.last.next

            # 中间位置
            else:
                first = self.header
                second = first.next
                while second:
                    if first.data <= data <= second.data:
                        new_node = LinkedNode(data)
                        #   插在first之后
                        new_node.next = second
                        # new_node.next = first.next
                        first.next = new_node
                        break
                    first = first.next
                    second = second.next



if __name__ == "__main__":
    # first = LinkedNode(1)
    # second = LinkedNode(2)
    # # first --> second
    # # 1 --> 2
    # first.next = second
    #
    # """如何遍历一个单链表"""
    # temp = first
    # while temp:
    #     print(temp.data)
    #     temp = temp.next

    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5)
    list1.insert(6)
    list1.insert(7)
    # list1.insert(8)

    print(list1)
    print(f"Total linked nodes: {len(list1)}.")
    print()
    list1.split_linked_list()
    print()

    print(list1)

    list2 = LinkedList()
    list2.insert(2)
    list2.insert(5)
    list2.insert(13)

    list1.union(list2)
    list1.intersection(list2)

    print(list1)
    list1.insert_order_list(2.5)
    print(list1)

    # print()
    # print("reverse linked list: ")
    # list1.reversed_list()
    # list2.reversed_list()
    # print(list1)
    # print(list2)
























