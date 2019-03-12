import sys

input = sys.stdin.readline

def prime(k):
    a = [False, False] + [True]*(k-1)
    primes = []

    for i in range(2, k+1):
        if(a[i]):
            primes.append(i)
            for j in range(2*i, k+1, i):
                a[j] = False

    return primes

while(True):
    n = int(input())
    if(n == 0):
        break
    aa = prime(2*n)
    cnt = 0
    for i in aa:
        if(n<i<=2*n):
            cnt += 1
    print(cnt)