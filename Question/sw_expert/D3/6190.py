T = int(input())

for tc in range(T):
    n = int(input())
    word = list(map(int, input().split()))
    word.sort()
    res = []
    for i in range(n-1):
        for j in range(1+i, n):
            s = str(word[i] * word[j])
            if(len(s) <= 1):
                res.append(int(s))
            else:
                a = 0
                for k in range(1,len(s)):
                    if(s[k-1] > s[k]):
                        a = 1
                        break
                if(a == 0):
                    res.append(int(s))
    ans = -1
    if(len(res) != 0):
        ans = max(res)

    print("#{} {}".format(tc+1, ans))
