### 점화식 : maxAt(i) = max(0, maxAt(i-1)) + arr[i]
### arr[i]를 오른쪽 끝으로 갖는 구간의 최대합을 반환하는 함수
### arr[i]에서 끝나는 최대 합 부분 구간은 항상 arr[i] 하나만으로 구성되어 있거나,
### arr[i-1]를 오른쪽 끝으로 갖는 최대 합 부분 구간의 오른쪽에 arr[i]를 붙인 형태
def maxsum(arr):
    n = len(arr)
    ret = max(arr)
    sum = 0
    for i in range(n):
        sum = max(sum, 0) + arr[i]
        ret = max(sum, ret)
    
    return ret

T = int(input())

for tc in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    res = maxsum(nums)


    print(f"#{tc+1} {res}")
