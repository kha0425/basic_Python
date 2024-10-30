# 267p
class Computer: #클래스 정의
    def set_spec(self, cpu, ram, vga, ssd): # 인스턴스 메서드 정의
        self.cpu = cpu # 인스턴스 변수(객체 변수)
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self): # 인스턴스 메서드 정의
        print('CPU : {}'.format(self.cpu))
        print('RAM : {}'.format(self.ram))
        print('VGA : {}'.format(self.vga))
        print('SSD : {}'.format(self.ssd))
        print('--------------------------')

desktop = Computer() # 인스턴스 객체를 생성 -> 붕어빵을 구웠다.
desktop.set_spec('i7','16GB', 'GTX1060', '512GB') # 인스턴스 메서드 호출
desktop.hardware_info() # 인스턴스 메서드 호출
print(desktop)
print('--------------------------')
notebook = Computer() # 인스턴스(객체) 생성 -> 또 다른 붕어빵을 구웠다.
notebook.set_spec('i5','8GB', 'MX300', '256GB') # 인스턴스 메서드 호출
notebook.hardware_info() # 인스턴스 메서드 호출
print(notebook)

# 269p
class Calculator(): # 클래스 정의
    def input_expr(self): # 인스턴스 메서드 정의
        expr = input('수식을 입력하세요 >>>') # 지역 변수
        self.expr = expr  # 인스턴스 변수로 다시 저장
    def calculate(self): # 인스턴스 메서드 정의
        return eval(self.expr) # eval() : 문자열로 된 수식을 계산해주는 함수
    
calc = Calculator() # 인스턴스(객체) 생성 -> 붕어빵을 구웠다.
calc.input_expr() # 인스턴스 메서드 호출
print(f'수식 결과는 {calc.calculate()}입니다.')

# 270p 섹션 15 응용예제 1번)
class Book(): # 클래스 정의
    def set_info(self,title, author): # 인스턴스 메서드 정의
        self.title = title
        self.author = author
    
    def print_info(self): # 인스턴스 메서드 정의
        print(f'책 제목 : {self.title}')
        print(f'책 저자 : {self.author}')
        print('-------------------------')

# 인스턴스(객체) 생성 -> 책 생성
book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()
print(book1, book2, book3, book4, sep = '\n')

# 책 제목과 저자 정보를 저장
book1.set_info('파이썬','민경태')
book2.set_info('어린왕자','생택쥐페리')
book3.set_info('오늘부터 개발자','김병욱')
book4.set_info('트렌드 코리아 2024', '김난도')

book_list = [book1, book2, book3, book4] # 객체 4개를 담은 리스트 생성
print(book_list)
for book in book_list:
    book.print_info() # 출력 메서드 호출

# 섹션 15 응용예제 2번)
class Watch(): # 클래스 생성
    def set_time(self): # 인스턴스 메서드 정의
        now = input('시간을 입력하세요 >>> ') # ex)12:00:00
        hms = now.split(':') # :(콜론)으로 분리 ex) ['12','00','00']
        self.hour = int(hms[0]) # 인스턴스 변수
        self.minute = int(hms[1]) # 인스턴스 변수
        self.second = int(hms[2]) # 인스턴스 변수
    
    def add_hour(self, hour): # 인스턴스 메서드 정의
        if hour <= 0:
            return # 함수 종료
        self.hour += hour
        self.hour %= 24

    def add_minute(self, minute): # 인스턴스 메서드 정의
        if minute <= 0:
            return # 함수 종료
        self.minute += minute
        self.add_hour(self.minute//60)
        self.minute %= 60

    def add_second(self, second):
        if second <= 0:
            return # 함수 종료
        self.second += second
        self.add_minute(self.second//60)
        self.second %= 60

    def see(self): # 인스턴스 메서드(출력 메서드)
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초 입니다.') 

watch = Watch() # 인스턴스(객체) 생성
watch.set_time() # 인스턴스 메서드 호출
watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))
watch.see()# 출력(인스턴스) 메서드 호출

#####################################################################################
# 클래스 문제)
# 친구의 이름과 전화번호 정보를 담을 수 있는 클래스 Friend를 만들어 보자
# set_info(), show_info() 인스턴스 메서드를 포함한다.
# 인스턴스 변수 : 이름, 전화번호 (변수명은 마음대로 하기!)
# [화면실행결과]
# 이름 : 라이언
# 전화번호 : 010-1234-5678
# -------------------------
# 이름 : 춘식이
# 전화번호 : 010-1111-2222

class Friend():
    def set_info(self,name,tel):
        self.name = name
        self.tel = tel

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'전화번호 : {self.tel}')
        print('--------------------------')

