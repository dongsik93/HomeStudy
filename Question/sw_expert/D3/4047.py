# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    s = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]
    d = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]
    h = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]
    c = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]

    card = input()
    dec = []
    for i in range(0, len(card), 3):
        dec.append(card[i:i+3])
    print("#{}".format(tc+1), end=" ")

    res = 0
    for i in range(len(dec)):
        if(dec[i][0] == "S"):
            if(dec[i][1] + dec[i][2] in s):
                idx = s.index(dec[i][1] + dec[i][2])
                s.pop(idx)
            else:
                res = "ERROR"
                break
        elif(dec[i][0] == "D"):
            if (dec[i][1] + dec[i][2] in d):
                idx = d.index(dec[i][1] + dec[i][2])
                d.pop(idx)
            else:
                res = "ERROR"
                break
        elif(dec[i][0] == "H"):
            if(dec[i][1] + dec[i][2] in h):
                idx = h.index(dec[i][1] + dec[i][2])
                h.pop(idx)
            else:
                res = "ERROR"
                break
        elif(dec[i][0] == "C"):
            if(dec[i][1] + dec[i][2] in c):
                idx = c.index(dec[i][1] + dec[i][2])
                c.pop(idx)
            else:
                res = "ERROR"
                break

    if(res == "ERROR"):
        print(res)
    else:
        print("{} {} {} {}".format(len(s), len(d), len(h), len(c)))