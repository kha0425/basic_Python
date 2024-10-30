# ex) 문자열을 판단하는 if-esle
string = 'python'

id = input('아이디를 입력하세요 : ')
if id == string:
    print('환영합니다.') # 참
else:
    print('ID를 찾을 수 없습니다!') # 거짓

# ex) 값을 입력받아 짝수, 홀수 구분하기
num = int(input('정수를 입력하세요 : '))
if num % 2 == 0:
    print('짝수 입니다.')
else:
    print('홀수 입니다.')

# ex) 값을 입력받아 in연산자를 활용하여 짝수, 홀수 구분하기
num = input('정수를 입력하세요: ') # 문자열 형식으로 입력받을 것
a = num[-1]
if a in ['0','2','4','6','8']:
    print('짝수 입니다.')
else:
    print('홀수 입니다.')

# p 96
# if-elif
# ex)
num = int(input('정수를 입력하세요: '))
if num > 0:
    print('양수 입니다.')
elif num == 0:
    print('0입니다.')
else:
    print('음수입니다.')

# p 98
age = int(input('몇 살입니까? >> '))
if age < 8:
    print('미취학 아동입니다.')
elif age <= 13:
    print('초등학생입니다.')
elif age <= 16:
    print('중학생입니다.')
elif age <= 19:
    print('고등학생입니다.')
else:
    print('성인입니다.')

# p 102 
# 섹션 6 : 반복문
'''
<형식 : 조건문으로 판단하는 경우>
while 조건식:
    이 부분을 반복 # 참이면

< 형식 : 반복횟수가 정해진 경우>
변수 = 시작값
while 변수 < 끝값:
    변수 += 증감값
    추가적인 코드들~
'''

# ex) 100번 출력
i = 0
while i < 100:
    print('Hello, world: {}'.format(i))
    i += 1

# p 105
n = 10 # 시작값(초기식)
while n >= 1:
    print(n)
    n -= 1

# ex) 무한 반복
while True:
    print('ㅋ', end = '')

# ex) while을 이용해서 숫자로 데미지를 입힌 후 체력이 0이 되면 종료하기
hp = 100
while hp > 0:
    print(f'주인공의 체력은 {hp}입니다.')
    damage = int(input('얼마의 데미지를 입히겠습니까? : '))
    hp -= damage
print('주인공의 체력은 0이 되어 종료합니다.')

# p 107
my_list = []
n = int(input('정수를 입력하세요 (종료는 0입니다.)>>> '))
while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요 (종료는 0입니다.)>>> '))
print(my_list)

# while문의 중첩
# p 108
day = 1
while day < 6:
    study = 1
    while study < 4:
        print(f'{day}일차 {study}교시입니다.')
        study += 1
    day += 1

day = 1
study = 1 # 변수가 밖에 있으면 초기화 되지 않고 study가 4가 되어서 종료 됨.
while day < 6:
    while study < 4:
        print(f'{day}일차 {study}교시입니다.')
        study += 1
    day += 1

# p 110
i = 2
while i < 10:
    print(f'-----------{i}단------------')
    j = 1
    while j < 10:
        print(f'{i}*{j}={i*j}', end = ' ')
        j += 1
    print(',')
    print()
    i += 1

# if 문제)
# 1) 변수 n에 정수를 입력받는다. (input 함수 이용)
# 입력받은 정수가 10보다 크면 '10보다 크다.', 10보다 작으면 '10보다 작다.'
# 10과 같으면 '10과 같다.'라고 출력해 보시오
# [화면 실행결과]
# 정수를 입력하시오 : 10 
# 10과 같다.

n = int(input('정수를 입력하시오 : '))
if n > 10:
    print('10보다 크다')
elif n < 10:
    print('10보다 작다')
else:
    print('10과 같다.')

# 2) if 과제
# 한 점을 구성하는 (x,y) 좌표를 입력받고, 이 점이 (50,40), (50,80),
# (100,40), (100,80)을 꼭짓점으로 갖는 사각형 안에 있는지
# 판별하는 프로그램을 작성하시오.
# (선 위에 점이 있는 것은 포함하지 않는 것으로 한다.)
# [화면실행결과]
# x좌표를 입력하시오 : 60
# y좌표를 입력하시오 : 100
# 사각형 안에 없습니다.
x = int(input('x좌표를 입력하시오 : '))
y = int(input('y좌표를 입력하시오 : '))

if 50 < x <100 and 40 < y <80:
    print('사각형 안에 있습니다.')
else:
    print('사각형 안에 없습니다.') 
