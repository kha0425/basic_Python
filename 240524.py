# p64
# ex) input의 형변환
a = input('입력 : ')
print('변수 a의 값 : {}'.format(a))
print('변수 a의 자료형(type): {}'.format(type(a)))
print()

b = int(input('입력 : '))
print('변수 b의 값 : {}'.format(b))
print('변수 b의 자료형(type): {}'.format(type(b)))

# ex) 더하기 계산의 차이
s1 = input('입력 s1: ') # 문자열로 입력됨
s2 = input('입력 s2: ')
print('s1+s2={}'.format(s1+s2)) # 문자열이니까 이어붙임(연결)
print('s1+s2의 type은 {}'.format(type(s1+s2)))
print()

i1 = int(input('입력 i1: ')) # 정수형으로 형변환
i2 = int(input('입력 i2: ')) 
print('i1+i2 = {}'.format(i1+i2)) # 정수형이니까 더하기 계산
print('i1+i2의 type은 {}'.format(type(i1+i2)))

# ex) 실수형으로 입력받기
num1 = float(input('실수로 된 첫번째 숫자: '))
num2 = float(input('실수로 된 두번째 숫자: '))
print('덧셈 결과 : {}'.format(num1+num2))
print('뺄셈 결과 : {}'.format(num1-num2))

# p65
price = 50000 # 물건값
n = int(input('할부 개월 입력 >>> '))
print('매달 내는 돈은 {}입니다.'.format(price/n)) # 파이썬의 나누기는 실수형으로 출력됨

# 섹션 4 : 연산자
# 산술 연산자
# p73
a = 7
b = 2
print('{}+{}={}'.format(a,b,a+b))
print('{}-{}={}'.format(a,b,a-b))
print('{}*{}={}'.format(a,b,a*b))
print('{}**{}={}'.format(a,b,a**b)) # 거듭제곱
print('{}/{}={}'.format(a,b,a/b))   # 나누기 -> 결과가 실수형
print('{}//{}={}'.format(a,b,a//b)) # 몫
print('{}%{}={}'.format(a,b,a%b))   # 나머지

# 복합 대입 연산자
# ex) a가 10에서 시작해서 코드가 진행될수록 값이 변하도록 해보기
a = 10
print('a의 값: {}'.format(a))

a += 5 # a = a + 5
print('a의 값: {}'.format(a))

a -= 5 # a = a - 5
print('a의 값: {}'.format(a))

a *= 5 # a = a * 5
print('a의 값: {}'.format(a))

a /= 5 # a = a / 5
print('a의 값: {}'.format(a)) # 결과가 실수형

a %= 5 # a = a % 5
print('a의 값: {}'.format(a))

p76
piggy_bank = 0 # 저금통

money = 10000
piggy_bank += money # piggy_bank = piggy_bank + money
print('저금통의 용돈 {}원을 넣었습니다.'.format(money))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))

snack = 2000
piggy_bank -= snack # piggy_bank = piggy_bank - snack
print('저금통에서 스낵구입비 {}원을 뺐습니다.'.format(snack))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))


# 관계 연산자
# p 78
a = 15
print('{} > 10 : {}'.format(a,a>10))
print('{} < 10 : {}'.format(a,a<10))
print('{} >= 10 : {}'.format(a,a>=10))
print('{} <= 10 : {}'.format(a,a<=10))
print('{} == 10 : {}'.format(a,a==10))
print('{} != 10 : {}'.format(a,a!=10))

# 논리 연산자
# p79
a = 10 # True(참)
b = 0  # False(거짓)
print('{} > 0 and {} > 0 : {}'.format(a,b, a>0 and b>0))
print('{} > 0 or {} > 0 : {}'.format(a,b, a>0 or b>0))
print('not {} : {}'.format(a,not a))
print('not {} : {}'.format(b,not b))

# 비트 연산자
# p82
a = 10 # 00001010(2진수,보통 8비트가 1바이트이기 때문)
b = 70 # 01000110(2진수)

print('a & b : {}'.format(a&b)) # 00000010(둘다 1일 때만 1)
print('a | b : {}'.format(a|b)) # 01001110(둘 중에 하나만 1이여도 1)
print('a ^ b : {}'.format(a^b)) # 01001100(서로 다를 경우 1)
print('~a : {}'.format(~a))     # 11110101(0과 1을 반대로)
print('a << 1 : {}'.format(a << 1))  # 00010100(왼쪽 shift 연산자: 1을 왼쪽으로 한칸씩 이동후 0을로 채움)
print('a >> 1 : {}'.format(a >> 1))  # 00100101(오른쪽 shift 연산자: 1을 오른쪽으로 한칸씩 이동후 0을로 채움)

a, b = map(int,input('숫자 2개: ').split(','))
print(a+b)

# 시퀀스 연산자
# 시퀀스 자료형 : 순서가 있는 자료형(리스트, 튜플,range,문자열 등)
# p83
tree = '#'
space = ' '
print(space*4 + tree*1)
print(space*3 + tree*3)
print(space*2 + tree*5)
print(space*1 + tree*7)
print(space*0 + tree*9)

# 멤버십 연산자 : in 연산자
# ex)
print('안녕' in '안녕하세요') # 포함되어 있다.
print('메롱' in '안녕하세요') # 포함되어 있지 않다.

print('안녕' not in '안녕하세요') 
print('메롱' not in '안녕하세요') 

# 조건 연산자(삼항 연산자)
# 참 if 조건식 else 거짓
a = 10
b = 20
result = a - b if a >= b else b - a
print('{}와 {}의 차이는 {}입니다.'.format(a,b,result))

# 섹션 5 : 조건문
# if
# ex)
a = 99
if a < 100:
    print('100보다 작군요!') # 참일 때만 출력

print()

num = int(input('정수를 입력하세요: '))
if num > 0:
    print('양수입니다.')
if num == 0:
    print('0입니다.')
if num < 0:
    print('음수입니다.')

# if - else
# 95p
age = int(input('몇 살입니까? >>> '))
if age >= 20:
    print('성인') # 참일 경우
else:
    print('미성년자') # 거짓일 경우

#########################################################
# input 문제
# 1) 정수 변수 2개를 만들어 숫자를 입력받는다. input 함수
# 아래의 출력결과처럼 나오게 해보자.
# [화면실행결과]
# 첫번째 정수는? 13
# 두번재 정수는? 5
# 나눗셈의 몫은 2 나머지는 3입니다.
a = int(input('첫번째 정수는? '))
b = int(input('두번째 정수는? '))
print(f'나눗셈의 몫은 {a//b}, 나머지는 {a%b}입니다')

a,b = map(int,input('정수 2개를 입력하세요: ').split())
print(f'첫번째 정수는: {a}')
print(f'두번째 정수는: {b}')
print(f'나눗셈의 몫은 {a//b}, 나머지는 {a%b}입니다')


