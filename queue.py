from collections import deque

class queue:
    def __init__ (self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

if __name__ == "__main__":
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    print(q.buffer)
    q.dequeue()
    print(q.buffer)
    q.dequeue()
    print(q.buffer)
    q.dequeue()
