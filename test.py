#!/usr/bin/env python3

import algorithms

queue = algorithms.NodeQueue()

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(10)
queue.enqueue(132)

print(str(queue.dequeue()))
print(str(queue.dequeue()))
print(str(queue.dequeue()))
print(str(queue.dequeue()))
