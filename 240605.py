# 숫자 내장 함수
# abs() : 절대값
print(abs(10))
print(abs(-10))
print('------------------------')

# divmod(): (몫,나머지), 결과는 튜플 형식
print(divmod(10,3))
a,b = divmod(10,3)
print(a)
print(b)
print('------------------------')

# max() : 최댓값
print(max(1,2))
li = [10,8,4,6,2]
print(max(li))
print('------------------------')

# min() : 최솟값
print(min(1,10))
print(min(li))
print('------------------------')

# pow() : 거듭제곱 (** 연산자)
print(pow(2,3)) # 2를 3번 곱하다
print(pow(10,3))
print(pow(10,-2))
print('------------------------')

# round() : 반올림
print(round(1.5)) # 일의 자리까지
print(round(1.4))
print(round(1.55,1)) # 소수 첫째자리까지

# sum() : 합계 함수
li = [1,2,3,4,5]
print(sum(li))

# p153
money = 10000
price = 3000 # 빵 한개의 가격
result = divmod(money,price)
print(f'빵을{result[0]}개 사고 {result[1]}원이 남았습니다.')

# 시퀀스 내장 함수

# enumerate()
'''
<형식>
for 인덱스번호, 값 in enumerate(리스트) : # 문자열 또는 튜플도 가능
    수행할 코드
'''

# ex)
li = [10,20,30]
for i in li:
    print(i) # 리스트의 값(요소)만 출력

print()

for item in enumerate(li):
    print(item) # 튜플로 묶어져서 나온다

for index,value in enumerate(li):
    print(f'{index}번째 : {value}')

print()
for index,value in enumerate(li):
    print(f'{index+1}번째 : {value}')

for i, v in enumerate(li, start = 1): # 인덱스 시작 번호를 1로 정함
    print('{}번째 : {}'.format(i,v))

print('------------------------------------')

# len() : 길이(글자 수, 리스트 항목수 등)
li = ['a','b','c','d']
print(len(li))

ch = 'Hello'
print(len(ch))

d = {'a':'apple', 'b':'banana'}
print(len(d))

print(len(range(10))) # 0~9 : 10개
print(len(range(1,10))) # 1~9 : 9개

# ex) 총점과 평균구하기
score = [70, 60, 55, 75, 95] # 학생 점수를 모아놓은 리스트
total = 0
for i,v in enumerate(score, start =1):
    print('{}번째 학생 점수 : {}점'.format(i,v))
    total += v
avg = total/len(score) # 리스트의 개수롤 나누어 평균을 구한다.
print(f'학생들의 총 점수는 {total}점 입니다.\n학생들의 점수 평균은 {avg}점 입니다.') 

# sorted(): 정렬
my_list = [6,3,1,2,5,4]
sorted_list = sorted(my_list) # 정렬된 새로운 리스트 생성, 원본은 그대로
reverse_list = sorted(my_list,reverse=True)
print(f'원본 : {my_list}')
print(f'정렬 후 (오름차순) : {sorted_list}')
print(f'정렬 후 (내림차순) : {reverse_list}')
print('----------------------------')

# zip() : 튜플로 묶기
names = ['james','emily','amanda']
scores = [60, 70, 80,]
for student in zip(names,scores):
    print(student)

for name,score in zip(names,scores):
    print(f'{name}의 점수는 {score}점 입니다.')

# p159
months = [31,28,31,30,31,30,31,31,30,31,30,31]
for month,day in enumerate(months):
    print(f'{month+1}월 = {day}일')

# 섹션 10 : 메소드

# 문자열 메소드
# .count() : 특정 문자열의 개수
s = '내가 그린 기린 그림은 목 긴 기린 그림이고 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린'))

a = 'best of best'
print(a.count('best'))
print(a.count('best',5)) # 5번 인덱스부터 시작
print(a.count('best',-7))
print('------------------------')

# .find(), .index() : 특정 문자열의 위치 반환
b = 'apple'
print(b.find('p')) # 해당 인덱스 번호
print(b.rfind('p')) # 끝(오른쪽)에서부터 시작한 해당 인덱스 번호
print(b.find('z')) # 없는 문자일 경우 -1 도출
print(a.find('best'))
print(a.find('best',5)) # 지정한 인덱스부터 검색

print(b.index('p'))
print(b.index('z')) # 없는 문자일 경우 오류가 남.

# .upper(), .lower(), .capitalize() : 대소문자 변환 메소드
s = 'BEST of best'
print(s.upper()) # 대문자 변환
print(s.lower()) # 소분자 변환
print(s.capitalize()) # 첫 글자만 대문자
print('-------------------------')

# .join() : 합치기
a = '-'.join('python')
print(a)

b = '+'.join(['a','b','c']) # 문자열로 도출
print(b)
b = list(b)
print(b)

c = ''.join(['x','y','z'])
print(c)

d = ''.join({'a':'apple','b':'banana'})
print(d) # key만 사용

# .split() : 나누기(리스트 형식으로 결과가 나옴)
a = 'Life is too short'
print(a.split()) # 공백을 기준으로 분리, 리스트로 결과가 도출되기 때문에 인덱싱 가능함.

b = '010-1234-5678'
print(b.split('-')) # -을 기준으로 분리

c = '제임스,25,남,서울'
print(c.split(',')) # ,를 기준으로 분리
print('------------------------------')

# .replace() : 교체 함수
print(a.replace('Life','Leg'))

print(b.replace('-',''))
print('------------------------------')

# .strip() : 불필요한 문자열 제거
a = '      apple   '
print(a)
print(len(a))

b = a.lstrip() # 왼쪽 공백 제거 rstrip() : 오른쪽 공백 제거
print(b)
print(len(b))

c = '<head<'
d = c.strip('<') # 양쪽 '<' 문자 제거
print(c)
print(d)

# 리스트 메소드
# .extend(): 확장(여러개 추가)
my_list = ['apple','banana']
my_list.extend(['cherry','mango']) 
print(my_list) # 원본 수정됨
print('-------------------------------')
pop = my_list.pop()
print(pop)

# .remove() : 특정 값을 제거, 인덱스 번호가 아닌 값을 넣어야 함
my_list.remove('mango')
print(my_list) # 원본 수정됨
my_list.remove('banana')
print(my_list)

# .clear() : 모든 값을 제거합니다.
my_list.clear()
print(my_list)





