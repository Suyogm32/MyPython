import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
        customqueue = queue.Queue()
        customqueue.put(root)
        while not customqueue.empty():
            root = customqueue.get()
            print(root.data)
            if root.left is not None:
                customqueue.put(root.left)
            if root.right is not None:
                customqueue.put(root.right)


def search(root, target):
    if not root:
        return "the BT dose not exist"
    else:
        customqueue = queue.Queue()
        customqueue.put(root)
        while not customqueue.empty():
            root = customqueue.get()
            if root.data == target:
                return "Success"
            if root.left is not None:
                customqueue.put(root.left)
            if root.right is not None:
                customqueue.put(root.right)
        return "Not Found"


def insert(root, newNode):
    if not root:
        root = newNode
    else:
        custom_queue = queue.Queue()
        custom_queue.put(root)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.left is not None:
                custom_queue.put(root.left)
            else:
                root.left = newNode
                return "Successfully inserted"
            if root.right is not None:
                custom_queue.put(root.right)
            else:
                root.right = newNode
                return "Successfully inserted"


def getDeepestNode(root):
    if not root:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.put(root)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.left is not None:
                custom_queue.put(root.left)
            if root.right is not None:
                custom_queue.put(root.right)
        deepestNode = root
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.put(rootNode)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root is dNode:
                root = None
                return "Deleted Successfully"
            if root.left:
                if root.left is dNode:
                    root.left = None
                    return "Deleted Successfully"
                else:
                    custom_queue.put(root.left)
            if root.right:
                if root.right is dNode:
                    root.right = None
                    return "Deleted Successfully"
                else:
                    custom_queue.put(root.right)
        return "Failed to delete"


def deleteNode(rootNode, target):
    if not rootNode:
        return "BT does not exist"
    else:
        custom_queue = queue.Queue()
        custom_queue.put(rootNode)
        dNode = getDeepestNode(rootNode)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.data == target:
                root.data = dNode.data
                myNode = getDeepestNode(rootNode)
                print("MyNode data is", myNode.data)
                deleteDeepestNode(rootNode, myNode)
                return "Node deleted Successfully"
            if root.left is not None:
                custom_queue.put(root.left)
            if root.right is not None:
                custom_queue.put(root.right)


newBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
sprite = TreeNode("Sprite")
mirinda = TreeNode("Mirinda")
newBT.left = hot
newBT.right = cold
hot.left = tea
hot.right = coffee
cold.left = mirinda
cold.right = sprite
# print("Preorder Traversal")
# preOrderTraversal(newBT)
# print("Inorder Traversal")
# inOrderTraversal(newBT)
# print("postorder Traversal")
# postOrderTraversal(newBT)

# print("Search Method")
# print(search(newBT, "Sprite"))
# print(search(newBT, "pepsi"))
ltea = TreeNode("Lemon Tea")
print(insert(newBT, ltea))
# print("Level order Traversal")
# levelOrderTraversal(newBT)
deepNode = getDeepestNode(newBT)
print(deepNode.data)
print(deleteDeepestNode(newBT, deepNode))
levelOrderTraversal(newBT)
print(deleteNode(newBT, "Hot"))
levelOrderTraversal(newBT)
