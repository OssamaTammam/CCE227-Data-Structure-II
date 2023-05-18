class Node:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBT:
    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.size = 0

    def insert(self, val):
        self.size += 1
        newNode = Node(val)
        newNode.parent = None
        newNode.left = self.nil
        newNode.right = self.nil
        newNode.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if newNode.val < current.val:
                current = current.left
            elif newNode.val > current.val:
                current = current.right
            else:
                return

        newNode.parent = parent
        if parent is None:
            self.root = newNode
        elif newNode.val < parent.val:
            parent.left = newNode
        else:
            parent.right = newNode

        self.insertFix(newNode)

    def insertFix(self, newNode):
        while newNode != self.root and newNode.parent.red:
            if newNode.parent == newNode.parent.parent.right:
                uncle = newNode.parent.parent.left
                if uncle.red:
                    uncle.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rotateRight(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.rotateLeft(newNode.parent.parent)
            else:
                uncle = newNode.parent.parent.right

                if uncle.red:
                    uncle.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.rotateLeft(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.rotateRight(newNode.parent.parent)
        self.root.red = False

    def rotateLeft(self, rotatedNode):
        replacementNode = rotatedNode.right
        rotatedNode.right = replacementNode.left
        if replacementNode.left != self.nil:
            replacementNode.left.parent = rotatedNode

        replacementNode.parent = rotatedNode.parent
        if rotatedNode.parent is None:
            self.root = replacementNode
        elif rotatedNode == rotatedNode.parent.left:
            rotatedNode.parent.left = replacementNode
        else:
            rotatedNode.parent.right = replacementNode
        replacementNode.left = rotatedNode
        rotatedNode.parent = replacementNode

    def rotateRight(self, rotatedNode):
        replacementNode = rotatedNode.left
        rotatedNode.left = replacementNode.right
        if replacementNode.right != self.nil:
            replacementNode.right.parent = rotatedNode

        replacementNode.parent = rotatedNode.parent
        if rotatedNode.parent is None:
            self.root = replacementNode
        elif rotatedNode == rotatedNode.parent.right:
            rotatedNode.parent.right = replacementNode
        else:
            rotatedNode.parent.left = replacementNode
        replacementNode.right = rotatedNode
        rotatedNode.parent = replacementNode

    def search(self, val):
        current = self.root
        while current != self.nil:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return current
        return None

    def treeSize(self):
        return self.size

    def treeHeight(self, root):
        if root is self.nil:
            return 0
        else:
            leftHeight = self.treeHeight(root.left)
            rightHeight = self.treeHeight(root.right)
            return 1 + max(leftHeight, rightHeight)
