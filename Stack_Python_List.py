class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        result='|'
        for ele in self.list:
            result += str(ele)+"|"
        return result

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, value):
        self.list.append(value)
        return f"The element ${value} is inserted successfully."

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list[len(self.list)-1]


st = Stack()
print(st.isEmpty())
st.push(1)
st.push(2)
st.push(4)
print(st)
st.pop()
print(st)
st.pop()
st.pop()
print(st.peek())