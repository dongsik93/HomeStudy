T = int(input())

for i in range(T):
    N = int(input())

    num = list(map(int, input().split()))
    num = sorted(num)
    print(f"#{i+1}", end = " ")
    for j in num:
        print(j, end = " ")
    print("")
    