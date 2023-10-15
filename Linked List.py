from Node import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = new_node

    def insert(self, pos, value):
        self.length += 1
        # self.tail = new_node
        if pos < 0:
            print(len(self), (pos + 1))
            pos = len(self) + (pos + 1)
            print(pos)
        if pos == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return None
        current = self.head
        count = 1
        while current.next is not None and count != pos:
            current = current.next
            count += 1
        if current.next is not None:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
        else:
            self.append(value)

    def __str__(self):
        current = self.head
        result = ''
        # result = 'head->'
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += '->'
            current = current.next
        # result += '<-tail'
        return result

    def __len__(self):
        current = self.head
        ct = 0
        while current is not None:
            current = current.next
            ct += 1
        return ct

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def get(self, idx):
        current = self.head
        if idx < 0:
            idx = len(self) + idx
        if idx < 0 or idx >= len(self):
            return None
        for _ in range(idx):
            current = current.next
        return current

    def set_Value(self, idx, val):
        current = self.get(idx)
        if current:
            current.value = val
            return True
        return False

    def remove(self, idx):
        current = self.head
        # self.length-=1
        if idx == 0:
            self.head = self.head.next
            current.next = None
            # temp = current
            del current
            return None
        ct = 1
        while current.next is not None and ct != idx:
            current = current.next
            ct += 1
        if current.next is not None:
            temp = current.next
            current.next = current.next.next
            del temp
        else:
            return None


new_Linked_list = LinkedList(10)
new_Linked_list2 = LinkedList(70)
print(new_Linked_list)
new_Linked_list2.append(69)
# new_Linked_list.append(new_Linked_list2)
print("Linked list after inserting value at end\n", new_Linked_list)
new_Linked_list.insert(4, 20)
new_Linked_list.insert(0, 50)
print("Linked list after inserting new element 20 at position 3\n", new_Linked_list)
print("head->", new_Linked_list.head.value)
print("tail->", new_Linked_list.tail.value)
print("Length of linked list is", len(new_Linked_list))
print(new_Linked_list)
new_Linked_list.insert(-5, 150)
print("Linked list after inserting new element 150 at position -1\n", new_Linked_list)
print(new_Linked_list.head.value)
print(new_Linked_list2.search(69))
print(new_Linked_list.get(3))
print(new_Linked_list.set_Value(2, 89))
print(new_Linked_list)
print(new_Linked_list.remove(0))
print(new_Linked_list)
