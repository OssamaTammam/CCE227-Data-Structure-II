import RBT


class Dictionary:
    def __init__(self, fileName):
        self.fileName = fileName + ".txt"
        self.dictTree = RBT.RBT()
        self.loadFile()

    def loadFile(self):
        dictFile = open(self.fileName, "r")
        for line in dictFile:
            self.dictTree.insert(line.strip())
        dictFile.close()

    def insert(self, word):
        if self.search(word) is True:
            print("ERROR: Word already in the dictionary!")
        else:
            self.dictTree.insert(word)
        dictFile = open(self.fileName, "a")
        dictFile.write(f"{word}\n")
        dictFile.close()

    def search(self, word):
        if self.dictTree.search(word) is self.dictTree.NIL:
            print("NO")
            return False
        print("YES")
        return True

    def printSize(self):
        print(f"Number of elements is {self.dictTree.treeSize()}\nTree height is {self.dictTree.treeHeight()}")
