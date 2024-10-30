# p116
# 섹션 7 : 반복문
# for
'''
반복 횟수가 정해져 있을 때 사용

<형식>
for 변수명 in 리스트명:
    반복할 코드

for 변수명 in range(횟수): # 시작값이 0
    반복할 코드 --> 횟수만큼 실행

for 변수명 in range(시작값, 끝값+1):
     반복할 코드

for 변수명 in range(시작값, 끝값*1, 증감값):
    반복할 코드

for _ in range(횟수): # 반복할 변수를 생략가능(횟수만 반복하고 싶을때)
    반복할 코드
'''

# 시퀀스(순서가 있는 자료형: 리스트, 튜플, 문자열)와 for문

# for와 리스트
for n in [1,2,3]:
    print(n)

print()

string = ['가위', '바위', '보']
for item in string:
    print(item)

print('--------------------')

# for와 문자열
for ch in "Hello":
    print(ch)

print('--------------------')

# for와 튜플
four_seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
for season in four_seasons:
    print(season)

# p120
pwd = input('비밀번호를 입력하세요 >>> ')

ch_count = 0 # 문자 갯수를 담을 변수
num_count = 0 # 숫자 갯수를 담을 변수

for ch in pwd:
    if ch.isalpha(): # isalpha 문자면 True, 숫자면 False 반환   
        ch_count =+ 1
    elif ch.isnumeric():
        num_count =+ 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호')

# for와 range()
for i in range(10): # 10번 반복, i 변수의 초깃값 0
    print(f'{i}번째 문장입니다!') # 0~9

print()

for i in range(1,11): # 10번 반복, i 변수의 초깃값 1, 끝값 10
    print(f'{i}번째 문장입니다!') # 1~10

print()

for i in range(1,11,2): # 홀수만 출력, 증감값 2
    print(f'{i}번째 문장입니다!') # 1,3,5,7,9

print()

for i in range(10,0,-1): # 10부터 1까지 1씩 감소
    print(f'{i}번째 문장입니다!') # 10~1

print()

for i in reversed(range(10)): # reversed : 반전(반대로)
    print(f'{i}번째 문장입니다!') # 9~0

print()

count = int(input('반복할 횟수를 입력하세요 (1부터 시작) : '))
for i in range(1,count+1):
    print(f'{i}번째 문장입니다!')

# ex) 1부터 100까지 수 중 3의 배수, 5의 배수, 3과 5의 공배수를 출력
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print(f'{i}: 3과 5의 공배수')
    elif i%3 == 0:
        print(f'{i}: 3의 배수')
    elif i%5 == 0:
        print('{}: 5의 배수'.format(i))
    else:
        print(i)

# p125
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1,10):
    print(f'{dan}X{n}={dan*n}')

# ex) 중첩 for문을 사용한 구구단 만들기
for i in range(2,10):
    print(f'-{i}단-')
    for j in range(1,10):
        print(f'{i}X{j}={i*j}', end = ' ')
    print()
    print()


# ex) 중첩 for문을 이용한 별찍기
for i in range(5): # 총 다섯번
    for j in range(5):
        print('*', end=('')) # 옆으로 다섯번
    print()

print()

for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()

print()

for i in range(5):
    for j in range(5):
        if i > j:
            print(' ', end='')
        else:
            print('*', end='')
    print()

print()

for i in range(5):
    for j in range(i+1):
        print('*', end = '')
    print()

#############################################
# ex) 반복문 문제
# 문제 1 ) for를 이용해서 1~5까지의 숫자들을 차례대로 출력하기
# (range 함수 사용)
# [화면실행결과]
# 1 2 3 4 5
for i in range(1,6):
    print(i, end = ' ')

print()
# 문제 2 ) for문을 이용하여 1부터 10까지의 합을 구하시오.
# [화면실행결과]
# 1부터 10까지의 합 : 55
# 힌트 : 합계를 담을 변수를 먼제 만들어서 초기화하고 진행하기, range 사용
sum = 0
for num in range(1,11):
    sum += num
print(f'1부터 10까지의 합 : {sum}')

print()

# 문제 3 ) for문을 이용하여 1부터 키보드로 입력한 값까지의 합계 구하기
# [화면실행결과]
# 값을 입력하시오: 123
# 1부터 123까지의 합계 : 7626

sum = 0
num = int(input('값을 입력하시오: '))
for i in range(1,num+1):
    sum += i
print('1부터 {}까지의 합계: {}'.format(num,sum))
