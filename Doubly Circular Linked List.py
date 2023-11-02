class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Circular_DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None:
            return 0
        ct = 1
        current = self.head
        while current.next != self.head:
            ct += 1
            current = current.next
        return ct

    def __str__(self):
        if self.head is None:
            return "Circular linked list is Empty."
        current = self.head
        result = str(current.value)
        while current.next != self.head:
            current = current.next
            result += '<->' + str(current.value)
        return result

    def append(self, value):
        new_Node = Node(value)
        new_Node.next = self.head
        new_Node.previous = self.tail
        self.tail.next = new_Node
        self.head.previous = new_Node
        self.tail = new_Node
        return True

    def prepend(self, value):
        new_Node = Node(value)
        new_Node.next = self.head
        new_Node.previous = self.tail
        self.tail.next = new_Node
        self.head.previous = new_Node
        self.head = new_Node

    def insert(self, value, pos=0):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            new_Node.next = new_Node
            new_Node.previous = new_Node
            return True
        elif pos == 0:
            self.prepend(value)
        elif pos == len(self):
            self.append(value)
        else:
            current = self.head
            ct = 1
            while ct != pos:
                current = current.next
                ct += 1
            if current.next != self.head:
                temp = current.next
                current.next = new_Node
                new_Node.next = temp
                temp.previous = new_Node
                new_Node.previous = current
            else:
                self.append(value)

    def traverse(self, reverse=False):
        if self.head is None:
            return "List is empty"
        if reverse:
            current = self.tail
            while current.previous != self.tail:
                print(current.value, end='<->')
                current = current.previous
            print(current.value)
        else:
            current = self.head
            while current.next != self.head:
                print(current.value, end='<->')
                current = current.next
            print(current.value)

    def search(self, target):
        if self.head is None:
            return -1
        current = self.head
        ct = 0
        while current.next != self.head:
            if current.value == target:
                return ct
            current = current.next
            ct += 1
        if current.value == target:
            return ct
        return -1

    def popFirst(self):
        self.tail.next = self.head.next
        self.head.next.previous = self.tail
        self.head.next = None
        self.head.previous = None
        self.head = self.tail.next
        return True

    def pop(self):
        self.head.previous = self.tail.previous
        self.tail.previous.next = self.head
        self.tail.next = None
        self.tail.previous = None
        self.tail = self.head.previous

    def remove(self, pos):
        if self.head is None:
            return "List is already empty"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif pos == 0:
            self.popFirst()
        elif pos == len(self):
            self.pop()
        else:
            current = self.head
            ct = 0
            while ct != pos:
                current = current.next
                ct += 1
            if current.next != self.head:
                current.previous.next=current.next
                current.next.previous=current.previous
                current.next=None
                current.previous=None
                del current
            else:
                self.pop()


cdll = Circular_DLL()
# cdll.append(10)
# cdll.prepend(15)
# cdll.append(76)
cdll.insert(10)
cdll.insert(40)
cdll.insert(15, len(cdll))
cdll.insert(76, 5)
cdll.insert(80, 1)
print(cdll)
print(len(cdll))
cdll.traverse()
# cdll.traverse(True)
# print(cdll.search(76))
# print(cdll.search(10))
cdll.remove(0)
print(cdll)
cdll.remove(len(cdll)-1)
print(cdll)
cdll.remove(1)
print(cdll)
cdll.remove(2)
print(cdll)
cdll.remove(0)
print(cdll)
