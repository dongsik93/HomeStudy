N = int(input())

a = str.maketrans("369","---")
for i in range(1, N+1):
    s = str(i).translate(a)
    print(s, end = " ")
     