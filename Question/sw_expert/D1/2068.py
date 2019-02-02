T = int(input())

for i in range(T):
    num = map(int, input().split())
    max = 0
    for j in num:
        if(j > max):
            max = j
    print(f"#{i+1} {max}")

