class Node:
    def __init__(self, val):
        self.val = val
        self.color = 'red'
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    @property
    def isLeftChild(self):
        if self.parent is not None:
            return self == self.parent.leftChild
        return False

    @property
    def isRightChild(self):
        if self.parent is not None:
            return self == self.parent.rightChild
        return False

    def flipColor(self):
        self.color = 'R' if self.color == 'B' else 'B'

    def set_color(self, color):
        self.color = color


class RBT:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.flipColor()
        self.root = self.NIL
        self.size = 0

    # def leftRotate(self, rotatedNode):
    #     replacementNode = rotatedNode.rightChild
    #     rotatedNode.rightChild = replacementNode.leftChild
    #     if replacementNode.leftChild is not None:
    #         replacementNode.leftChild.parent = rotatedNode
    #     replacementNode.parent = rotatedNode.parent
    #     replacementNode.leftChild = rotatedNode
    #     if rotatedNode.parent is None:
    #         self.root = replacementNode
    #     elif rotatedNode == rotatedNode.parent.rightChild:
    #         rotatedNode.parent.rightChild = replacementNode
    #     else:
    #         rotatedNode.parent.leftChild = replacementNode
    #     rotatedNode.parent = replacementNode
    #
    # def rightRotate(self, rotatedNode):
    #     replacementNode = rotatedNode.leftChild
    #     rotatedNode.leftChild = replacementNode.rightChild
    #     if rotatedNode.leftChild is not None:
    #         rotatedNode.leftChild.parent = rotatedNode
    #     replacementNode.parent = rotatedNode.parent
    #     replacementNode.rightChild = rotatedNode
    #     if rotatedNode.parent is None:
    #         self.root = replacementNode
    #     elif rotatedNode == rotatedNode.parent.rightChild:
    #         rotatedNode.parent.rightChild = replacementNode
    #     else:
    #         rotatedNode.parent.leftChild = replacementNode
    #     rotatedNode.parent = replacementNode
    #
    # def insert(self, val):
    #     newNode = Node(val)
    #     newNode.parent = None
    #     newNode.leftChild = self.NIL
    #     newNode.rightChild = self.NIL
    #
    #     # search for the right position for new node
    #     curr = self.root
    #     prev = self.NIL
    #     while curr is not self.NIL:
    #         prev = curr
    #         if val < curr.val:
    #             curr = curr.leftChild
    #         else:
    #             curr = curr.rightChild
    #
    #     # set new parameters for new node
    #     newNode.parent = prev
    #     if prev is self.NIL:
    #         self.root = newNode
    #     elif val < prev.val:
    #         prev.leftChild = newNode
    #     else:
    #         prev.rightChild = newNode
    #
    #     if newNode.parent.parent is None:
    #         return
    #     # balance red black tree
    #     self.insertFixup(newNode)
    #
    # def insertFixup(self, node):
    #     if node == self.root:
    #         node.flipColor()
    #         return
    #     if node.parent == self.root:
    #         return
    #     while node.parent.color == 'R':
    #         if node == self.root:
    #             break
    #         if node.parent.isLeftChild:
    #             uncle = node.parent.parent.rightChild
    #             if uncle is not None and uncle.color == 'R':
    #                 uncle.flipColor()
    #                 node.parent.flipColor()
    #                 node.parent.parent.flipColor()
    #                 node = node.parent.parent
    #             else:
    #                 if node.isRightChild:
    #                     node = node.parent
    #                     self.leftRotate(node)
    #                 node.parent.flipColor()
    #                 node.parent.parent.flipColor()
    #                 self.rightRotate(node.parent.parent)
    #                 #node = node.parent
    #
    #         else:
    #             uncle = node.parent.parent.leftChild
    #             if uncle is not None and uncle.color == 'R':
    #                 uncle.flipColor()
    #                 node.parent.flipColor()
    #                 node.parent.parent.flipColor()
    #                 node = node.parent.parent
    #             else:
    #                 if node.isLeftChild:
    #                     node = node.parent
    #                     self.rightRotate(node)
    #                 node.parent.flipColor()
    #                 node.parent.parent.flipColor()
    #                 self.leftRotate(node.parent.parent)
    #                 #node = node.parent
    #
    #     if self.root == 'R':
    #         self.root.flipColor()

    def search(self, key):
        curr = self.root
        while curr is not self.NIL:
            if curr.val.lower() == key.lower():
                return curr
            elif key < curr.val:
                curr = curr.leftChild
            else:
                curr = curr.rightChild
        return self.NIL

    def treeSize(self):
        return self.calcTreeSize(self.root)

    def calcTreeSize(self, root):
        return self.size

    def treeHeight(self):
        return self.calcTreeHeight(self.root)

    def calcTreeHeight(self, root):
        if root is self.NIL:
            return 0
        else:
            leftHeight = self.calcTreeHeight(root.leftChild)
            rightHeight = self.calcTreeHeight(root.rightChild)
            return max(leftHeight, rightHeight) + 1

    def left_rotate(self, x) -> None:
        y = x.right
        x.right = y.left
        if not y.left.is_null():
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x) -> None:
        y = x.left
        x.left = y.right
        if not y.right.is_null():
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key) -> None:
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        node.set_color("red")

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        self.size += 1

        if node.parent is None:
            node.set_color("black")
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, node) -> None:
        while node.parent == "red":
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.leftChild
                if u.is_red():
                    u.set_color("black")
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    node = node.parent.parent
                else:
                    if node == node.parent.leftChild:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.rightChild

                if u.color == "red":
                    u.set_color("black")
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    node = node.parent.parent
                else:
                    if node == node.parent.rightChild:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.set_color("black")
