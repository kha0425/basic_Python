# 276p
class USB: # 클래스 생성
    def __init__(self, capacity): # 생성자
        self.capacity = capacity # 인스턴스 변수

    def show_info(self): # 인스턴스 메서드 정의
        print('{}GB USB'.format(self.capacity))

USB1 = USB(64) # 인스턴스(객체) 생성 -> 붕어빵을 구워냈다
USB1.show_info() # 인스턴스 메서드 호출

USB2 = USB(265) # 인스턴스(객체) 생성 -> 붕어빵을 구워냈다
USB2.show_info() # 인스턴스 메서드 호출

# 277p
class Service:
    def __init__(self, service): # 생성자
        self.service = service # 인스턴스 변수
        print(f'{self.service} Service가 시작되었습니다.')
    
    def __del__(self): # 소멸자
        print('{} Service가 종료되었습니다.'.format(self.service))

Service1 = Service('길안내') # 인스턴스 객체 생성 -> 붕어빵 구워냈다.
del Service1 # 인스턴스(객체) 삭제 -> 붕어빵 먹었다!(사라짐)

# 클래스 변수
'''
클래스 안에서 공간이 할당된 변수
여러 인스턴스(객체)가 클래스 변수 공간을 함께 사용
'''

# ex)
class Car: # 클래스 정의
    count = 0 # 클래스 변수 정의(0으로 초깃값을 줬다)

    def __init__(self, name, speed): # 생성자
        self.name = name  # 인스턴스 변수
        self.speed = speed # 인스턴스 변수
        Car.count += 1  # 클래스 변수를 1 증가 시킨다.
    
    def show_info(self):
        print(f'{self.name}의 현재 속도: {self.speed}Km')
        print('생산된 자동차 수 : {}대'.format(Car.count))
        print('---------------------------------')

Car1 = Car('코란도',100) # 인스턴스(객체) 생성 -> 붕어빵 구워냈다
Car2 = Car('코나' ,120)
Car3 = Car('제네시스', 130)

Carlist = [Car1,Car2,Car3]
for car in Carlist:
    car.show_info() # 인스턴스 메서드 호출

class Car: # 클래스 정의
    count = 0 # 클래스 변수 정의(0으로 초깃값을 줬다)
    def __init__(self, name, speed): # 생성자
        self.name = name  # 인스턴스 변수
        self.speed = speed # 인스턴스 변수
    
    def show_info(self):
        print(f'{self.name}의 현재 속도: {self.speed}Km')
      
Car1 = Car('코란도',100) # 인스턴스(객체) 생성 -> 붕어빵 구워냈다
Car2 = Car('코나' ,120)
Car3 = Car('제네시스', 130)

Carlist = [Car1,Car2,Car3]
for car in Carlist:
    car.show_info() # 인스턴스 메서드 호출
    Car.count += 1
    print('생산된 자동차 수 : {}대'.format(Car.count))
    print('---------------------------------')

# 클래스 메소드 - 클래스 변수를 사용하는 메서드, 객체 없이 호출 가능!
# 280p
class Korean: # 클래스 정의
    country = '한국' # 클래스 변수('한국'으로 초기화)
    
    @ classmethod
    def trip(cls, country): # 클래스 메서드 정의
        if cls.country == country: # cls.country: 클래스 변수, country: 매개변수
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

Korean.trip('한국') # 객체 없이 호출 가능(클래스 메서드 특징)
Korean.trip('일본') # 객체 없이 호출 가능(클래스 메서드 특징)

# 282p
class Bag: # 클래스 정의
    count = 0 # 클래스 변수(가방 개수)

    def __init__(self): # 생성자(객체 생성될 때 자동으로 호출되는 함수)
        Bag.count += 1 # 생성자 호출될 때마다 1씩 증가(객체생성시 1씩 증가)
    @classmethod
    def sell(cls): # 클래스 메서드 정의
        cls.count -= 1 # 호출될 때마다 1씩 감소(가방 팔릴때마다 1씩 감소)
    @classmethod
    def remain_bag(cls): # 클래스 메서드 정의
        return cls.count # 가방 개수를 반환함(알려줌)

print(f'현재 가방: {Bag.remain_bag()}개')
Bag1 = Bag() # 인스턴스(객체) 생성(생성자도 실행)
Bag2 = Bag() # 인스턴스(객체) 생성(생성자도 실행)
Bag3 = Bag() # 인스턴스(객체) 생성(생성자도 실행)
print(f'현재 가방: {Bag.remain_bag()}개')
Bag1.sell() # Bag.sell()도 가능
Bag2.sell()
print(f'현재 가방: {Bag.remain_bag()}개')

# 클래스 상속
# 284p
class Person: #슈퍼 클래스(부모 클래스) 생성
    def __init__(self,name): # 생성자 생성
        self.name = name # self.name: 인스턴스 변수, name: 매개변수

    def eat(self,food): # 인스턴스 메서드 정의
        print(f'{self.name}가 {food}를 먹습니다.')

class Student(Person): # 서브 클래스(자식 클래스)
    def __init__(self, name, school): # 생성자 생성
        super().__init__(name) # 슈퍼(부모) 클래스의 생성자를 호출
        self.school = school
    def study(self): # 인스턴스 메서드
        print(f'{self.name}는 {self.school}에서 공부를 합니다.')

Person1 = Student('해리포터','호그와트') # 인스턴스(객체) 생성
Person1.eat('감자') # 상속받은 메서드 호출
Person1.study() # 인스턴스 메서드 호출

# 286p
class Coffee: # 슈퍼 클래스(부모 클래스) 생성
    def __init__(self, bean): # 부모 생성자
        self.bean = bean
    def coffee_info(self): # 인스턴스 메서드 정의
        print('원두: {}'.format(self.bean))

class Espresso(Coffee): # 서브 클래스(자식 클래스)
    def __init__(self, bean, water): # 자식 생성자
        super().__init__(bean) # 부모의 생성자를 호출 
        self.water = water
    def Espresso_info(self): # 자식 인스턴스 메서드
        super().coffee_info() # 부모 클래스의 메서드 호출
        print(f'물 : {self.water}ml')
        print('-----------------------------')

coffee = Espresso('콜롬비아',30) # 인스턴스(객체) 생성
# coffee.Espresso_info() # 인스턴스 메서드 호출

coffee2 = Espresso('케냐',30)
# coffee2.Espresso_info()

coffee3 = Espresso('맥심 모카골드',50)
# coffee3.Espresso_info()

coffee_list = [coffee,coffee2,coffee3]
for coffee in coffee_list:
    coffee.Espresso_info()



