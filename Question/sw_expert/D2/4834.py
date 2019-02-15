T = int(input())

for i in range(T):
    N = int(input())
    a = input()
    ac = []
    for j in a:
        ac.append(j)
    ac.sort(reverse=True)
    total = {}
    for j in ac:
        if(ac.count(j) not in total):
            total[ac.count(j)] = j
    
    total_max = max(total)
    print(f"#{i+1} {total[total_max]} {total_max}")