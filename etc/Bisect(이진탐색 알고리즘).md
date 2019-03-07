### Bisect(이진탐색 알고리즘)

- 일반전익 이진 탐색 알고리즘

```python
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))
# 2
```



- ##### bisect.bisect메소드를 이용

```python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
# bisect.bisect_right == bisect.bisect , 찾고자하는 위치의 오른쪽 인덱스를 반환
print(bisect.bisect(mylist, 3))
## >> 3

# 찾고자 하는 위치의 인덱스를 반환
print(bisect.bisect_left(mylist, 3))
## >> 2
```