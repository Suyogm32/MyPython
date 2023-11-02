import queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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


def getHeight(root):
    if not root:
        return 0
    return root.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.left
    disbalancedNode.left = disbalancedNode.left.right
    newRoot.right = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.left), getHeight(disbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.right
    disbalancedNode.right = disbalancedNode.right.left
    newRoot.left = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.left), getHeight(disbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def getBalance(root):
    if not root:
        return root
    return getHeight(root.left) - getHeight(root.right)


def insertNode(root, value):
    if not root:
        return AVLNode(value)
    elif value < root.data:
        root.left = insertNode(root.left, value)
    else:
        root.right = insertNode(root.right, value)
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)
    if balance > 1 and value < root.left.data:
        return rightRotate(root)
    if balance > 1 and value > root.left.data:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and value > root.right.data:
        return leftRotate(root)
    if balance < -1 and value < root.right.data:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root


def getMinimum(root):
    if root is None or root.left is None:
        return root
    return getMinimum(root.left)


def deleteNode(root, value):
    if not root:
        return root
    elif value < root.data:
        root.left = deleteNode(root.left, value)
    elif value > root.data:
        root.data = deleteNode(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = getMinimum(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root


newAVl = AVLNode(30)
newAVl = insertNode(newAVl, 25)
newAVl = insertNode(newAVl, 35)
newAVl = insertNode(newAVl, 20)
newAVl = insertNode(newAVl, 15)
newAVl = insertNode(newAVl, 5)
newAVl = insertNode(newAVl, 10)
newAVl = insertNode(newAVl, 50)
newAVl = insertNode(newAVl, 60)
newAVl = insertNode(newAVl, 70)
newAVl = insertNode(newAVl, 65)
newAVl = insertNode(newAVl, 4)
newAVl = insertNode(newAVl, 7)
newAVl = insertNode(newAVl, 23)

newAVl = deleteNode(newAVl, 7)
levelOrderTraversal(newAVl)
