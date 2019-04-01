#!/usr/bin/env python3

import algorithms

queue = algorithms.Queue()
stack = algorithms.Stack()
print("Size: ", str(stack.size()), " Empty?: ", str(stack.isEmpty()))
stack.push(1)
print("Size: ", str(stack.size()), " Empty?: ", str(stack.isEmpty()))
stack.push(2)
print("Size: ", str(stack.size()), " Empty?: ", str(stack.isEmpty()))
stack.push(3)
print("Size: ", str(stack.size()), " Empty?: ", str(stack.isEmpty()))

print("Stack")
print(str(stack.pop()))
print(str(stack.pop()))
print(str(stack.pop()))

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("")
print("Queue")
print(str(queue.dequeue()))
print(str(queue.dequeue()))
print(str(queue.dequeue()))





