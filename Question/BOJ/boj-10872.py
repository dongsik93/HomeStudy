import sys
from math import factorial

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
print(factorial(n))