## 34장. 클래스 사용하기

### 클래스 만들기

```python
class 클래스이름:
    def 메서드(self):
        코드
```

```python
class Person:
    def greeting(self):
        print("hello")
```

```python
james = Person()
# james인스턴스 생성
```

### 메서드 호출

- 메서드는 클래스가 아니라 인스턴스를 통해 호출한다

```python
james.greeting()
>>> hello
# 인스턴스를 통해 호툴하는 메서드를 인스턴스 메서드라고 부릅니다
```

### 인스턴스와 객체의 차이점

- 보통 객체만 지칭할 때는 그냥 객체(object)라고 부른다. 하지만 클래스와 연관지어 말할 때는 인스턴스라고 부릅니다

```python
a = list(range(10))
b = list(range(20))
# 리스트 변수 a,b는 객체이며 a와 b는 list클래스의 인스턴스이다
```

### 메서드 안에서 메서드 호출하기

- 메서드 안에서 메서드를 호출할 때는 다음과 같이 self. 메서드() 형식으로 호출한다
- self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이다

```python
class Person():
    def greeting(self):
        print("hello")
        
    def hello(self):
        self.greeting()
    # self.메서드() 형식으로 클래스 안의 메서드를 호출   
james = Person()
james.hello()
```

- 특정 클래스의 인스턴스인지 확인하는 방법은

```python
isinstance(james, Person)
>>> True
```

### 속성 사용하기

- 클래스에서 속성을 만들고 사용하기

```python
class 클래스이름:
    def __init__(self):
        self.속성 = 값
```

- `__innit__`메서드는 클래스에 ()(괄호)를 붙여서 **인스턴스를 만들 때 호출되는 특별한** **메서드** 이다
- __(밑줄 두개)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드인데 스페셜 메서드(매직 메서드)라고 부른다

### self의 의미

- `__init__`의 매개변수 self에 들어가는 값은 Person()이라 할 수 있다. 그리고 self가 완성된 뒤 james에 할당된다. 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어온다.

