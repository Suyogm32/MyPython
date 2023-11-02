class Queue_PList:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty!"
        values = [str(x) for x in self.list]
        return '|'.join(values)

    def enqueue(self, value):
        self.list.insert(0, value)
        return "Element is inserted."

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        self.list.pop()
        return "One element is dequeued"

    def peek(self):
        return self.list[len(self.list) - 1]

    def deleteQueue(self):
        self.list = None
        return "Queue is deleted"


queue = Queue_PList()
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
