import sys

input = sys.stdin.readline

n = int(input())

a = []
for _ in range(9):
    a.append(int(input()))

print(n-sum(a))
