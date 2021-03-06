## 25장. 딕셔너리 응용하기

### key - value값 추가 & 수정 & 삭제

- setdefault : kety-value	쌍으로 추가

```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x.setdefault('f', 100)
x
>>> {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f':100}
# key값만 지정해주면 None을 value로 지정
```

- update : key의 값 수정, key가 없으면 key-value 쌍으로 추가
- update(key=value)는 키가 문자열일때만 사용가능

```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a = 90)
>>> {'a': 90, 'b': 20, 'c': 30, 'd': 40}
x.update(e = 50)
>>> {'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e':50}
```

- update(리스트), update(튜플)은 리스트와 튜플로 값을 수정한다
- 리스트는 [[key1,value1],[key2,value2]]

```python
y = {1:'one', 2:'two'}
y.update(zip([1,2], ['one','two']))
y
>>> {1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}
# key 와 value를 묶은 zip객체로 값을 수정
```

- setdefault 와 update의 차이점
- setdefault는 key-value 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수저할 수 없다
- update는 key-value 쌍 추가와 값 수정이 모두 가능하다



- pop(key)는 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환합니다

```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
x
>>> {'b': 20, 'c': 30, 'd': 40}
# x에서 key'a'를 삭제한 뒤 10을 반환한다
x.pop('z',0)
>>> 0
# 해당 key가 없을 때는 기본값만 반환
```

- del로 특정 key-value 쌍을 삭제한다

```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
x
>>> {'b': 20, 'c': 30, 'd': 40}
```

- 마지막 key-value 쌍 삭제하기 `popitem()`

```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()
('d',40)
x
>>> {'a': 10, 'b': 20, 'c': 30}
```

- 모든 key-value 쌍 삭제하기 `clear()`

```python
x.clear()
```

- key의 값을 가져오기 `get(key)`

```python
x.get('a')
>>> 10
x.get('z',0)
>>> 0
# key가 없을 때는 기본값을 반환
```

- key-value 쌍을 모두 가져오기
- `items()` : key-value 모두 가져옴
- `keys()` : key를 모두 가져옴
- `values()` : value를 모두 가져옴

```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items()
>>> dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
x.keys()
>>> dict_keys(['a', 'b', 'c', 'd'])
x.values()
>>> dict_values([10, 20, 30, 40])
```

### 리스트 / 튜플로 딕셔너리 만들기

-  `dict.fromkeys(keylist)`

```python
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
x
>>> {'a': None, 'b': None, 'c': None, 'd': None}
# 키 리스트로 딕셔너리를 생성하며, 값은 모두 None으로 저장

y = dict.fromkeys(keys, 100)
y
>>> {'a': 100, 'b': 100, 'c': 100, 'd': 100}
# 키 리스트와 값을 지정하면 해당 값이 키의 값으로 저장됨
```

- 현재까지 딕셔너리는 없는 키에 접근했을 경우 에러가 발생, 이때는 defaultdict를사용
- `defaultdict` 는 없는 키에 접근하더라도 에러가 발생하지 않으며, 기본값을 반환

```python
from  collections import defautdict
y = defaultdict(int)
y['z']
>>> 0
# 기본값을 0으로 설정했기 때문에 value가 0으로나옴
```

### 딕셔너리 안에서 딕셔너리 사용하기

- 딕셔너리 = {key1 : {keyA : valueA}, key2 : {keyB : valueB}}

```python
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius']) 
>>> 6051.8
# 딕셔너리[key][key] = value
```

### 할당과 복사

```python
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
# 딕셔너리를 다른 변수에 할당하면 딕셔너리는 두 개가 될 것 같지만 실제로
# 딕셔너리는 한개

x is y
>>> True
# 변수 이름만 다를 뿐 딕셔너리 x와 y는 같은 객체

y = x.copy()
# 이렇게 copy메서드로 해야 완전히 두 개로 만들어짐
```



