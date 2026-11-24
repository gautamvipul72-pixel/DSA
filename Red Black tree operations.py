class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = self.TNULL
        self.TNULL.right = self.TNULL
        self.root = self.TNULL

    def left_rotate(self, node):
        new_node = node.right
        node.right = new_node.left

        if new_node.left != self.TNULL:
            new_node.left.parent = node

        new_node.parent = node.parent

        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        new_node.left = node
        node.parent = new_node

    def right_rotate(self, node):
        new_node = node.left
        node.left = new_node.right

        if new_node.right != self.TNULL:
            new_node.right.parent = node

        new_node.parent = node.parent

        if node.parent is None:
            self.root = new_node
        elif node == node.parent.right:
            node.parent.right = new_node
        else:
            node.parent.left = new_node

        new_node.right = node
        node.parent = new_node

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.color = 1

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current

            if key < current.val:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 0
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent.color == 1:

            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent

                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)

            else:
                uncle = node.parent.parent.right

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent

                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = 0

    def search(self, key):
        current = self.root

        while current != self.TNULL:
            if current.val == key:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right

        return None

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left

        return node

    def transplant(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

        new_node.parent = old_node.parent

    def delete(self, key):
        node = self.search(key)

        if node is None:
            print(key, "not found")
            return

        replace_node = node
        original_color = replace_node.color

        if node.left == self.TNULL:
            child = node.right
            self.transplant(node, node.right)

        elif node.right == self.TNULL:
            child = node.left
            self.transplant(node, node.left)

        else:
            replace_node = self.minimum(node.right)
            original_color = replace_node.color
            child = replace_node.right

            if replace_node.parent == node:
                child.parent = replace_node
            else:
                self.transplant(replace_node, replace_node.right)
                replace_node.right = node.right
                replace_node.right.parent = replace_node

            self.transplant(node, replace_node)
            replace_node.left = node.left
            replace_node.left.parent = replace_node
            replace_node.color = node.color

        if original_color == 0:
            self.fix_delete(child)

    def fix_delete(self, node):
        while node != self.root and node.color == 0:

            if node == node.parent.left:
                sibling = node.parent.right

                if sibling.color == 1:
                    sibling.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    node = node.parent

                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.right_rotate(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = 0
                    sibling.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root

            else:
                sibling = node.parent.left

                if sibling.color == 1:
                    sibling.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == 0 and sibling.left.color == 0:
                    sibling.color = 1
                    node = node.parent

                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.left_rotate(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 0
                    sibling.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root

        node.color = 0

    def inorder(self):
        self.inorder_helper(self.root)
        print()

    def inorder_helper(self, node):
        if node != self.TNULL:
            self.inorder_helper(node.left)

            color = "RED" if node.color == 1 else "BLACK"
            print(f"{node.val} ({color})", end=" ")

            self.inorder_helper(node.right)

    def printTree(self):
        self.print_tree(self.root)

    def print_tree(self, node, space="", last=True):
        if node != self.TNULL:
            print(space, end="")

            if last:
                print("R----", end="")
                space += "     "
            else:
                print("L----", end="")
                space += "|    "

            color = "RED" if node.color == 1 else "BLACK"
            print(f"{node.val} ({color})")

            self.print_tree(node.left, space, False)
            self.print_tree(node.right, space, True)


rbt = RedBlackTree()

values = [41, 38, 31, 12, 19, 8]

for value in values:
    rbt.insert(value)

print("Red-Black Tree:")
rbt.printTree()

print("\nInorder Traversal:")
rbt.inorder()

print("\nSearching for 19:")
if rbt.search(19):
    print("Element found")
else:
    print("Element not found")

print("\nDeleting 19:")
rbt.delete(19)

rbt.printTree()

print("\nInorder after deletion:")
rbt.inorder()
