# 二叉树的特点：
# 1.左右两个子节点
# 2. height 最长的从root到leaf的edge的个数？
# 3. 左节点的值<root<右节点的值
# 4。前，中，后序的打印
# 5。level打印


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertTree(tree, data):
    if tree is None:
        return Tree(data)
    elif data < tree.data:
        tree.left = insertTree(tree.left, data)
    elif data > tree.data:
        tree.right = insertTree(tree.right, data)
    return tree


#  前、中、后序
def preOrder(tree):
    """tree的前序输出
    根结点 --> 左子树 --> 右子树
          1
      2      3
    4  5       6
      7 8
    前序遍历：1 2 4 5 7 8 3 6
    """
    if tree:
        print(tree.data)
        preOrder(tree.left)
        preOrder(tree.right)


def inOrder(tree):
    """tree 中序打印输出
    中序遍历：左子树---> 根结点 ---> 右子树
          1
      2      3
    4  5       6
      7 8

    中序遍历: 4 2 7 5 8 1 3 6
    """
    if tree:
        inOrder(tree.left)
        print(tree.data)
        inOrder(tree.right)


def postOrder(tree):
    """tree后序序打印输出
    后序遍历：左子树 ---> 右子树 ---> 根结点
         1
      2      3
    4  5       6
      7 8

    后序遍历输出： 4 7 8 5 2 6 3 1
    """
    if tree:
        postOrder(tree.left)
        postOrder(tree.right)
        print(tree.data)


def get_kth_item(tree, current, k):
    '''获取第 k 个 元素的值'''
    if tree:
        get_kth_item(tree.left, current, k)
        # global current
        current[0] += 1
        if current[0] == k:
            print(tree.data)
        get_kth_item(tree.right, current, k)


#      5
#   3     6
# 2

def count_height(tree):
    if tree:
        left = count_height(tree.left)
        right = count_height(tree.right)
        if left > right:
            return left + 1
        else:
            return right + 1
    else:
        return -1


def count_leaf(tree):
    """        300
          100       400
      200   250  310    500
      leaf 结点个数计算
    """
    # //base case:
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    # // recursion case:
    left = count_leaf(tree.left)
    right = count_leaf(tree.right)
    return left + right


def count_odd(tree):
    # // base case:
    if tree is None:
        return 0
    left = count_odd(tree.left)
    right = count_odd(tree.right)

    if tree.data % 2 == 1:
        return left + right + 1
    else:
        return left + right

    # if tree:
    #     left = count_odd(tree.left)
    #     right = count_odd(tree.right)
    #
    #     if tree.data % 2 == 1:
    #         return left + right + 1
    #     else:
    #         return left + right
    # else:
    #     return 0


#  tree1                tree2
#    5                    5
#  2                   3

def same_tree(first_tree, second_tree):
    """check same tree"""
    if first_tree is None and second_tree is None:
        return True
    elif first_tree is None or second_tree is None:
        return False
    elif first_tree.data != second_tree.data:
        return False
    else:
        return same_tree(first_tree.left, second_tree.left) \
               and same_tree(first_tree.right, second_tree.right)


def fibonacci(n):
    """
    # 递归：包含两部分
    # // 1. stop case/base case
    # // 2. recursion case
    """
    if n == 1 or n == 2:
        return 1
    # recursion case
    return fibonacci(n - 1) + fibonacci(n - 2)


def height(tree):
    # stop case
    if tree is None:
        return -1
    # recursion case
    left = height(tree.left)
    right = height(tree.right)
    if left >= right:
        return left + 1
    else:
        return right + 1


def level_sum(tree, result, level):
    if tree:
        result[level] += tree.data
        #  继续往下走
        level_sum(tree.left, result, level + 1)
        level_sum(tree.right, result, level + 1)


def copy_tree(first_tree):
    if first_tree:
        second_tree = Tree(first_tree.data)

        # 继续查找
        second_tree.left = copy_tree(first_tree.left)
        second_tree.right = copy_tree(first_tree.right)

    else:
        second_tree = None

    return second_tree


if __name__ == '__main__':
    print()
    print('--' * 30)
    #       301
    #  105        503
    # None  200  400  None
    tree1 = Tree(5)
    insertTree(tree1, 3)
    insertTree(tree1, 10)
    insertTree(tree1, 1)
    insertTree(tree1, 4)
    insertTree(tree1, 8)
    insertTree(tree1, 0)
    insertTree(tree1, 2)
    inOrder(tree1)

    print()
    # get_kth_item(tree1, [0], 3)
    # print(count_height(tree1))
    print("asaaaaa")
    # print(count_leaf(tree1))
    #
    # print(count_odd(tree1))

    # tree2 = Tree(301)
    # insertTree(tree2, 503)
    # insertTree(tree2, 105)
    # insertTree(tree2, 200)
    # insertTree(tree2, 400)
    # print(same_tree(tree1, tree2))

    # from collections import defaultdict
    #
    # result = defaultdict(int)
    # level_sum(tree1, result, 0)
    # for level in sorted(result.keys()):
    #     print(level, result[level])

    tree2 = copy_tree(tree1)
    inOrder(tree2)
