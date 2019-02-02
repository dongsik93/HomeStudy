T = int(input())

for i in range(T):
    num = map(int, input().split())
    sum = 0
    for j in num:
        sum += j
    avg = round(sum / 10)
    print(f"#{i+1} {avg}")