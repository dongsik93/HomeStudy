import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))

    maxi = {}
    for i in range(len(score)):
        if(score[i] not in maxi):
            maxi[score.count(score[i])] = score[i]
    
    ans = max(maxi)
    print(f"#{tc+1} {maxi[ans]}")