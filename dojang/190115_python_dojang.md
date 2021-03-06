## 26장. 세트 사용하기

### 세트(set)

- 세트 = {값1, 값2, 값3}

- 세트는 요소의 순서가 정해져 있지 않다. 따라서 세트를 출력해 보면 매번 요소의 순서가 다르게 나온다

```python
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
'orange' in fruits
>>> True
'peach' in fruits
>>> False
# 세트에 특정 값이 있는지 없는지 확인하기
```

### set을 사용해서 만들기

```python
a = set('apple')
a
>>> {'e','l','a','p'}
# set는 중복 문자는 포함되지 않는다
b = {}
# 비어있는 set를 이렇게 만들면 빈 딕셔너리가 만들어진다
c = set()
# 이렇게 만들어야 빈 set가 만들어짐
```

### 집합연산

- | 연산자는 합집합을 구하며, or연산자 |를 사용한다
- 세트1 | 세트2
- set.union(세트1, 세트2)

```python
a = {1,2,3,4}
b = {3,4,5,6}
a | b
>>> {1,2,3,4,5,6}
```

- &연산자는 교집합을 구하며 and연산자 &를 사용한다
- 세트1 & 세트2
- set.intersection(세트1, 세트2)

```python
a & b
>>> {3,4}
```

- -연산자는 차집합을 구하며 뺄셈연산자 -를 사용한다
- 세트1 - 세트2
- set.difference(세트1,세트2)

```python
a - b
>>> {1,2}
```

- ^연산자는 대칭차집합을 구하며 xor연산자 ^를 사용한다
- 세트1 ^ 세트2
- set.symmetric_difference(세트1, 세트2)

```python
a ^ b
>>> {1,2,5,6}
```

### 할당연산자

- |= 는 현재 세트에 다른 세트를 더하며 update메서드와 같다

```python
a = {1,2,3,4}
a |= {5}
>>> {1,2,3,4,5}
# a.update({5})와 같다
```

- &= 는 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장한다

```python
a = {1,2,3,4}
a &= {0,1,2,3,4}
>>> {1,2,3,4}
# a.intersection_update({0,1,2,3,4})와 같다
```

- -=는 현재 세트에서 다른 세트를 뺀다

```python
a = {1,2,3,4}
a -= {3}
>>> {1,2,4}
# a.difference_update({3})과 같다
```

- ^=는 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장한다

```python
a = {1,2,3,4}
a ^= {3,4,5,6}
>>> {1,2,5,6}
# a.symmetric_Difference_update({3,4,5,6})과 같다
```

- <=는 현재세트가 다른세트의 부분집합인지 확인한다

```python
a = {1,2,3,4}
a <={1,2,3,4}
>>> True
# a.issubset({1,2,3,4})와 같다
```

### 세트 조작하기

```python
a.add(5)
# 요소 추가

a.remove(3)
# 요소 삭제 없으면 에러발생

a.discard(3)
# 요소 삭제 없으면 그냥 넘어감

a.pop()
# 임의의 요소 삭제
```



## 27장. 파일 사용하기

### 파일에 문자열 쓰기

```python
file = open("hello.txt", "w")
# hello.txt 파일을 쓰기모드(w)로 열기. 파일 객체 반환
file.write("hello, world!")
# 파일에 문자열 저장
file.close()
# 파일 객체 닫기
```

### 파일에서 문자열 읽기

```python
file = open("hello.txt","r")
s = file.read()
# 파일에서 문자열 읽기
```

### 자동으로 파일 객체 닫기

```python
with open("hello.txt", "r") as file:
    s = file.read()
    print(s)
    
# close를 사용하지 않아도 파일 객체를 자동으로 닫아줌
```

- 파일에 여러줄을 저장할 때 `\n` 개행 문자를 지정해주어야 줄바꿈이 된다. 붙이지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의



## 28장. 회문 판별과 N-gram만들기

### 회문 판별

- 회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 말한다
- for문으로 

```python
word = input("단어 입력")

is_palindrome = True				# 회문 판별값 저장 변수
for i range(len(word) // 2): 		# 0~문자열 길이의 절반만큼 반복
    if(word[i] != word[-1-i]):		# 왼쪽 오른쪽 문자를 비교해 다르면
        is_palindrom = False
        break
        
print(is_palindrom)
```

- 시퀀스 뒤집기로

```python
word = input("")

print(word == word[::-1])
# 원래 문자열과 반대로 뒤집은 문자열을 비교
```

- 리스트와 reversed로

```python
word = "level"
list(word) == list(reversed(word))
>>> True
```

- 문자열 join메서드와 reversed로

```python
word = "level"
word == "".join(reversed(word))
>>> True
```

### N-gram 만들기

- n-gramd은 문자열에서 n개의 연속된 요소를 추출하는 방법

2-gram이면 He / el / ll / lo처럼 2글자 추출

- for 문으로

```python
# 2-gram
text = "hello"

for i in range(len(text) -1):
    print(text[i], text[i+1], sep="")
```

- zip으로

```python
text = "hello"

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep="")

# zip함수는 반복 가능한 객체의 각 요소를 튜플로 묶어준다
```

