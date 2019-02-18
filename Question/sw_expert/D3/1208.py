import sys

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    dump = int(input())
    h = list(map(int, input().split()))

    cnt = 0
    while(cnt<dump):
        cnt += 1
        for i in range(len(h)):
            if(max(h) == h[i]):
                h[i] -= 1
                break
        for i in range(len(h)):
            if(min(h) == h[i]):
                h[i] += 1
                break
    
    print(f"#{tc+1} {max(h) - min(h)}")