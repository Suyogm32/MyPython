import queue


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, val):
    if root.data is None:
        root.data = val
    elif val <= root.data:
        if root.left is None:
            newNode = BSTNode(val)
            root.left = newNode
        else:
            insert(root.left, val)
    else:
        if root.right is None:
            newNode = BSTNode(val)
            root.right = newNode
        else:
            insert(root.right, val)

    return "New Node is inserted"


def preOrderTraversal(root):
    if root is not None:
        print(root.data)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
    else:
        return None


def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)


def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


def levelOrderTraversal(root):
    if not root:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.put(root)
        while not custom_queue.empty():
            root = custom_queue.get()
            print(root.data)
            if root.left is not None:
                custom_queue.put(root.left)
            if root.right is not None:
                custom_queue.put(root.right)


def search(root, target):
    if root.data == target:
        print("Value is Found")
    elif target < root.data:
        if root.left.data == target:
            print("Value is found")
        else:
            search(root.left, target)
    else:
        if root.right.data == target:
            print("Value is Found")
        else:
            search(root.right, target)


def minValueNode(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, target):
    if root is None:
        return root
    if target < root.data:
        root.left = deleteNode(root.left, target)
    elif target > root.data:
        root.right = deleteNode(root.right, target)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        if root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root


def deleteBST(root):
    root.data = None
    root.left = None
    root.right = None
    return "The BST is deleted"


newBST = BSTNode(None)
insert(newBST, 10)
insert(newBST, 15)
insert(newBST, 5)
insert(newBST,2)
insert(newBST, 9)
insert(newBST, 12)
# print(newBST.data)
# print(newBST.left.data)
# print("Pre-Order Traversal")
# preOrderTraversal(newBST)
# print("In-Order Traversal")
# inOrderTraversal(newBST)
# print("Post-Order Traversal")
# postOrderTraversal(newBST)
print("Level-Order Traversal")
levelOrderTraversal(newBST)
search(newBST, 12)
deleteNode(newBST, 10)
levelOrderTraversal(newBST)

