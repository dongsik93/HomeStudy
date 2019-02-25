import sys

sys.stdin = open("input.txt", 'r')


def fun(n, k):
    if(k == 1):
        return n
    else:
        return n * fun(n, k-1)
    
for tc in range(10):
    a = int(input())
    n, m = map(int, input().split())
    
    print(f"#{tc+1} {fun(n,m)}")
