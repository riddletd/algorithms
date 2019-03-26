#!/usr/bin/env python3

##
# Book Algorithm Examples
##

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


##
# Collections
##

def bag(self, parameter_list):
    raise NotImplementedError


def queue(self, parameter_list):
    raise NotImplementedError


def stack(self, parameter_list):
    raise NotImplementedError


def union_find(self, parameter_list):
    raise NotImplementedError


##
# Sorts
##

def insertion_sort():
    raise NotImplementedError


def selection_sort():
    raise NotImplementedError


def shell_sort():
    raise NotImplementedError


def quick_sort():
    raise NotImplementedError


def merge_sort():
    raise NotImplementedError


def heap_sort():
    raise NotImplementedError


def priority_queues():
    raise NotImplementedError

##
# Searching
##


def symbol_table():
    raise NotImplementedError


def binary_search_tree():
    raise NotImplementedError


def balanced_search_tree():
    raise NotImplementedError


def hash_table():
    raise NotImplementedError


##
# Graphs
##

def undirected_graph():
    raise NotImplementedError


def directed_graph():
    raise NotImplementedError


def depth_first_search():
    raise NotImplementedError


def breadth_first_search():
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


##
# Strings
##

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


##
# General Fields of Use
#  * Scientific Computing
#  * Operations Research
#  * Theory of Computing
##

def event_based_simulation():
    raise NotImplementedError


def b_tree():
    raise NotImplementedError


def suffix_array():
    raise NotImplementedError


def max_flow():
    raise NotImplementedError
