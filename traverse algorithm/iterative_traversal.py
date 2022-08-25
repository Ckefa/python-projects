class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.inod = []
        self.pre = []
        self.post = []

    def in_order(self):
        tree = self.root
        mystack = []

        while True:
            if tree:
                mystack.append(tree)
                tree = tree.left
            elif mystack:
                curr = mystack.pop()
                self.inod.append(curr.data)
                if curr.right is not None:
                    tree = curr.right
            else:
                break

        print([i.data for i in mystack])

    def pre_order(self):
        tree = self.root

    def post_order(self):
        tree = self.root

        print(self.inod)
        print(self.pre)
        print(self.post)


mytree = Tree(7)
mt = mytree.root
mt.left = Node(5)
mt.left.left = Node(2)
mt.left.left.left = Node(3)
mt.left.left.right = Node(1)
mt.left.right = Node(4)

mt.right = Node(8)
mt.right.right = Node(6)
mt.right.right.right = Node(9)
mt.right.right.left = Node(10)
mt.right.left = Node(11)

mytree.in_order()
mytree.pre_order()
mytree.post_order()
