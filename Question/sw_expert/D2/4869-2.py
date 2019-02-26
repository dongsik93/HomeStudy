import sys

sys.stdin = open('input.txt', 'r')


# tiling의 대표적인 예
## f(n) = f(n-1) + 2*f(n-2)
### 반복문으로 풀기

T = int(input())

for tc in range(T):
    n = int(input())
    n = int(n/10)
    a = [1,3]
    for i in range(n-2):
        s = a[i]*2 + a[i+1]
        a.append(s)
    print(f"#{tc+1} {a[-1]}")