# 인스턴스(객체) 생성 -> 붕어빵 굽는다 -> 친구 생성
person1 = Friend()
person2 = Friend()
# 인스턴스 메서드 호출(데이터 저장하는 역할을 하는 메서드 호출)
person1.set_info('라이언','010-1234-5678')
person2.set_info('춘식이','010-1111-2222')

# 인스턴스 메서드 호출(출력해주는 메서드 호출)
person_list = [person1,person2]

for person in person_list:
    person.show_info()

# 현재 시간 저장하여 계산
import time
class Watch(): # 클래스 생성
    def set_time(self): # 인스턴스 메서드 정의
        now = time.strftime('%H-%M-%S')
        hms = now.split('-') # :(-)으로 분리 ex) ['12','00','00']
        self.hour = int(hms[0]) # 인스턴스 변수
        self.minute = int(hms[1]) # 인스턴스 변수
        self.second = int(hms[2]) # 인스턴스 변수
    
    def add_hour(self, hour): # 인스턴스 메서드 정의
        if hour <= 0:
            return # 함수 종료
        self.hour += hour
        self.hour %= 24

    def add_minute(self, minute): # 인스턴스 메서드 정의
        if minute <= 0:
            return # 함수 종료
        self.minute += minute
        self.add_hour(self.minute//60)
        self.minute %= 60

    def add_second(self, second):
        if second <= 0:
            return # 함수 종료
        self.second += second
        self.add_minute(self.second//60)
        self.second %= 60

    def see(self): # 인스턴스 메서드(출력 메서드)
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초 입니다.') 

watch = Watch() # 인스턴스(객체) 생성
watch.set_time() # 인스턴스 메서드 호출
watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))
watch.see()# 출력(인스턴스) 메서드 호출

# 섹션 16 : 클래스와 객체2
# 생성자 (constructor)

'''
객체에서 초깃값을 설정해야 할 필요가 있을 때 사용, ex) set_info()
객체가 생성될 때 자동으로 호출해주는 메서드
__init__  사용

스페셜메서드(매직메서드) : 파이썬에서 목적에 따라 자동으로 호출되는 메서드
                        앞뒤로 __가 붙은 메서드
<형식>
class 클래스 이름:
    def __init__(self): # 생성자(인스턴스 메서드)
        self.속성 = 값 # 인스턴스 변수
'''

# ex) 생성자를 사용하지 않은 경우
class Candy:
    def set_info(self,shape,color): # 인스턴스 메서드 정의
        self.shape = shape # 인스턴스 변수
        self.color = color # 인스턴스 변수

    def print_info(self): # 인스턴스 메서드
        print('<생성자를 사용하지 않은 경우!!>')
        print('self.shape: ',self.shape)
        print('self.color: ',self.color)
        print('-------------------------')

satang = Candy() # 인스턴스 객체 생성
satang.set_info('circle','red') # 인스턴스 메서드 호출
satang.print_info() # 인스턴스 메서드 호출

# ex) 생성자를 사용한 예제
class Candy2:
    def __init__(self,shape,color): # 생성자
        self.shape = shape
        self.color = color
    def print_info(self): # 일반 인스턴스 메서드
        print('<생성자를 사용한 경우!!>')
        print('self.shape: ',self.shape)
        print('self.color: ',self.color)
        print('-------------------------')

satang2 = Candy2('circle','red') # 객체 생성과 동시에 생성자를 호출
satang2.print_info() # 인스턴스 메서드 호출
satang3 = Candy2('circle','pink') # 객체 생성과 동시에 생성자를 호출
satang4 = Candy2('circle','green') # 객체 생성과 동시에 생성자를 호출
satang_list = [satang2,satang3,satang4]
for satang in satang_list:
    satang.print_info()

######################################################################
# 과제) 파일입출력
# practice.txt를 만들어 '제 1의 아해가 무섭다고 그리오.' 부터
# '제 5의 아해가 무섭다고 그리오.'까지 순서대로 한 줄에 하나씩
# 파일안에 내용을 넣고, 그 파일을 다시 열어 파이썬 화면에 출력하시오
# (파일 쓰기 , 파일 읽기 모두 해야함)
# [화면 출력 결과]
# 제 1의 아해가 무섭다고 그리오.
# 제 2의 아해가 무섭다고 그리오.
# 제 3의 아해가 무섭다고 그리오.
# 제 4의 아해가 무섭다고 그리오.
# 제 5의 아해가 무섭다고 그리오.

# 1)
f = open('./output/practice.txt','wt')
for i in range(1,6):
    f.write(f'제 {i}의 아해가 무섭다고 그리오.\n')
f.close()

f = open('./output/practice.txt','rt')
lines = f.readlines()
for line in lines:
    print(line, end = '')
f.close()

# 2)
with open('./output/practice2.txt','wt') as f:
    for i in range (1,6):
        f.write(f'제 {i}의 아해가 무섭다고 그리오.\n')

with open('./output/practice2.txt','rt') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')