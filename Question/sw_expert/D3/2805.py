import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
ans = []
for tc  in range(T):
    n = int(input())

    farm  = []
    for i in range(n):
        a = list(input())
        a = [int(j) for j in a]
        farm.append(a)

    res = 0
    mid = int(n/2)
    for i in range(n):
        for j in range(n):
            if(j == mid):
                res += farm[i][j]
            elif(i == mid):
                res += farm[i][j]
    #1
    for i in range(mid):    
        for j in range(mid):        
            if(i+j>=mid):
                res += farm[i][j]
    #2
    for i in range(mid):
        for j in range(n-1,mid,-1):
            if(j-i <= mid):
                res += farm[i][j]
    #3
    for i in range(n-1,mid,-1):
        for j in range(mid):
            if(i-j <= mid):
                res += farm[i][j]
    #4
    for i in range(n-1,mid,-1):
        for j in range(n-1,mid,-1):
            if(i+j <= mid*3):
                res += farm[i][j]
    ans.append(res)

for i in range(T):
    print(f"#{i+1} {ans[i]}")
