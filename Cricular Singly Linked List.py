from Node import Node


class Circular_SLL:
    def __init__(self):
        # new_Node = Node(value)
        # self.head = new_Node
        # new_Node.next = new_Node
        # self.tail = new_Node
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None:
            return 0
        current = self.head
        ct = 1
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
            result += '->' + str(current.value)
            # if current.next != self.head:
            #     result += '->'

        return result

    def append(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            new_Node.next = new_Node
            self.tail = new_Node
            return None
        current = self.head
        for _ in range(len(self) - 1):
            current = current.next
        new_Node.next = self.head
        current.next = new_Node

    def prepend(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            new_Node.next = new_Node
            self.tail = new_Node
            return None
        current = self.head
        for _ in range(len(self) - 1):
            current = current.next
        current.next = new_Node
        new_Node.next = self.head
        self.head = new_Node

    def insert(self, pos, value):
        place = pos // len(self)
        # pos = pos % len(self)
        if pos == 0 and place == 0:
            self.prepend(value)
        elif place > 0:
            self.append(value)
        else:
            new_Node = Node(value)
            current = self.head
            ct = 0
            while ct != pos:
                current = current.next
                ct += 1
            new_Node.next = current.next
            current.next = new_Node

    def search(self, target):
        if self.head is None:
            return -1
        ct = 0
        current = self.head
        while current.next != self.head:
            if current.value == target:
                return ct
            current = current.next
            ct += 1
        return -1

    def get(self, idx):
        if idx < 0 or idx >= len(self):
            return None
        current = self.head
        for _ in range(idx):
            current = current.next
        return current

    def set_value(self, idx, val):
        current = self.get(idx)
        if current:
            current.value = val
            return True
        return False

    def pop_First(self):
        if self.head.next == self.head:
            self.head = None
            self.tail = None
            return None
        current = self.head
        while current.next != self.head:
            current = current.next
        temp = self.head
        current.next = temp.next
        self.head = temp.next
        temp.next = None
        del temp

    def pop(self):
        current = self.head
        # print(len(self)-2)
        for _ in range(len(self) - 2):
            current = current.next
        temp = current.next
        current.next = temp.next
        temp.next = None
        del temp

    def remove(self, idx):
        if idx == 0 and idx == len(self) - 1:
            temp = self.head
            self.head = None
            del temp
        elif idx == 0:
            self.pop_First()
        elif idx == len(self) - 1:
            self.pop()
        else:
            ct = 0
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            temp = current.next
            current.next = temp.next
            temp.next = None
            del temp


csll = Circular_SLL()
print(len(csll))
print(csll)
csll.append(15)
csll.append(60)
csll.insert(3, 30)
print(len(csll))
csll.insert(4, 78)
print(csll)
csll.insert(7, 80)
print(csll)
# print(csll.head.value)
# print(csll.search(69))
# print(csll.search(30))
# print(csll.get(7))
# print(csll.set_value(4, 69))

# csll.remove(0)
# print("After removing first", csll)
csll.remove(4)
print("After removing 4th Element", csll)
print("Before removing element", csll)
csll.remove(len(csll) - 1)
csll.remove(0)
print("After removing 0th idx", csll)
