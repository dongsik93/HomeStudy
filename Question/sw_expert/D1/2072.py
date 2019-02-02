T = int(input())

for i in range(T):
    sum = 0 
    num = map(int, input().split())
    for j in num:
        if(j%2==1):
            sum += j
    print(f"#{i+1} {sum}")
