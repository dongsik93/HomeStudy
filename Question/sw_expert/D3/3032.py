import sys

sys.stdin = open("input.txt", "r")

def gcd(a, b): 
    r = [a, b] 
    s = [1, 0] 
    t = [0, 1]
    while r[-1] != 0:
        q = int(r[-2] / r[-1]) 
        r.append(r[-2] - q * r[-1]) 
        s.append(s[-2] - q * s[-1]) 
        t.append(t[-2] - q * t[-1]) 
    return s[-2], t[-2]


T = int(input())

res = []
for _ in range(T):
    a, b = map(int, input().split())
    res.append(gcd(a, b))

for i in range(T):
    print(f"#{i+1}", end=" ")
    for j in range(2):
        print(f"{res[i][j]}", end=" ")
    print()