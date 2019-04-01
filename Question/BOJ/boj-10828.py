T = int(input())

stack =[]
for tc in range(T):
    a = list(input().split())
    if(a[0] == 'push'):
        stack.append(a[1])
    elif(a[0] == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
    elif(a[0] == 'size'):
        print(len(stack))
    elif(a[0] == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(a[0] == 'pop'):
        if(len(stack) == 0):
            print(-1)
        else:
            s = stack.pop(-1)
            print(s)