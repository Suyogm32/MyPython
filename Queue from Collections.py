from collections import deque

customQueue=deque(maxlen=4)

print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)

print(customQueue.popleft())
print(customQueue)
print(customQueue.clear())
print(customQueue)