T = int(input())

for tc in range(T):
    word = input()
    res = "Exist"
    
    for i in range(1,len(word)//2+1):
        if(word[i-1] != word[-i]):
            if(word[i-1] == "?" or word[-i] == "?"):
                pass
            else:
                res = "Not exist"


    print(f"#{tc+1} {res}")

    