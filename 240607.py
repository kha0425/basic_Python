# 173
while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
    if p.find('-') != 6: # 하이픈의 위치가 6이 아니라면
        print('하이픈의 위치가 잘못되었습니다.')
        continue

    birthday = p.split('-')[0] # 하이픈을 기준으로 분리, 0번 인덱스값(생년월일)
    print(f'생년월일은 {birthday}입니다.')
    break

# p177
a_list = ['above','cookie','app','about','admin','bisket','apple','april']

for i,item in enumerate(a_list):
    if item.find('a') == -1: # a 가 없는 값은 -1로 반환
        print('{} 제거됩니다.'.format(a_list.pop(i))) # i번째 값을 삭제

print(a_list)


# 세트 메소드
# ex)
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print('세트 s1: {}'.format(s1))
print('세트 s2: {}'.format(s2))

# 교집합
print('교집합 : {}'.format(s1 & s2))
print('교집합 : {}'.format(s1.intersection(s2)))
print()
# 합집합
print('합집합 : {}'.format(s1 | s2))
print('합집합 : {}'.format(s1.union(s2)))
print()
# 차집합
print('차집합 : {}'.format(s1 - s2))
print('차집합 : {}'.format(s2 - s1))
print('차집합 : {}'.format(s1.difference(s2)))
print('차집합 : {}'.format(s2.difference(s1)))

# 섹션 11 : 사용자 함수

# 함수 용어 정리
'''
입력 : 인수, 인자, 매개변수, 파라미터
출력 : 결과값, 반환값, return, 돌려주는 값
'''

# 매개변수(입력), 반환값(출력)이 없는 가장 간단한 함수
'''
<형식>
def 함수이름() : # 함수 정의
    수행할 코드

# 함수이름() # 함수 호출
# '''
# ex)
def hello(): # 함수 정의
    print('Hello, world')

hello() # 함수 호출
hello()
hello()

# 매개변수(입력)만 있는 함수
'''
<형식>
def 함수이름(매개변수1, 매개변수2): # 함수 정의
    수행할 코드

# 함수이름(인수1,인수2) # 함수 호출
# '''
# ex) 
def add(a,b): # 함수 정의
    print(a + b) 
add(10,5) # 함수 호출
add(10,20)

x = 6
y = 3
add(x,y)

n1 = int(input('첫번째 수를 입력하세요 >> '))
n2 = int(input('두번째 수를 입력하세요 >> '))
add(n1,n2)

# 반환값(출력)만 있는 함수
'''
<형식>
def 함수이름(): # 함수 정의
    수행할 코드 - 없어도 됨(만드는 사람 마음)
    return 반환값(출력값)
결과변수 = 함수이름() # 함수 호출
'''
# ex)
def hello(): # 함수 정의
    return 'Hello~'

x = hello() # 함수 호출
print(x) 

print(hello()) # 한번만 호출해서 결과를 볼 수도 있다.

# 매개변수(입력), 반환값(출력)이 1개인 함수
'''
<형식> 
def 함수이름(매개변수1,매개변수2): # 함수 정의
    수행할 코드(있으면)
    return 반환값(출력값)

결과변수 = 함수이름(인수1, 인수2) # 함수 호출
'''
# ex)
def add(a, b): # 함수 정의
    return a + b

n1 = add(1,2) # 함수 호출 후 결과값을 n1변수에 담았다
print(n1) # 실제 담겼는지 print문으로 확인해본다.

n2 = add(10,20)
print(n2)

print(add(100,200)) # 한번만 호출

# 매개변수(입력), 반환값(출력)이 2개 이상인 함수
'''
<형식>
def 함수이름(매개변수1,매개변수2): # 함수 정의
    수행할 코드(있으면)
    return 반환값1, 반환값2
결과변수1, 결과변수2 = 함수이름(인수1,인수2) # 함수 호출
'''
# ex)
def add_sub(a, b): # 함수 정의
    return a + b, a - b
x, y = add_sub(1,2)
print(x,y) # 첫번째 결과값을 x변수에, 두번째 결과값을 y변수에 담았다.
print(add_sub(10,20)) # 결과값이 튜플로 추출된다.
print(add_sub(10,20)[0])

# 디퐅트 매개변수(매개변수에 초깃값 설정)
# ex)
def info(name, age, address = '비공개'): # 함수 정의
    print('이름 : {}'.format(name))
    print('나이 : {}'.format(age))
    print('주소 : {}'.format(address))
    print('-------------------------')

info('푸바오',4) # 함수 호출
info('라이언',20,'대구')

# 키워드 인수 : 각각의 매개변수가 어떤 용도인지 알기 어려울 때 사용
# ex)
def info(name ,age, address):
    print('이름 : {}'.format(name))
    print('나이 : {}'.format(age))
    print('주소 : {}'.format(address))
    print('-------------------------')

info('라인언',20,'대구') # 일반적인 함수 호출 방식
info(name = '어피치', age = 30, address = '부산') # 키워드 인수
info(age = 40, address = '서울', name = '춘식이') # 순서를 다르게 지정해도 된다.

##############################################################
# 사용자 함수 문제)
# 1) 매개변수를 통해서 두 개의 정수를 전달받는다.
# 이 둘의 평균값을 계산해서 화면에 보여주는 함수를 만들어보자
# 예를 들어 3과 4가 전달되면 이 두 수 의 평균값 3.5가 나와야 한다.
# 함수이름은 average로 하고, 매개변수명은 각각 num1, num2로 한다.
# 반환값 return은 없다.
# 함수 호출은 한번만 한다.
# [화면실행결과]
# 3.5
def average(num1,num2):
    print((num1+num2)/2)

average(3,4) # 함수 호출

# 2) 하나의 정수를 매개변수에 전달받아서 부호가 반대인 정수를 반환하는
# 함수를 정의해보자. 함수이름은 하고싶은대로 하고, 매개변수명도 자유롭게 한다.
# 반환값 return이 있도록 한다.
# 호출할 때 반환값은 따로 결과변수에 담도록 하고, 그 변수값을 print한다.
# 함수 호출은 한번만 한다.
# [화면실행결과] - 호출할 때 인수를 12로 넣었을 경우
# -12
def reverse(x): # 함수 정의
    return -x
a = reverse(12) # 함수 호출
print(a) 
 


