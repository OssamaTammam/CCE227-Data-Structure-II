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
        self.Nil.color.flipcolor()
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
        if prev is None:
            self.root = newNode
        elif val < prev.val:
            prev.leftChild = newNode
        else:
            prev.rightChild = newNode

        # balance red black tree
        self.restoreRBT(newNode)

    def restoreRBT(self, node):
