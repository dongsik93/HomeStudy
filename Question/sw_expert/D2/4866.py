import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    word = list(input())
    a = []
    res = 0
    
    for i in word:
        if(i == "(" or i == "{"):
            a.append(i)
        elif(i == ")"):
            if(len(a) == 0):
                res += 1
                break
            elif(a[-1] == "("):
                a.pop(-1)
            else:
                res += 1
                break
        elif(i == "}"):
            if(len(a) == 0):
                res += 1
                break
            elif(a[-1] == "{"):
                a.pop(-1)
            else:
                res += 1
                break
    
    ans = 0
    if(res == 0 and len(a) == 0):
        ans = 1       

    print(f"#{tc+1} {ans}")

    # for i in word:
    #     if(i in a):
    #         s = a.index(i)
    #         a.pop(s)
    # print(a)

