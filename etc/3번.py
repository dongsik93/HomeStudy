def solution(healths, items):
    answer = []
    
    for i in items:
        for j in range(len(healths)):
            if(healths[j] - i[1] >= 100):
                    if(items.index(i)+1 not in answer):
                        answer.append(items.index(i)+1)
    
    
    return answer

healths = [200, 120, 150]
items = [ [30, 100], [500, 30], [100, 400]]


print(solution(healths, items))