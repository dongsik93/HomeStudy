# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# res = []
# for i in range(2**len(a)):
#     s = 0
#     for j in range(n):
#         if(i & (1 << j) != 0):
#             s += a[j]
#     if(s <= m):
#         res.append(s)
#
# print(max(res))

# from itertools import combinations
# import sys
#
# N, S = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))
#
# res = []
# for i in range(1, N+1):
#     boxs = combinations(num, i)
#     for box in boxs:
#         if(sum(box) <= S):
#             res.append(sum(box))
# print(max(res))

#
#
#
# from itertools import combinations
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
#
# res = 0
# for i in list(combinations(a,3)):
#     print(i)
#     if(max(i) <= m):
#         if(sum(i) == m):
#             res = sum(i)
#             break
#         elif(sum(i) < m):
#             res = sum(i)
# print(res)
#


from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = 0
maxs = 0
for i in list(combinations(a,3)):
    s = sum(i)
    if(m >= s > maxs):
        maxs = s

print(maxs)

