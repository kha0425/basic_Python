# 섹션 3 : 기본 입출력
# 표준 출력
# 이스케이프 문자
# \n: 줄 바꿈
'''
프로그래밍 할 때 사용할 수 있도록 미리 정의해둔 문자 조합
출력물을 보기 좋게 보는 용도로 사용
대표적인 것 --> \n (엔터)
'''

# 53p
print('Hello \'World\'')
print("Hello 'world'")

print("Hello \"word\"")
print('Hello "world"')

print('*\n**\n***')

# p54(print() 함수)
# p55
print('재미있는', '파이썬')
print('Python', 'Java', 'C', sep = ',')

print() # 빈 줄을 의미

print('영화 타이타닉')
print('평점', end = ':')
print('5점')

fos = open('sample.py', mode = 'wt')  # 파일 열기
print('print("Hello World")', file = fos) # 파일에 출력(저장)
fos.close() # 파일 닫기

# 형식을 갖춘 문자열(문자열 포매팅)
# 1) % 연산자 (기본 포매팅)
# p58
name = 'Kai' # 문자열
print('내 이름은 %s 입니다.' % name)

heigth = 120.5 # 실수
print('내 키는 %f 입니다.' % heigth) # 소수 여섯째자리까지 출력

weight = 23.55 # 실수
print('내 몸무게는 %.1fkg 입니다.' % weight) # 소수 첫째자리까지 반올림해서 출력

year, month, day = 2014, 8, 25 # 정수형
print('내 생일은 %d년 %d월 %d일 입니다.' % (year,month,day))

# p59
# 2) .format() 

'''
<형식>
'문자열 {}'.format(변수명)
'''
# 60p
zipcode = '06236'
print('우편번호 : {}'.format(zipcode))

address = '''서울특별시 강남구
테헤란로 146'''
print('주소 : {addr}'.format(addr=address))

tel1, tel2, tel3 = '02', '538', '0021'
print('연락처: {0}-{1}-{2}'.format(tel1,tel2,tel3))

# ex)
print('{0:<10}'.format('Hi')) # 전체 10칸, 왼쪽 정렬
print('{0:>10}'.format('Hi')) # 전체 10칸, 오른쪽 정렬
print('{0:^10}'.format('Hi')) # 전체 10칸, 가운데 정렬

print('{:=^30}'.format('python')) # 전체 30칸, 가운데 정렬, 공백을 '='로 표현
print('{:!<30}'.format('python')) # 전체 30칸, 왼쪽 정렬, 공백을 '!'로 표현

n = 3.141595
print('{:.3f}'.format(n)) # 소수셋째자리까지 반올림

a = '파이썬 열공하여 첫 연봉 {}만원 만들기'.format(5000)
print(a)

b = '{} {}      {}'.format(100, 200, 300)
print(b)

c = '{} {} {}'.format(1, '파이썬', True)
print(c)

# f - strings (f문자열 포매팅)
'''
<형식>
f'문자열 {변수명} 문자열'
'''

# ex)
name = '푸바오'
age = 3
print(f'나의 이름은 {name}이고 {age}살 입니다.')
print(f'나는 내년이면 {age+1}살이 됩니다.') # 변수 연산은 .format에서도 가능하다.

print(f'{"python":=^30}') # 전체 30칸, 공백을 =로 표현, 가운데 정렬
print(f'{"python":!<30}') # 전체 30칸, 공백을 !로 표현, 외쪽 정렬
print(f'{"python":!>30}') # 전체 30칸, 공백을 !로 표현, 오른쪽 정렬

n = 3.141592
print(f'{n:.4f}') # 소수 넷째자리까지 반올림

# 포매팅 비교하기
n = 3 # 정수
print('I eat', n, 'apples.')
print('I eat %d appels.' % n) # % 연산자 포매팅(기본 포매팅)
print('I eat {} apples.'.format(n)) # format메서드 포매팅
print(f'I eat {n} apples.') # f-strings (f 문자열 포매팅)

# 표준 입력
# input() 함수
n = input('정수를 입력하세요 :')
print(n)

# p63
name = input('이름을 입력하세요: ')
age = input('나이를 입력하세요: ')
print('입력된 이름은 {}입니다.'.format(name))
print('입력된 나이는 {}살 입니다.'.format(age))


############################################
# 포매팅 문제)
# 변수 number 에 정수 5를 담고, 오늘 배운 3가지 포매팅 형식으로 출력해보자
# 화면 실행 결과
# I ate 5 apples
number = 5
print('I ate %d apples.' %number)
print('I ate {} apples.'.format(number))
print(f'I age {number} apples.')




