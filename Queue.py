class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        if self.isEmpty():
            return 0
        current = self.head
        ct = 0
        while current is not None:
            ct += 1
            current = current.next
        return ct

    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty!"
        current = self.head
        result = '|'
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += '|'
            current = current.next
        return result

    def enqueue(self, value):
        new_Node = Node(value)
        if self.isEmpty():
            self.head = new_Node
            return "One element is enqueued"
        new_Node.next = self.head
        self.head = new_Node
        return "One element is enqueued"

    def dequeue(self):
        if self.isEmpty():
            return "Element can not be removed as Queue is Empty"
        if len(self) == 1:
            self.head = None
            return None
        current = self.head
        while current.next is not None:
            temp = current
            current = current.next

        temp.next = None
        del current

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        current = self.head
        while current.next is not None:
            current = current.next
        return current.value

    def deleteQueue(self):
        if self.isEmpty():
            return "Queue is empty"
        current = self.head
        while current.next is not None:
            temp = current
            current = current.next
            temp.next = None
            del temp
        self.head = None
        return "Queue is deleted"


queue = Queue()
print(queue.isEmpty())
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
print(queue)
queue.dequeue()
print(queue)
print(queue.peek())
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)
print(queue.enqueue(75))
print(queue)
print(queue.deleteQueue())
