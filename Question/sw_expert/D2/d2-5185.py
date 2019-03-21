T = int(input())

for tc in range(T):
    n , num = input().split()
    res = []
    for i in num:
        if(i == "A"):
            res.append(format(10,'b'))
        elif(i == "B"):
            res.append(format(11,'b'))
        elif (i == "C"):
            res.append(format(12,'b'))
        elif (i == "D"):
            res.append(format(13,'b'))
        elif (i == "E"):
            res.append(format(14,'b'))
        elif (i == "F"):
            res.append(format(15,'b'))
        else:
            i = int(i)
            if(i > 7):
                res.append(format(i, 'b'))
            elif(i > 3):
                res.append("0")
                res.append(format(i, 'b'))
            elif(i > 1):
                res.append("00")
                res.append(format(i, 'b'))
            else:
                res.append("000")
                res.append(format(i, 'b'))

    print("#{}".format(tc+1), end=" ")
    print(*res, sep="")




