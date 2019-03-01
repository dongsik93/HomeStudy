import time
start_time = time.time()

def solution(n):
    answer = 0
    
    a = [False, False] + [True]*(n-1)
    primes = []
    
    for i in range(2,n+1):
        if(a[i]):
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    for i in range(2**len(primes)):
        ss = []
        for j in range(len(primes)):
            if(i & (1 << j) != 0):
                ss.append(primes[j])
        if(sum(ss) == n and len(ss)==3):
            answer += 1
    return answer
            
n = int(input())
print(solution(n))

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time ))
