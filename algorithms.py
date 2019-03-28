#!/usr/bin/env python3

########################################
# Book Algorithm Examples
########################################

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

def max(arr):
    max = arr[0]
    for value in arr:
        if value > max:
            max = value
    return max

def avg(arr):
    sum = 0.0
    for value in arr:
        sum += value
    return sum / len(arr)

def copy(arr):
    copy = []
    for value in arr:
        copy.append(value)
    return copy

def reverse(arr):
    N = len(arr)
    for i in range(0, int(N/2)):
        tmp = arr[i]
        arr[i] = arr[N-1-i]
        arr[N-i-1] = tmp
    return arr

def matrix_square_mult(a, b):
    N = len(a)
    result = [[0 for x in range(len(a))] for y in range(len(b))]

    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                tmp_a = a[i][k]
                tmp_b = b[k][j]
                a_times_b = tmp_a * tmp_b
                result[i][j] += a_times_b
    return result

def abs(x):
    if x < 0: return -x
    else: return x

def isPrime(x):
    if (x < 2): return False
    i = 2
    while(True):
        if i*i > x: break
        if (x % i == 0): return False
        i = i + 1
    return True

def sqrt(x):
    if x < 0: return float('NaN')
    ans = x
    precision = 1e-15
    while (abs(ans - x/ans) > precision * 1):
        ans = (x/ans + ans) / 2
    return ans

def hypotenuse_of_right_triangle(x, y): 
    return sqrt(x*x + y*y)

def harmonic_number(x):
    sum = 0.0
    for i in range(1, x):
        sum = sum + 1.0 / i
    return sum

# This returns the index of where the value passed in is.
def binary_search(key, arr):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if    key < arr[mid]: hi = mid - 1
        elif  key > arr[mid]: lo = mid + 1
        else:                 return mid
    return int('NaN')


########################################
# Collections
########################################

class Bag:
    def __init__(self):

class Queue:
    def __init__(self):

class Stack:
    def __init__(self):

class PriorityQueueMin:
    def __init__(self):

class PriorityQueueMax:
    def __init__(self):

class PriorityQueueMinIndex:
    def __init__(self):

class PriorityQueueMaxIndex:
    def __init__(self):

class SymbolTable:
    def __init__(self):

class SymbolTableString:
    def __init__(self):

class Set:
    def __init__(self):


########################################
# Sorts
########################################

class Sort:
    @staticmethod
    def insertion_sort(parameter_list):
        pass

    @staticmethod
    def selection_sort(parameter_list):
        pass

    @staticmethod
    def shell_sort(parameter_list):
        pass

    @staticmethod
    def quick_sort(parameter_list):
        pass

    @staticmethod
    def merge_sort(parameter_list):
        pass

    @staticmethod
    def heap_sort(parameter_list):
        pass


########################################
# Searching
########################################

class BinarySearchTree:
    def __init__(self):

class BalancedSearchTree:
    def __init__(self):

class HashTable:
    def __init__(self):


########################################
# Data-Oriented Graph Types
########################################

class Graph:
    def __init__(self):

class DiGraph:
    def __init__(self):

class EdgeGraph:
    def __init__(self):

class EdgeGraphWeighted:
    def __init__(self):

class EdgeDiGraph:
    def __init__(self):

class EdgeDiGraphWeighted:
    def __init__(self):


########################################
# Operations-Oriented Graph Types
########################################

def dynamic_connectivity():
    raise NotImplementedError

def connected_components():
    raise NotImplementedError

def depth_first_search():
    raise NotImplementedError

def breadth_first_search():
    raise NotImplementedError

def kruskal_minimum_spanning_tree():
    raise NotImplementedError

def prim_minimum_spanning_tree():
    raise NotImplementedError

def dijkstra_shortest_path():
    raise NotImplementedError

def bellman_ford_shortest_path():
    raise NotImplementedError


########################################
# Strings
########################################

def sort_string():
    raise NotImplementedError

def try_string():
    raise NotImplementedError

def substring_search():
    raise NotImplementedError

def regex_match():
    raise NotImplementedError

def compress_data():
    raise NotImplementedError


########################################
# Standard I/O Types
########################################

class In:
    def __init__(self, file):
        self.file = file

class Output:
    def __init__(self):

class Draw:
    def __init__(self):


########################################
# Data-Oriented Client Example Types
########################################

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Interval1D:
    def __init__(self):

class Interval2D:
    def __init__(self):

class Date:
    def __init__(self):

class Transaction:
    def __init__(self):


########################################
# Algorithm Analysis Types
########################################

class Counter:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def inc(self):
        self.count = self.count + 1

class Accumulator:
    def __init__(self):

class VisualAccumulator:
    def __init__(self):

class Stopwatch:
    def __init__(self):


########################################
# General Fields of Use
#  * Scientific Computing
#  * Operations Research
#  * Theory of Computing
########################################

def event_based_simulation():
    raise NotImplementedError

def b_tree():
    raise NotImplementedError

def suffix_array():
    raise NotImplementedError

def max_flow():
    raise NotImplementedError
