## 20장. FizzBuzz 문제

```python
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리
```

## 21장. 별그리기



## 22장. 리스트와 튜플 응용하기

### 리스트 조작하기

`append`  : 요소 하나를 추가

```python
a = [1,2,3,4]
a.append(5)
>>> [1,2,3,4,5]
# 이처럼 리스트 끝에 요소 하나를 추가
a = []
a.append(10)
# 빈 리스트에 값을 추가 할 수 있다
```

`extend`  : 리스트를 연결하여 확장

```python
a = [10, 20, 30]
a.extend([500, 600])
>>>[10, 20, 30, 500, 600]
# 리스트 끝에 다른 리스트를 연결해 리스트를 확장
```

`insert`  : 특정 인덱스에 요소 추가

```python
a = [10, 20, 30]
a.insert(2, 500)
>>>[10, 20, 500, 30]
# 원하는 위치에 요소를 추가
a.insert(0,500)
# 맨 처음에 요소 추가
a.insert(len(a),500)
# 맨 마지막에 요소 추가
# a.append(500)과 같은 결과
a[1:1] = [500,600]
# 인덱스 슬라이스를 이용해 리스트 중간에 요소 여러개를 할당 가능하다
# [1:1] 은 1위치에 
```

### 리스트 요소 삭제하기

`pop`   :  마지막 요소 또는 특정 인덱스의 요소를 삭제

```python
a = [1,2,3,4,5]
a.pop()
# 맨 마지막 요소 삭제
a.pop(1)
# 인덱스 1 삭제
del a[1] #같은 결과
```

`remove`   : 특정 값을 찾아서 삭제

```python
a.remove(2)
# 같은 값이 여러 개 있을 경우 처음 찾은 값을 삭제
```

### 특정 값의 인덱스 & 개수 구하기

```python
a = [1,2,3,4,5,2]
a.index(2)
# 인덱스
a.count(2)
# 개수 구하기
```

### 순서 뒤집기 & 요소 정렬하기

```python
a.reverse()
# 뒤집기
a.sort()
# 오름차순 정렬
```

### sort 매서드와 sorted함수

- sort는 매서드를 사용한 리스트를 변경
- sorted 함수는 정렬된 새 리스트를 생성

```python
a = [10,20,30,15,20,40]
a.sort()
# a의 내용을 변경하여 정렬
a
>>> [10, 15, 20, 20, 30, 40]

b = [10,20,30,15,20,40]
sorted(b)
>>> [10, 15, 20, 20, 30, 40]
# 정렬된 새 리스트를 생성
```

### 모든 요소 삭제 & 슬라이스 조작

```python
a.clear()
# 모든 요소삭제
del a[:]
# 모든 요소 삭제

a[-1]
# 마지막 요소 접근
```



### 리스트로 스택 & 큐만들기

`리스트로 스택 만들기`

![img](https://dojang.io/pluginfile.php/13694/mod_page/content/4/022007.png)

`리스트로 큐 만들기`

![img](https://dojang.io/pluginfile.php/13694/mod_page/content/4/022008.png)

- python에서 스택은 리스트로 활용해도 되지만 큐는 효율적으로 하기위해 덱 사용

### 덱(deque, double ended queue)

- 양쪽 끝에서 추가/ 삭제가 가능한 자료구조

```python
from collections import deque    
# collections 모듈에서 deque를 가져옴
>>> a = deque([10, 20, 30])
>>> a
deque([10, 20, 30])
>>> a.append(500)    # 덱의 오른쪽에 500 추가
>>> a
deque([10, 20, 30, 500])
>>> a.popleft()     # 덱의 왼쪽 요소 하나 삭제
10
>>> a
deque([20, 30, 500])
```

- deque의 append는 덱의 오른쪽에 요소를 추가하고, popleft는 덱의 왼쪽 요소를 삭제한다. 반대로 appendleft는 덱의 왼쪽에 요소를 추가하고, pop으로 덱의 오른쪽 요소를 삭제할 수도 있다



### 리스트의 할당과 복사

```python
a = [0,0,0,0,0]
b = a
```

![img](https://dojang.io/pluginfile.php/13695/mod_page/content/1/022012.png)

- 변수 이름만 다를 뿐 리스트 a와 b는 같은 객체
- a와 b가 같으므로

```python
b[2] = 99
print(a[2])
>>> 99
```

- 완전히 두개로 만드려면

```python
a = [0,0,0,0,0]
b = a.copy()
# copy를 사용한 뒤 b에 할당해주면 a의 요소가 모두 b에 복사됨
```

![img](https://dojang.io/pluginfile.php/13695/mod_page/content/1/022014.png)

- a와 b는 별개의 객체



### enumerate()

- 인덱스와 요소를 함께 출력



### list comprehension(리스트 표현식,축약)

- [식 for 변수 in 리스트]
- list[식 for 변수 in 리스트]

```python
a = [i for i in range(10)]       
# 0부터 9까지 숫자를 생성하여 리스트 생성
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = list(i for i in range(10))  
 # 0부터 9까지 숫자를 생성하여 리스트 생성
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

![img](https://dojang.io/pluginfile.php/13698/mod_page/content/1/022016.png)

- [식 for 변수 in 리스트 if 조건식]
- list(식 for 변수 in 리스트 if 조건식)

```python
>>> a = [i for i in range(10) if i % 2 == 0]    
# 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성
>>> a
[0, 2, 4, 6, 8]
```

![img](https://dojang.io/pluginfile.php/13698/mod_page/content/1/022017.png)



- 다중 포문

![img](https://dojang.io/pluginfile.php/13698/mod_page/content/1/022018.png)



### map()

- 리스트의 요소를 지정된 함수로 처리해주는 함수
- 원본 리스트를 변경하지 않고 새 리스트를 생성

- list(map(함수, 리스트))
- tuple(map(함수, 튜플))

```python
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
>>>[1, 2, 3, 4]

a = map(int,input().split())
# 입력 결과를 map을 사용해 정수르 변환
```

