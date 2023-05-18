class Node:

    def __init__(self, value, color='R'):
        self.__value = value
        self.__color = color

        # If not Nil node
        if value != None:
            self.__parent = Nil.get_instance()
            self.__left_node = Nil.get_instance()
            self.__right_node = Nil.get_instance()

    def get_grand_parent(self):
        if self.get_parent() == Nil.get_instance():
            return Nil.get_instance()

        return self.get_parent().get_parent()

    def get_uncle(self):
        if self.get_parent() == Nil.get_instance() or self.get_grand_parent() == Nil.get_instance():
            return Nil.get_instance()

        if self.get_grand_parent().get_left_node() == self.get_parent():
            return self.get_grand_parent().get_right_node()

        return self.get_grand_parent().get_left_node()

    def set_parent(self, parent: 'Node'):
        self.__parent = parent

    def get_parent(self) -> 'Node':
        return self.__parent

    def set_left_node(self, left_node: 'Node'):
        self.__left_node = left_node

    def get_left_node(self) -> 'Node':
        return self.__left_node

    def set_right_node(self, right_node: 'Node'):
        self.__right_node = right_node

    def get_right_node(self) -> 'Node':
        return self.__right_node

    def get_value(self):
        return self.__value

    def change_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __str__(self):
        return f"{self.get_value()}({self.get_color()})"

    # Singleton Nil class


class Nil():
    __instance = None

    def __init__(self):
        if Nil.__instance is not None:
            raise Exception("Nil instance already exists.")
        Nil.__instance = Node(None, 'B')
        Nil.__instance.set_parent(None)

    def __str__(self):
        return f"Nil"

    @staticmethod
    def get_instance():
        if Nil.__instance is None:
            Nil()
        return Nil.__instance


class RedBlackTree:
    def __init__(self):
        self.__root = Nil.get_instance()
        self.__size = 0
        self.__height = 0

    def get_root(self) -> Node:
        return self.__root

    def set_root(self, root: Node):
        self.__root = root

    def get_size(self) -> Node:
        return self.__size

    def inc_size(self):
        self.__size += 1

    def __get_height_helper(self, root: Node) -> Node:
        if root is Nil.get_instance():
            return 0

        left_height = self.__get_height_helper(root.get_left_node())
        right_height = self.__get_height_helper(root.get_right_node())

        return max(left_height, right_height) + 1

    def get_height(self) -> Node:
        return self.__get_height_helper(self.get_root())

    def __search_helper(self, data, root: Node):

        # Base cases
        if root == Nil.get_instance():
            return False
        if root.get_value() == data:
            return True

        elif data > root.get_value():
            return self.__search_helper(data, root.get_right_node())
        else:
            return self.__search_helper(data, root.get_left_node())

    def search(self, data):
        return self.__search_helper(data, self.get_root())

    def left_rotate(self, x: Node):
        y = x.get_right_node()
        x.set_right_node(y.get_left_node())

        if y.get_left_node() != Nil.get_instance():
            y.get_left_node().set_parent(x)

        y.set_parent(x.get_parent())

        if x.get_parent() == Nil.get_instance():
            self.set_root(y)

        elif x == x.get_parent().get_left_node():
            x.get_parent().set_left_node(y)

        else:
            x.get_parent().set_right_node(y)

        y.set_left_node(x)

        x.set_parent(y)

    def right_rotate(self, y: Node):
        x = y.get_left_node()
        y.set_left_node(x.get_right_node())

        if x.get_right_node() != Nil.get_instance():
            x.get_right_node().set_parent(y)

        x.set_parent(y.get_parent())

        if y.get_parent() == Nil.get_instance():
            self.set_root(x)

        elif y == y.get_parent().get_right_node():
            y.get_parent().set_right_node(x)

        else:
            y.get_parent().set_left_node(x)

        x.set_right_node(y)

        y.set_parent(x)

    def __insert_helper(self, data, root: Node, parent: Node):
        if root == Nil.get_instance():
            new_node = Node(data, 'R')
            new_node.set_parent(parent)

            if self.get_root() == Nil.get_instance():
                self.set_root(new_node)
            else:
                if data > parent.get_value():
                    parent.set_right_node(new_node)
                else:
                    parent.set_left_node(new_node)

            self.__insert_fixup(new_node)

        elif data > root.get_value():
            self.__insert_helper(data, root.get_right_node(), root)
        else:
            self.__insert_helper(data, root.get_left_node(), root)

    def fixup_case1(self, node: Node):
        node.get_uncle().change_color('B')
        node.get_parent().change_color('B')
        node.get_grand_parent().change_color('R')

    def fixup_case2(self, node_parent: Node):
        if node_parent.get_parent().get_left_node() == node_parent:
            self.left_rotate(node_parent)
        elif node_parent.get_parent().get_right_node() == node_parent:
            self.right_rotate(node_parent)

    def fixup_case3(self, node: Node):
        node.get_parent().change_color('B')
        node.get_grand_parent().change_color('R')

        if node.get_grand_parent().get_left_node() == node.get_parent():
            self.right_rotate(node.get_grand_parent())
        elif node.get_grand_parent().get_right_node() == node.get_parent():
            self.left_rotate(node.get_grand_parent())

    def insert(self, data):
        self.__insert_helper(data, self.get_root(), Nil.get_instance())
        self.inc_size()

    def __insert_fixup(self, node: Node):
        while node.get_parent().get_color() == 'R':
            if node.get_uncle().get_color() == 'R':
                self.fixup_case1(node)
                node = node.get_grand_parent()
            else:
                # Case 2
                if ((
                        node.get_grand_parent().get_left_node() == node.get_parent() and node.get_parent().get_right_node() == node) or
                        (
                                node.get_grand_parent().get_right_node() == node.get_parent() and node.get_parent().get_left_node() == node)):
                    node = node.get_parent()
                    self.fixup_case2(node)

                self.fixup_case3(node)  # Case 3

        self.get_root().change_color('B')
