T = int(input())

for tc in range(T):
    N = int(input())
    word = []
    for n in range(N):
        word.append(list(input().split()))
    
    a = []
    for i in range(N):
       a.append(word[i][0] * int(word[i][1]))
    
    print(f"#{tc+1}")

    sum = "".join(a)
    cnt = 0
    for i in sum:
        cnt += 1
        print(i, end="")
        if(cnt == 10):
            print("")
            cnt = 0
    print("")