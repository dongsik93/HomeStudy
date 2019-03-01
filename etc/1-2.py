def solution(n):
    answer = 0
    
    a = [False, False] + [True]*(n-1)
    primes = []
    
    for i in range(2,n+1):
        if(a[i]):
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    s = []
    for i in range(len(primes)):
        for j in range(1,len(primes)):
            for k in range(2,len(primes)):
                if(primes[i] + primes[j] + primes[k] == n and primes[i] != primes[j] and primes[j] != primes[k]):
                    print(primes[i] , primes[j] , primes[k])

n = int(input())
print(solution(n))


a = set(1,2,3)
b = set(3,2,1)
print(a == b)