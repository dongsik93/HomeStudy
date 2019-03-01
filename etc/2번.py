def solution(people, tshirts):
    answer = 0
    
    t = {}
    for i in tshirts:
        if(i not in t):
            t[i] = 1
        else:
            t[i] += 1
    
    for i in people:
        for j in t.keys():
            if(i <= j and t[j] != 0):
                answer += 1
                t[j] -= 1
    return answer


people = [1,2,2,2,2]
tshirts = [2,3,4,5,6,7,8]

print(solution(people, tshirts))