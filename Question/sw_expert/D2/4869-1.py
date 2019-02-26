import sys

sys.stdin = open('input.txt', 'r')


# tiling의 대표적인 예
## f(n) = f(n-1) + 2*f(n-2)
### 재귀로풀기
def paper(n):
    if(n == 10):
        return n
    elif(n == 20):
        n = 30
        return n
    else:
        return paper(n-10) + paper(n-20)*2

T = int(input())

for tc in range(T):
    n = int(input())
    cnt = 0
    print(f"#{tc+1} {int(paper(n)/10)}")