![img](https://dojang.io/pluginfile.php/13877/mod_page/content/1/034004.png)

### 인스턴스를 만들 때 값 받기

- 인스턴스를 통해 접근하는 속성을 **인스턴스 속성**이라고 한다

```python
class Person():
    def __init__(self, name, age, address):
        # self 다음에 name, age, address를 지정
        self.hello = "hi"
        self.name = name
     # 메서드 안에서는 위와 같이 매개변수를 그대로 self에 넣어서 속성으로 만듬
        self.age = age
        self.address = address
        
    def greeting(self):
        print(f"{self.hello}저는 {self.name}입니다")
        # name속성에 접근하기 위해 self.name으로 사용한다
maria = Person("마리아", 20, "서울시 서초구 반포동")
# 변수에 할당하고 그 내용이 채워져 maria 인스턴스가 만들어짐
# Person의 괄호 안에 넣은 값은 __init__ 메서드에서 self뒤에 있는 매개변수에 차례데로 들어간다
maria.greeting()

print("이름:", maria.name)
print("나이:", maria.age)
print("주소:", maria.address)

>>>
안녕하세요. 저는 마리아 입니다.
이름 : 마리아
나이 : 20
주소 : 서울시 서초구 반포동
```

### `__slots__` 

```python
class Person:
    __slots__ = ["name", "age"]
    # name, age만 허용(다른 속성은 생성 제한)
    # 허용되지 않은 속성은 추가할 떄 에러가 발생
```

### 클래스 위치인수 & 키워드 인수

- 위치 인수

```python
class Person:
    def __init__(self, *args): # 위치 인수
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
 
maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
```

- 키워드 인수

```python
class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
 
maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})
```

### 비공개 속성(private attribute)

- 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있다

```python
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    
        # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000   
# 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
```

### 비공개 메서드

- 속성 뿐 아니라 메서드도 이름이 __(밑줄 두개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 된다
- 보통 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 만든다

```python
class Person:
    def __greeting(self):
        print('Hello')
 
    def hello(self):
        self.__greeting()  
        # 클래스 안에서는 비공개 메서드를 호출할 수 있음
 
james = Person()
james.__greeting()   
# 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음
```



## 35장. 클래스 속성와 정적, 클래스 메서드 사용하기

### 클래스 속성

- 클래스 속성은 클래스에 속해 있으며, 모든 인스턴스에서 공유한다

```python
class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 		# 클래스 속성에 접글 할 때는 클래스 이름으로 접근해야 한다
        # 수정해야되는 코드
        # Person.bag.append(stuff)
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

>>>
["책", "열쇠"]
["책", "열쇠"]
```

### 속성, 메서드 이름을 찾는 순서

- 파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾는다. 그래서 인스턴스 속성이 없으면 클래스 속성을 찾게 되므로 james.bag이 잘 동작한다

![img](https://dojang.io/pluginfile.php/13898/mod_page/content/4/035002.png)

### 인스턴스 속성

- 여러사람이 가방을 공유하지 않으려면 인스턴스 속성으로 만들면 된다

```python
class Person:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)
>>>
["책"]
["열쇠"]
# 인스턴스 속성은 인스턴스별로 독립되어 있으며, 서로 영향을 주지 않는다
```

- **클래스 속성** : 모든 인스턴스가 공유, 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용한다
- **인스턴스 속성** : 인스턴스별로 독립되어 있음, 각 인스턴스가 값을 따로 저장해야 할 때 사용한다

### 정적 메서드

- 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있다
- 보통 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용한다
- 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들 때 사용한다

```python
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출
```

### 클래스 메서드

- 정적 메서드처럼 인스턴스 없이 호출할 수 있다는 점은 같지만, 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용한다
- cls를 사용하면 메서드 안에서 현재 클래스의 인스턴스를 만들 수도 있다

```python
class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1   
        # 인스턴스가 만들어질 때
        # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))   
        # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()   
# 2명 생성


 @classmethod
    def create(cls):
        p = cls()    
        # cls()로 인스턴스 생성
        return p
```



## 36장. 클래스 상속 사용하기

### 상속(inheritance)

- 물려받는 기능을 유지한 채로 다른 기능을 추가할 때 사용하는 기능
- 부모클래스 (슈퍼클래스) - 자식클래스(서브클래스)
- 새로운 기능이 필요할 때마다 계속 클래스를 만든다면 중복되는 부분을 반복해야 하므로, 이런 중복되는 기능을 만들지 않으려고 즉 기존 기능을 **재사용** 할 수 있다

```python
class Person():
    def greeting(self):
        print("hi")
    
class Student(Person):
    def study(self):
        print("study")
        
james = Student()
james.greeting()    
# 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       
# 공부하기: 파생 클래스 Student에 추가한 study 메서드
```

- 상속 관계를 확인하기 위해 issubclass(Student, Person)을 사용한다

### 상속 관계 & 포함 관계

- **상속관계** : 명확하게 같은 종류, 동등한 관계일때 사용, is-a관계라고 부른다. 

- **포함관계** : 상속관계 이외에 속성에 인스턴스를 넣는 방식, has-a관계

```python
# 포함관계의 예
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class PersonList():
    def __init__(self):
        self.person_list = []   
        # 리스트 속성에 Person 인스턴스를 넣어서 관리
 
    def append_person(self, person):   
        # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)
```

### 부모클래스 사용하기 super()

```python
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()               
        # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)
```

![img](https://dojang.io/pluginfile.php/13907/mod_page/content/2/036004.png)

```python
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()   
        # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'
        
# 좀 더 명확하게 super사용하기
```

### 메서드 오버라이딩 사용하기

- 자식클래스에서 부모클래스의 메서드를 새로 정의하는 것

```python
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 		# Person클래스의 greeting메소드를 무시하고 Student 클래스에서 
        # 새로운 greeting메서드를 만듬
james = Student()
james.greeting()
```

- 부모 클래스의 메서드를 재활용 하면 중복을 줄일 수 있기 때문에 , 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용한다

### 다중상속

```python
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
 
james = Undergraduate()
james.greeting()        
# 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    
# 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            
# 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드
```

![img](https://dojang.io/pluginfile.php/13909/mod_page/content/1/036005.png)

### 다이아몬드 상속

```python
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
 
x = D()
x.greeting()    # 안녕하세요. B입니다.
```

![img](https://dojang.io/pluginfile.php/13909/mod_page/content/1/068006.png)

### Object클래스

- object는 모든 클래스의 조상이다.

### 추상 클래스

- 메서드의 목록만 가진 클래스, 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용
- import로 abc모듈을 가져와야 한다

```python
from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
 
class Student(StudentBase):
    def study(self):
        print('공부하기')
 
    def go_to_school(self):
        print('학교가기')
 
james = Student()
james.study()
james.go_to_school()
```

- 추상 클래스는 자식 클래스가 반드시 구현해야 하는 메서드를 정해줄 수 있다
- 추상클래스의 추상 메서드를 모두 구현했는지 확인하는 시점은 자식 클래스가 인스턴스를 만들 때 이다. 따라서 james= Student()에서 확인한다



- 추상 클래스는 인스턴스를 만들 수 없기 때문에 추상 메서드도 호출할 일이 없어 추상메서드를 빈 메서드로 만든다

```python
@abstractmethod
    def study(self):
        pass    
    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
 
    @abstractmethod
    def go_to_school(self):
        pass    
    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
```

- 추상 클래스는 인스턴스로 만들때는 사용하지 않고,  오로지 상속에서만 사용한다



## 37장. 두 점 사이의 거리 구하기

### 피타고라스 정리로 두 점 거리 구하기

![img](https://dojang.io/pluginfile.php/13914/mod_page/content/1/037002.png)