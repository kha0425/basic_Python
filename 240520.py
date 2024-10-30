# 주말 과제
# sep : 구분자
print(2020, 10, 31, sep = "/" , end = ' ')
print(11,43,59, sep = ":")

string = 'PYTHON'
print(string[0])
print(string[1])
print(string[3])
print(string[-1])

mystr = 'GOOD NIGHT'
print(mystr[1:3])
print(mystr[-3:-1])
print(mystr[4:])

fruit = ["딸기", "복숭아", "포도"]
print(fruit)

food = ["치킨", "피자", "떡볶이"]
fruit.extend(food)
print(fruit)

fruit[0] = "바나나"
print(fruit)

# 리스트 연산자 --> +, *
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(list_a)
print(list_b)

list_c = list_a + list_b # 하나의 리스트로 합쳐진다(이어진다)
print(list_c)

list_d = list_a * 3 # 곱한 숫자만큼 반복
print(list_d)

# 리스트의 요소(값) 추가 : append, insert
# 메서드 : 파이썬에서 . 해서 나오는 함수
list1 = [1, 2, 3]
print('list1:', list1)

list1.append(4) # 맨 뒤에 정수 4를 삽입
print('list1:', list1)

list1.append(100)
print('list1:', list1)

list1.insert(1, 50) # 1번 인덱스 자리에 정수 50을 삽입
print('list1:', list1)

# 리스트의 요소(값) 제거 - 인덱스 번호로 삭제 : pop, del
list2 = [0, 1, 2, 3, 4, 5]
print('list2:', list2)

del list2[1] # 1번 인덱스 자료(값)를 삭제
print('list2:', list2)

list2.pop(2) # 2번 인덱스 자료(값)를 삭제
print('list2:', list2)

list2.pop() # 맨 마지막 자료(값) 삭제
print('list2:', list2)

# 튜플 자료형 - 읽기 전용 리스트
t1 = (1, 2, 3)
print('tuple t1:', t1)

t2 = 1, 2, 3 # 괄호를 생략할 수 있다.
print('tuple t2:', t2)

t3 = tuple([100, 3.14, 'hello'])
print('tuple t3:', t3)
print(type(t3))

t4 = (100) # 튜플이 아님, 변수로 인식
print('변수 t4:', t4)
print(type(t4))

t5 = (100,) # 한개짜리 튜플 생성시 (변수,)
print('tuple:', t5)
print(type(t5))

# 리스트와 튜플의 차이점
'''
리스트는 [], 튜플은 ()
리스트는 그 값의 추가, 수정, 삭제 가능
튜플은 그 값을 바꿀 수 없다.
'''

# 리스트와 튜플의 공통점
'''
연산 가능(덧셈, 곱셈)
인덱싱, 슬라이싱 가능(시퀀스 자료형 - 순서가 있는 자료형)
'''

# 세트 (집합)
# 순서가 없고, 중복이 없다.
# 집합 연산 
s1 = {1, 2, 3}
print('set s1:', s1)
print(type(s1))

# set 관련 함수
# 값 1개 추가하기 - add
s1.add(4) # 무조건 맨 뒤에 추가(순서가 없기 때문에)
print('set s1:', s1)

# 값 여러개 추가하기 - update
s1.update([5, 6, 7])
print('set s1:', s1)

# 특정 값을 제거하기 - remove --> 값을 직접 작성해야 함
s1.remove(3) # 값 3을 지워라
print('set s1:', s1)

# 딕셔너리
dic = {} # 빈 딕셔너리
print(type(dic))

s2 = set() # 빈 세트
print(s2)
print(type(s2))

dic = {'name': '홍길동', 'birthday': '0720'}
print('딕셔너리 dic:', dic)

# 특정 값을 출력할 때
print(dic['name']) # 값(홍길동)이 출력
a = dic['birthday'] # 0720이 변수 a에 담긴다
print(a)

# 딕셔너리 값을 수정할 때
dic['name'] = '푸바오'
print('딕셔너리 dic:', dic)

# 딕셔너리 쌍을 추가할 때
dic['address'] = '용인'  # 해당하는 키가 없으면 추가됨
print('딕셔너리 dic:', dic)

# 딕셔너리 쌍을 삭제할 떄 - del
del dic['address']  # adderess에 해당하는 키와 값 삭제
print('딕셔너리 dic:', dic)

# key 리스트 만들기 = keys
print(dic.keys()) # 키 부분만 따로 모은 것
li = list(dic.keys())
print(li)
print(type(li))

# 값(values) 리스트 만들기 - values
print(dic.values())
li_values = list(dic.values())
print(li_values)
print(type(li_values))

# items 함수를 이용해서 쌍을 얻기
print(dic.items()) # 쌍이 튜플형식으로 묶인다.
li_items = list(dic.items()) # 키와 값이 하나의 튜플로 형성
print(li_items)
print(type(li_items))

# 키와 값을 모두 지우기
dic.clear()
print('딕셔너리 dic:', dic)
