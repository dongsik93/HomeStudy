import sys

sys.stdin = open("input.txt", 'r')

def my_page(start, end, total, page):
    cnt = 0
    c = 0
    while(c != page):
        middle = int( (start + end) / 2 )
        if(page - middle >= 0):
            c = middle
            start = c
            cnt += 1
        elif(page - middle <= 0):
            c = middle
            end = c
            cnt += 1
    return cnt

T = int(input())

for tc in range(T):
    total, pa, pb = map(int, input().split())
    res = 0
    page = [pa, pb]
    start = 1
    end = total
    pa_cnt = my_page(start, end, total, pa)
    pb_cnt = my_page(start, end, total, pb)

    if(pa_cnt > pb_cnt):
        res = "B"
    elif(pa_cnt < pb_cnt):
        res = "A"

    print(f"#{tc+1} {res}")