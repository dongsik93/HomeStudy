재귀호출 & 탐욕법
# 메모리 줄임
## 시간복잡도 O(nlogn)
def continueMaxSum(arr, start, end):
    # 구간의 길이가 1일 경우    
    if(arr[start] == arr[end]):
        return arr[start]
    
    mid = int((start + end) / 2)

    left, right = max(arr),max(arr)
    # 왼쪽
    sum = 0
    for i in range(end, mid, -1):
        sum += arr[i]
        left = max(left, sum)
    
    # 오른쪽
    sum = 0
    for i in range(start, mid+1):
        sum += arr[i]
        right = max(right, sum)
    #최대 구간이 두 조각중 하나에만 속해 있는 경우의 답을 재귀호출로 찾음
    single = max(continueMaxSum(arr, start, mid), continueMaxSum(arr, start, mid))
    #두 경우 최대치를 반환
    return max(left,right, single)

T = int(input())

for tc in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    res = continueMaxSum(nums, 0, n-1)


    print(f"#{tc+1} {res}")
