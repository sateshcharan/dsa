from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    pass
    s = Stack()
    s.push("hello")
    s.push("world")
    print(s.container)
    s.peek()
    s.pop()
    print(s.container)
    s.pop()
    print(s.container)
    # s.is_empty()
    # s.size()