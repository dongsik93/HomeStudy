def isprime(m):
    a = [False, False] + [True]*(m-1)
    for i in range(2, m+1):
        if a[i]:
            prime.append(i)
            for j in range(2*i, m+1, i):
                a[j] = False



n,m = map(int, input().split())
prime = []
isprime(m)
for i in prime:
    if(i >= n):
        print(i)