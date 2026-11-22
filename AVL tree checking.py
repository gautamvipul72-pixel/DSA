
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def checkAVL(root):

    def check(node, minVal, maxVal):
        if node is None:
            return 0

        if node.val <= minVal or node.val >= maxVal:
            return -1

        leftHeight = check(node.left, minVal, node.val)

        if leftHeight == -1:
            return -1

        rightHeight = check(node.right, node.val, maxVal)

        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)

    return check(root, float('-inf'), float('inf')) != -1

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

if checkAVL(root):
    print("The tree is an AVL Tree")
else:
    print("The tree is not an AVL Tree")
