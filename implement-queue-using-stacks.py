"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""

class MyQueue:
    def __init__(self):
        self.placeholder_stack = []
        self.active_stack = []

    def push(self, x: int) -> None:
        self.active_stack.append(x)

    def pop(self) -> int:
        while len(self.active_stack) > 1:
            self.placeholder_stack.append(self.active_stack.pop())

        remaining_val = self.active_stack.pop()
        while self.placeholder_stack:
            self.active_stack.append(self.placeholder_stack.pop())

        return remaining_val

    def peek(self) -> int:
        while len(self.active_stack) > 1:
            self.placeholder_stack.append(self.active_stack.pop())

        remaining_val = self.active_stack.pop()
        self.placeholder_stack.append(remaining_val)
        while self.placeholder_stack:
            self.active_stack.append(self.placeholder_stack.pop())

        return remaining_val

    def empty(self) -> bool:
        return not self.active_stack


# Your MyQueue object will be instantiated and called as such:
myQueue = MyQueue()
print(myQueue.empty()) # return false

myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek()) # return 1
print(myQueue.pop()) # return 1, queue is [2]
print(myQueue.empty()) # return false
print(myQueue.pop()) # return 1, queue is [2]
print(myQueue.empty()) # return false