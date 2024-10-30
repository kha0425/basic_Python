# 가변 매개변수 : 매개변수(입력값)의 개수를 정확히 모를 때 사용
'''
<형식>
def 함수이름(*매개변수명/args): # 함수 정의
    수행할 코드

함수이름(필요한 인수만큼 입력) # 함수 호출
'''
#
# 191p
def adder(*args): # 함수 정의
    print('{}의 합은 {}입니다.'.format(args, sum(args)))

adder(1,2) # 함수 호출
adder(1,2,3)
adder(1,2,3,4)
adder(1,3,5,7,9)

# ex)
def add_mul(choice, *args): # 함수 정의(가변 매개변수를 맨 뒤로 배치)
    if choice == 'add':
        answer = 0 # 합계를 담을 변수 초깃값을 0으로 한다.
        for i in args: # 가변 매개변수 args의 개수만큼 반복
            answer += i
    elif choice == 'mul':
        answer = 1 # 초깃값을 1로 한다.(0으로 하면 계쏙 0이 됨)
        for i in args:
            answer *= i
    return answer # 결과로 나온 answer을 반환한다.

result = add_mul('add',1,2,3) # 1+2+3
print(result)

b = add_mul('mul',4, 5, 6, 7) # 4*8*9*7
print(b)

# 지역 변수 / 전역 변수
'''
지역 변수 : 한정된 지역(함수 안)에서 사용
전역 변수 : 프로그램 전체에서 사용, 예약어 global
'''
# ex)
a = 100 # 전역 변수

def func1(): # 함수 정의
    a = 10  # 지역 변수 (이 함수 안에서만 사용)
    print('func1 함수에서의 a의 값 : {}'.format(a))

def func2(): # 함수 정의
    print('func2 함수에서의 a의 값 : {}'.format(a))

func1() # 함수 호출
func2() # 함수 호출

# ex) 전역 변수의 값을 변경해야 하는 경우
a = 0 # 전역 변수

def f(): # 함수 정의
    global a # 전역 변수 a를 가리킨다.
    a = 10 # 전역 변수 a의 값을 10으로 변경한다.

print('함수 호출 전 a :{}'.format(a))
f() # 함수 호출
print('함수 호출 후 a :{}'.format(a))
def fa():
    print(a)
fa()

# 195p
def coffee_machine(money,pick): # 함수 정의
    print('{}원의 {}를 선택하셨습니다.'.format(money,pick))
    menu = {
        '아메리카노' : 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }
    if pick not in menu: # 메뉴에 없는 음료라면
        print("{}는 판매하지 않습니다.".format(pick))
        return money, '없는 메뉴' # 돈을 다시 돌려준다. 없는 메뉴라는 글자 반환
    elif menu[pick] > money: # 해당 음료의 금액이 부족한 경우
        print(f'{pick}은 {menu[pick]}원입니다.')
        return money, '금액 부족'
    else: # 정상적인 경우
        return money - menu[pick], pick # 음료값을 제외한 잔돈과 음료 이름 반환

order = input('커피를 선택하세요(아메리카노, 카페라떼, 카푸치노)>>> ')
pay = int(input('얼마를 내시나요? >>> '))

change, coffee = coffee_machine(pay,order) # 반환값이 2개이므로 결과변수 2개
print(f'잔돈: {change}원, 커피: {coffee}')

섹션 12 : 모듈과 import

# 모듈을 불려와서 사용하기
'''
<형식>
import 모듈이름 as 별칭 --> as 별칭 생략 가능
또는
from 모듈이름 import 모듈 함수
--> 호출 시 모듈이름을 생략하고 함수만 사용하고 싶을때
from 모듈이름 import *
--> 모듈 안에 있는 모든 함수를 당겨쓸 때 모두의 의미를 가진 *를 사용
'''

# ex) import 방식
import m   # m이라는 모듈(파이썬 파일)을 불러온다.

result1 = m.add(1,2) # m모듈에 있는 add 함수 호출
result2 = m.sub(2,1) # m모듈에 있는 sub 함수 호출
print(f'result1 : {result1}')
print(f'result2 : {result2}')

# ex) from 방식(1)
from m import mul, div # m모듈에 있는 mul,div 함수 가져온다.

result1 = mul(1,2) # from으로 가져올떄는 모듈명이 필요없다.
result2 = div(2,1)

print(f'result1 : {result1}')
print(f'result2 : {result2}')

# ex) from 방식(2)
from m import * # m모듈안에 있는 모든 함수를 가져온다.

x = int(input('x를 입력하세요: '))
y = int(input('y를 입력하세요: '))

n1 = add(x,y)
n2 = sub(x,y)
n3 = mul(x,y)
n4 = div(x,y)

print(n1, n2, n3, n4 , sep = '\n')

# 209p
from my_secure import *
print(secure_name('김철수'))
print(secure_no('951012-1234567'))
print(secure_phone('010-1234-5678'))
##################################################

# 사용자함수 문제)
# 두 개의 정수를 전달받아서 그 두 수의 몫과 나머지를 각각 반환하는 
# 함수를 만들어보자. 이 때 두 개의 정수는 input을 이용해서 입력받는다.
# 반환값 return이 있도록 하고, 함수 이름과 매개변수를 이름 등은 자유롭게 한다.
# 함수 호출은 한번만 한다.
# [화면실행결과]
# 첫번째 수를 입력하세요 : 5
# 두번째 수를 입력하세요 : 2
# 몫 : 2, 나머지 1

# print(divmod(5,2)[0])

x = int(input('첫번째 수를 입력하세요 : '))
y = int(input('두번째 수를 입력하세요 : '))

def div(x,y):
    return divmod(x,y)[0], divmod(x,y)[1]

result1, result2 = div(x,y)
print(f'몫 {result1}, 나머지 {result2}')




