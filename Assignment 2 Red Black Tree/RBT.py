class Node:
    def __init__(self, val):
        self.val = val
        self.color = 'R'
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def isLeftChild(self):
        return self == self.parent.leftChild

    def isRightChild(self):
        return self == self.parent.rightChild

    def flipColor(self):
        self.color = 'R' if self.color == 'B' else 'B'


class RBT:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.flipColor()
        self.root = self.NIL

    def leftRotate(self, rotatedNode):
        replacementNode = rotatedNode.rightChild
        rotatedNode.rightChild = replacementNode.leftChild
        if replacementNode.leftChild is not None:
            replacementNode.leftChild.parent = rotatedNode
        replacementNode.parent = rotatedNode.parent
        if rotatedNode.parent is None:
            self.root = replacementNode
        elif rotatedNode == rotatedNode.parent.rightChild:
            rotatedNode.parent.rightChild = replacementNode
        else:
            rotatedNode.parent.leftChild = replacementNode
        replacementNode.leftChild = rotatedNode
        rotatedNode.parent = replacementNode

    def rightRotate(self, rotatedNode):
        replacementNode = rotatedNode.leftChild
        rotatedNode.leftChild = replacementNode.rightChild
        if replacementNode.rightChild is not None:
            replacementNode.rightChild.parent = rotatedNode
        replacementNode.parent = rotatedNode.parent
        if rotatedNode.parent is None:
            self.root = replacementNode
        elif rotatedNode == rotatedNode.parent.rightChild:
            rotatedNode.parent.rightChild = replacementNode
        else:
            rotatedNode.parent.leftChild = replacementNode
        replacementNode.rightChild = rotatedNode
        rotatedNode.parent = replacementNode

    def insert(self, val):

        # initialize new node
        newNode = Node(val)
        newNode.parent = None
        newNode.leftChild = self.NIL
        newNode.rightChild = self.NIL

        # search for the right position for new node
        curr = self.root
        prev = None
        while curr is not self.NIL:
            prev = curr
            if val < curr.val:
                curr = curr.leftChild
            else:
                curr = curr.rightChild

        # set new parameters for new node
        newNode.parent = prev
        if prev is self:
            self.root = newNode
        elif val < prev.val:
            prev.leftChild = newNode
        else:
            prev.rightChild = newNode

        # balance red black tree
        self.insertFixup(newNode)

    def insertFixup(self, node):
        if node == self.root:
            node.flipColor()
            return
        while node.parent.color == 'R':
            if node.parent.isLeftChild():
                uncle = node.parent.parent.rightChild
                if uncle.color == 'R':
                    uncle.flipColor()
                    node.parent.flipColor()
                    node.parent.parent.flipColor()
                    node = node.parent.parent
                else:
                    if node.isRightChild():
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.flipColor()
                    node.parent.parent.flipColor()
                    self.rightRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.leftChild
                if uncle.color == 'R':
                    uncle.flipColor()
                    node.parent.flipColor()
                    node.parent.parent.flipColor()
                    node = node.parent.parent
                else:
                    if node.isLeftChild():
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.flipColor()
                    node.parent.parent.flipColor()
                    self.leftRotate(node.parent.parent)
            if node == self.root:
                break

    def search(self, key):
        curr = self.root
        while curr is not self.NIL:
            if curr.val == key:
                return curr
            elif key < curr.val:
                curr = curr.leftChild
            else:
                curr = curr.rightChild
        return self.NIL

    def treeSize(self):
        return self.calcTreeSize(self.root)

    def calcTreeSize(self, root):
        if root == self.NIL:
            return 0
        return 1 + self.calcTreeSize(root.leftChild) + self.calcTreeSize(root.rightChild)

    def treeHeight(self):
        return self.calcTreeHeight(self.root)

    def calcTreeHeight(self, root):
        if root == self.NIL:
            return 0
        return 1 + max(self.calcTreeHeight(root.leftChild), self.calcTreeHeight(root.leftChild))
