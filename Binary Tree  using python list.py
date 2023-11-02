class BinaryTree:
    def __init__(self, size):
        self.Btlist = [None] * size
        self.lastUsedIndex = 0
        self.maxsize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return "Binary Tree is Full"
        self.Btlist[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Value is inserted successfully"

    def search(self, target):
        for i in range(len(self.Btlist)):
            if self.Btlist[i] == target:
                return f"Node found at position-> {i}"
        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.Btlist[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.Btlist[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.Btlist[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.Btlist[i])

    def deleteNode(self, target):
        if self.lastUsedIndex == 0:
            return "BT is Empty"
        for i in range(1, self.lastUsedIndex + 1):
            if self.Btlist[i] == target:
                self.Btlist[i] = self.Btlist[self.lastUsedIndex]
                self.Btlist[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node has been deleted successfully"

    def deleteTree(self):
        self.Btlist = None
        return "Deleted Entire Tree"


newBt = BinaryTree(15)
newBt.insertNode("Drinks")
newBt.insertNode("Hot")
newBt.insertNode("Cold")
newBt.insertNode("Tea")
newBt.insertNode("Coffee")
newBt.insertNode("Sprite")
newBt.insertNode("Fanta")
print(newBt.Btlist)
# print(newBt.search("Sprite"))
# print("Pre-Order Traversal")
# newBt.preOrderTraversal(1)
# print("In-Order Traversal")
# newBt.inOrderTraversal(1)
# print("Post-Order Traversal")
# newBt.postOrderTraversal(1)
# print("Level-Order Trversal")
# newBt.levelOrderTraversal(1)
print(newBt.deleteNode("Cold"))
print(newBt.deleteTree())
print(newBt.Btlist)
