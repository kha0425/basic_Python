# csv 모듈로 csv 파일 생성하기
# 249p
import csv

with open('./data/차량관리.csv', 'wt', newline = '') as file:
    csv_maker = csv.writer(file, delimiter = ',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])

print('차량관리.csv 파일이 생성되었습니다.')

# csv 모듈로 csv 파일 읽기
import csv

with open('./data/차량관리.csv','rt') as file:
    csv_reader = csv.reader(file, delimiter= ',', quotechar = '"')
    for line in csv_reader:
        print(line)

print(csv_reader)

# json 파일입출력
# json 파일 쓰기(생성)
# 251p

import json

dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [175.5,70.5]
    },
    {
        'name' : 'alice',
        'age' : 21,
        'spec' : [168.5,60.5]
    }
]

json_string = json.dumps(dict_list)  # json으로 변환(인코딩)

with open('./output/dictList.json','wt') as file:
    file.write(json_string) # json으로 인코딩한 내용을 json파일에 쓴다.

print('dictList.json 파일이 생성되었습니다.')

# json 파일 읽기
# 253p
import json

with open('./output/dictList.json','rt') as file:
    json_reader = file.read() # 파일 전체 읽어 json_reader에 저장
    dict_list = json.loads(json_reader) # 파이썬으로 변환

# print(dict_list)

for dic in dict_list:
    print(f'이름 : {dic['name']}')
    print(f'나이 : {dic['age']}')
    print(f'키 : {dic['spec'][0]}')
    print(f'몸무게 : {dic['spec'][1]}')
    print('--------------------------')

# 섹션 14 응용예제 1번)
while True:
    filename = input('복사할 파일명을 입력하세요 >>> ')
    extname = filename[filename.rfind('.')+1:] # 확장자를 추출
    if extname != 'txt':
        print('복사할 수 없는 파일입니다.')
    else:
        break
with open('./data/'+filename, 'rt') as source: # 원본
    with open('./output/복사본-'+ filename, 'wt') as copy: # 복사본
        while True:
            buffer = source.read(1) # 1바이트씩 읽어 buffer에 담는다
            if not buffer:
                break
            else:
                copy.write(buffer)
print('복사본-' + filename + ' 파일이 생성되었습니다.')

# 섹션 14 응용예제 2번)
import csv
with open('./data/cctv.csv', 'rt', encoding='cp949') as csvfile:
    buffer = csv.reader(csvfile, delimiter = ',', quotechar= '"')
    total_cctv = 0 # cctv 개수
    for i, line in enumerate(buffer):
        if i != 0: # 제목 줄은 제외
            total_cctv += int(line[6])

print(f'대구 광역시 달서구에 설치된 cctv는 총 {total_cctv}대입니다.')

# 섹션 14 응용예제 3번)

import json
with open('./data/cctv.json','rt',encoding='utf-8') as json_file:
    buffer = json_file.read()
    cctv_list = json.loads(buffer) # 파이썬으로 변환
    cctv_purpose = set() # 결과를 담을 빈 세트를 생성(중복x)
    for place in cctv_list:
        cctv_purpose.add(place['설치목적구분']) # set에 추가

print(cctv_purpose)

# 섹션 15 : 클래스와 객체 1

# 객체 지향 프로그래밍(Object-Oriented Programming, OOP)
'''
문제를 작게 나누어 객체(object)를 만들고 객체를 조합해서 문제를
해결하는 방식

복잡한 문제를 처리하는데 유용하며, 기능을 개선하고 발전시킬 때도
해당 클래스만 수정하면 되므로, 유지보수에 효율적

클래스(class) : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도
                과자틀, 붕어빵틀에 비유
객체(object) : 붕어빵틀에서 만들어 낸 붕어빵에 비유
                각각의 객체마다 고유의 특성을 가진다.
                파이썬에서는 문자, 정수, 실수, 함수 등 모두 객체다.
인스턴스(instance) : 특정 객체가 어떤 클래스의 객체인지 관계 위주로
                    설명할 때 사용
                    클래스와 연관지어 객체를 말할 때 인스턴스라고 한다.
메서드(method) : 클래스 안에서 구현된 함수

<형식>
class 클래스이름 : # 파이썬에서는 클래스 이름을 주로 대문자로 사용
    def 메서드이름(self, 매개변수): # 인스턴스 메서드
        # self -> 메서드를 호출한 객체가 자동으로 전달되는 매개변수
        self.속성 = 값 # 인스턴스 변수

인스턴스이름 = 클래스이름() # 인스턴스(객체) 생성 -> 붕어빵 굽는 행위
인스턴스이름.메서드이름() # 메서드(함수) 호출
'''

# ex)
class Person: # 클래스 정의
    def who_am_i(self, name, age, tel, address): # 인스턴스 메서드
        self.name = name  # 인스턴스 변수
        self.age = age
        self.tel = tel
        self.address = address

boy1 = Person() # boy1 인스턴스(객체) 생성 -> 붕어빵을 구웠다(생성)
print(boy1)
boy1.who_am_i('john',15,'123-1234','toronto') # 메서드(함수) 호출
print(boy1.name)
print(boy1.age)
print(boy1.tel)
print(boy1.address)

boy2 = Person() # boy2 인스턴스(객체) 생성 -> 붕어빵 새로 구웠다
print(boy2)
boy2.who_am_i('ryan',20,'111-1111','Daegu') # 인스턴스 메서드(함수) 호출
print(boy2.name)
print(boy2.age)
print(boy2.tel)
print(boy2.address)

boy3 = Person() # boy3 인스턴스(객체) 생성 -> 붕어빵 새로 구웠다
print(boy3)
boy3.who_am_i('fubao',4,'222-2222','Seoul') # 인스턴스 메서드(함수) 호출
print(boy3.name)
print(boy3.age)
print(boy3.tel)
print(boy3.address)

