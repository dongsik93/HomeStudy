import sys

input = sys.stdin.readline

def prime(n, k):
    a = [False, False] + [True]*(n-1)
    cnt = 0
    for i in range(2,n+1):
        if(a[i]):
            a[i] = True
            for j in range(i, n+1, i):
                if(a[j] == True):
                    a[j] = False
                    cnt += 1
                    if(cnt == k):
                        return j
n, k = map(int, input().split())
print(prime(n, k))