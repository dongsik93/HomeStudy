T = int(input())

for i in range(T):
    num = input().split()
    for j in range(1,len(num)):
        if(num[j-1] == num[j]):
            a = "="
        elif(num[j-1] < num[j]):
            a = "<"
        else:
            a = ">"
    print(f"#{i+1} {a}")
        