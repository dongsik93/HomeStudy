T = int(input())

for tc in range(T):
    N = input()

    num = list(range(10))
    k = 0
    my_num = []
    while(len(num) != len(my_num)):
        k += 1
        a = str(int(N) * k)
        for i in range(len(a)):
            if(a[i] not in my_num):
                my_num.append(a[i])
                
    print(f"#{tc+1} {a}")

