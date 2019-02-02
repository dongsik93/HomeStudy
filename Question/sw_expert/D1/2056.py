T = input()
dic = {
    "01":31,
    "02":28,
    "03":31,
    "04":30,
    "05":31,
    "06":30,
    "07":31,
    "08":31,
    "09":30,
    "10":31,
    "11":30,
    "12":31
}

for i in range(int(T)):
    cal = input().split()
    for j in cal:
        year = j[0:4]
        month = j[4:6]
        day = j[6:8]
        if month not in dic.keys() :
            print(f"#{i+1} -1")
        elif(dic[month] < int(day)):
            print(f"#{i+1} -1")
        else:
            print(f"#{i+1} {year}/{month}/{day}")
