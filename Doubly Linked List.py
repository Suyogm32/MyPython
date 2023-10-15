class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += '<->'
            current = current.next
        return result

    def __len__(self):
        if self.head is None:
            return 0
        current = self.head
        ct = 0
        while current is not None:
            current = current.next
            ct += 1
        return ct

    def append(self, value):
        new_Node = Node(value)
        if len(self) == 0:
            self.head = new_Node
            self.tail = new_Node
            return True
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_Node
        new_Node.previous = current
        self.tail = new_Node

    def prepend(self, value):
        new_Node = Node(value)
        if len(self) == 0:
            self.head = new_Node
            self.tail = new_Node
            return True
        new_Node.next = self.head
        self.head.previous = new_Node
        self.head = new_Node

    def insert(self, value, pos=0):
        if pos == 0:
            self.prepend(value)
        elif pos == len(self):
            self.append(value)
        else:
            new_Node = Node(value)
            current = self.head
            count = 1
            while current.next is not None and count != pos:
                current = current.next
                count += 1
            if current.next is not None:
                temp = current.next
                current.next = new_Node
                new_Node.next = temp
                temp.previous = new_Node
                new_Node.previous = current
            else:
                self.append(value)

    def search(self, target):
        current = self.head
        ct = 0
        while current is not None:
            if current.value == target:
                return ct
            current = current.next
            ct += 1
        return -1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end='<->')
            current = current.next

    def Reverse_treavers(self):
        current = self.tail
        while current is not None:
            print(current.value, end='<->')
            current = current.previous

    def popFirst(self):
        if self.head is None:
            return "List is empty"
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return None
        temp = self.head.next
        self.head.next = None
        temp.previous = None
        self.head = temp

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return None
        temp = self.tail.previous
        self.tail.previous = None
        temp.next = None
        self.tail = temp

    def remove(self, pos=0):
        if pos == 0:
            self.popFirst()
        elif pos == len(self) - 1:
            self.pop()
        else:
            current = self.head
            count = 1
            while current.next is not None and count != pos:
                current = current.next
                count += 1
            if current.next is not None:
                temp1 = current.next
                temp2 = temp1.next
                current.next = temp2
                temp2.previous = current
                temp1.next = None
                temp1.previous = None
                del temp1


dll = Doubly_Linked_List()
# dll.append(10)
# dll.append(15)
# dll.append(30)
# dll.prepend(5)
dll.insert(10)
dll.insert(30, 2)
print(dll)
print(dll.tail.value)
print(len(dll) - 1)
dll.insert(45, 1)
print(dll)
dll.insert(15, 2)
print(dll)
dll.insert(35, 1)
print(dll)
dll.insert(5)
print(dll)
print("Length of Doubly liknked list is ", len(dll))
print("THe value 69 is at ", dll.search(69))
print("THe value 15 is at ", dll.search(15))

# Delete operations
# print(dll)
# dll.popFirst()
# print(dll)
# dll.pop()
print(dll)
dll.remove(0)
dll.remove(len(dll)-1)
dll.remove(2)
print(dll)
