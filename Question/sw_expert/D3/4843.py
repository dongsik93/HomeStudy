import sys

sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    min_idx = 0
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if(num[min_idx] > num[j]):
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]

    num_min = num[0]
    num_max = num[0]
    min_idx = 0
    max_idx = 0
    for i in range(0,n-1):
        min_idx = i
        max_idx = i
        for j in range(i+1, n):
            if(i%2==0):
                if(num[max_idx] < num[j]):
                    max_idx = j
                    num[i] , num[max_idx] = num[max_idx] , num[i]
            else:
                if(num[min_idx] > num[j]):
                    min_idx = j
                    num[i], num[min_idx] = num[min_idx], num[i]
    
    print(f"#{tc+1}", end=" ")
    for i in range(10):
        print(num[i], end=" ")
    print()

