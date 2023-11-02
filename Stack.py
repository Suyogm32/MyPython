class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def __len__(self):
        if self.head is None:
            return 0
        current = self.head
        ct = 0
        while current is not None:
            ct += 1
            current = current.next
        return ct

    def __str__(self):
        if self.isEmpty():
            return "Stack is Empty"
        current = self.head
        result = '|'
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += '|'
            current = current.next
        return result

    def isEmpty(self):
        return self.head is None

    def push(self, value):
        new_Node = Node(value)
        if self.isEmpty():
            self.head = new_Node
            return None
        new_Node.next = self.head
        self.head = new_Node

    def pop(self):
        if self.isEmpty():
            return None
        elif self.head.next is None:
            val = self.head.value
            self.head = None
            return val
        else:
            val = self.head.value
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            return val

    def peek(self):
        return self.head.value

    def deleteStack(self):
        current = self.head
        self.head = None
        while current is not None:
            temp = current
            current = current.next
            temp.next = None
            del temp


stack = Stack()
print(stack.isEmpty())
stack.push(10)
stack.push(75)
stack.push(90)
stack.push(78)
stack.push(140)
print(len(stack))
print(stack)
print(stack.peek())
stack.pop()
stack.pop()
print(len(stack))
print(stack)
stack.deleteStack()
print(stack)
