# __name__
'''
현재 모듈의 이름을 담고 있는 내장 변수

원래 파일에서 실행하면 __name__에 '__main__'이 할당
모듈로 참조하고 있는 다른 파일에서 실행하면
__name__에 해당 모듈명이 할당됨
'''
import my_secure

# Using the functions from the secure module
name = my_secure.secure_name('박영희')
number = my_secure.secure_no('12345678901234')
phone = my_secure.secure_phone('01012345678')

print(f"Secure Name: {name}")
print(f"Secure Number: {number}")
print(f"Secure Phone: {phone}")
# ex)
from my_secure import *

print(secure_no('951012-1234567'))

# 210p
# 표준 모듈

# math 모듈
import math

print(math.pi)  # 원주율
print(math.ceil(1.1)) # 올림
print(math.floor(1.9)) # 내림
print(math.sqrt(25)) # 제곱근(루트)
print(math.pow(2,3)) # 거듭제곱

# random 모듈
import random

print(random.randint(1,10)) # 1 이상 10 이하의 정수 중 랜덤한 정수 반환
print(random.randrange(10)) # 0 이상 10 미만의 정수 중 랜덤한 정수 반환
print(random.randrange(1,11)) # 1 이상 11 미만의 정수 중 랜덤한 정수 반환
print(random.randrange(1,11,2)) # 1,3,5,7,9 중 하나

print(random.random()) # 0 이상 1 미만 중 아무 숫자(실수)

seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons)) # seasons 리스트 값 중 하나

print(random.sample(range(1,46),6)) # 중복없이 6개의 숫자를 리스트 형태로 반환

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list) # 임의로 리스트 요소 섞기
print(my_list)

# p213
import random

dice = random.randint(1,6) # 1~6
while True:
    user = int(input('주사위 값은 얼마일까요? >>> '))
    if dice == user:
        print('{}! 정답입니다.!'.format(dice))
        break
    else:
        print(f'오답입니다! 주사위 값은 {dice}입니다. 다시 시도하세요!')

# ex) 모듈을 이용해서 속으로 10초 세어 맞히는 프로그램
import time

input('엔터를 누르고 10초를 셉니다!!')
start = time.time() # 현재 시간을 저장

input('10초 후에 다시 엔터를 누릅니다!!')
end = time.time()

diff = end - start # 두 시간의 차이
print(f'실제 걸린 시간: {diff}초')
print(f'내가 예측한 시간과의 차이 : {abs(diff-10)}초')

# 218p
from datetime import *

start = datetime.now()  # 계산하기 전 현재 날짜와 시간
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.now() # 계산 완료 후 현재 날짜와 시간
elapse = end - start # 차이
elapse = elapse.total_seconds() # 초 단위로 변환해서 다시 저장
print(f'총 합은 {total}입니다.')
print(f'총 {elapse}가 소요되었습니다.')

# 섹션 13: 파일 입출력

# 파일 생성하고 문자열 쓰기
'''
<형식> (기본 문법)
파일객체명 = open('파일이름', 'w') # 파일 열기 (텍스트)
파일객체명.write('문자열')
파일객체명.write(str(숫자)) # write 함수는 문자열 형식만 가능
파일객체명.close() # 파일 닫기

<형식> (리스트 문법)
리스트명 = [값1, 값2, ...]
파일객체명 = open('파일 이름', 'w')
파일객체명.writelines(리스트명)
파일객체명.close()
'''

# ex)
file = open('Hello.txt', 'w')  # 파일 열기(쓰기 모드로)
file.write('Hello, world!')
file.close() # 파일 닫기

# ex) for를 이용해서 파일에 문자열 쓰기
file = open('Hello.txt','w')
# 상대 경로 : 현재 폴더를 기준으로   ./(현재폴더) ../(상위 폴더)
# 절대 경로 : 'C:\python'
# 예를 들어 c 드라이브 안 a라는 폴더에 hello.txt를 생성(절대 경로)
# 'C:/a/hello.txt'
for i in range(1,11):
    data = f'{i}번째 줄입니다.\n' # \n: 엔터
    file.write(data)

file.close() # 파일 닫기

# ex) for를 이용해서 파일에 새로운 내용을 추가하기
file = open('Hello.txt', 'a') # 파일 열기(추가 모드로)
for i in range(11,21):
    data = f'{i}번째 줄입니다.~~~~~~~~~~~~~~~~!!\n' # \n: 엔터
    file.write(data)
file.close()

######################################################
# 파일입출력 문제)
# 새로운 텍스트 파일 text.txt를 만들고 1부터 10까지의 수가 저장 되도록 하여라
# 쓰기 모드
# [text.txt 파일 열었을 때]
# 12345678910
file = open('text.txt', 'w')
for i in range(1,11):
    file.write(f'{i}')
file.close()