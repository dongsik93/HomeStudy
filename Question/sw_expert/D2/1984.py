T = int(input())

for i in range(T):
    nums = list(map(int,input().split()))
    min = nums[0]
    max = 0
    sum = 0
    for j in range(len(nums)):
        if(nums[j] > max):
            max = nums[j]
        if(nums[j] < min):
            min = nums[j]
        sum += nums[j]
    ans =round( (sum - min - max) / (len(nums)-2))
    print(f"#{i+1} {ans}")