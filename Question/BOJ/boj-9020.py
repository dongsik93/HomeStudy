def isprime(n):
    a = [False, False] + [True] * (n-1)
    prime = []
    for i in range(2, n+1):
        if a[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return prime

prime = isprime(10000)

T = int(input())

for tc in range(T):
    n = int(input())
    a, b = int(n/2), int(n/2)
    while(True):
        if((a in prime) and (b in prime)):
            break
        a -= 1
        b += 1
    print(a,b)
