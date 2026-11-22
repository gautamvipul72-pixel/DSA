
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def checkAVL(root, minVal=float('-inf'), maxVal=float('inf')):

    if root is None:
        return 0

    if root.val <= minVal or root.val >= maxVal:
        return -1

    leftHeight = checkAVL(root.left, minVal, root.val)
    if leftHeight == -1:
        return -1

    rightHeight = checkAVL(root.right, root.val, maxVal)
    if rightHeight == -1:
        return -1

    if abs(leftHeight - rightHeight) > 1:
        return -1

    return max(leftHeight, rightHeight) + 1


def isAVL(root):
    return checkAVL(root) != -1


# Creating a Binary Tree
root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(10)
root.left.right = Node(25)

if isAVL(root):
    print("The tree is an AVL Tree")
else:
    print("The tree is not an AVL Tree")
