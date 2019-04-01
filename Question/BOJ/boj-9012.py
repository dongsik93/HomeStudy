T = int(input())

for tc in range(T):
    arr = list(input())
    stack = []
    try :
        for i in arr:
            if(i == "("):
                stack.append(i)
            elif(i == ")"):
                stack.pop()
        if(len(stack) == 0):
            print("YES")
        else:
            print("NO")
    except:
        print("NO")