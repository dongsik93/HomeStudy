T = int(input())

for tc in range(T):
    test = list(input().split())

    planet = {
        "ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, 
        "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9
    }

    odnum = list(input().split())

    change = []
    for i in odnum:
        change.append(planet[i])
    
    change.sort()

    earth = {
        0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 
        5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"
    }
    print(f"#{tc+1}")
    for i in change:
        print(earth[i], end=" ")