T = int(input())

for tc in range(T):
    n, k = map(int, input().split())
    project = list(map(int, input().split()))

    print(f"#{tc+1}", end=" ")
    for i in range(1,n+1):
        if(i not in project):
            print(i, end=" ")
    print()
