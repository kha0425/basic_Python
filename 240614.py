# 파일에서 문자열 읽기
'''
<형식>
파일객체명 = open('파일이름', 'r')
변수명 = 파일객체명.read()
파일객체명.close()


print(변수명) # 화면으로 보고싶을 때 사용
'''

# ex)
# file = open('Hello.txt','r') # 파일 열기(읽기 모드로)
# temp = file.read() # 읽은 내용을 temp 변수에 담는다
# file.close() # 파일 닫기

# print(temp)

# 파일에서 여러 줄을 리스트로 각각 읽기
'''
<형식>
파일객체명 = open('파일이름', 'r')
리스트명 = 파일객체명.readlines()
파일객체명.close()

print(리스트명) # 화면에서 보고싶을 때 사용
'''

# ex)
file = open('./data/Hello.txt','r')
lines = file.readlines() # 파일에서 읽은 내용을 리스트형식으로 저장
file.close()

print(lines)
print('--------------------')
print(lines[3], end = '')
print('--------------------')
for line in lines:
    print(line, end = '') # print함수에 있는 엔터 기능 삭제

# 232p
import time

file = open('./output/'+time.strftime('%Y-%m-%d') + '.txt','at') # 날짜에 형식지정(파일명)
while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>> ')
    if not schedule: # 스케줄이 없다면(아무것도 입력안햇다면)
        break # 반복문을 종료합니다.
    file.write(schedule + '\n') # 스케줄 뒤에 엔터 삽입
file.close()  # 파일 닫기

# 237p
file = open('./data/엄마돼지아기돼지.txt', 'rt') # 파일 열기(읽기 모드로)

line_list = file.readlines() # 전체 글을 저장할 리스트
count = 0
for line in line_list: # 전체글 중 하나의 라인을 문자열 line 변수에 저장
    for ch in line: # line에 담긴 모든 문자들을 하나씩 ch변수에 저장
        if ch == '꿀': # ch변수에 담긴 값과 꿀을 비교
            count += 1 # 같다면 1씩 증가(개수변수 증가)
file.close() # 파일 닫기

print(f'꿀은 전체 {count}번 나타납니다.')

# with문과 함께 파일 입출력 하기
'''
파일을 열면 항상 close 해주어야 하는 불편함을 덜어주는 기능
 <형식>
 with open('파일 이름', '파일 열기 모드') as 파일객체명:
    수행할 코드
'''
# ex)
li = ["Hello~\n", 'world~\n', 'merong~~\n', 'python!!\n']

with open('./output/file.txt', 'wt') as f: # 파일 열기(쓰기 모드로)
    f.writelines(li) # 리스트를 파일에 쓸 때
    f.write('ㅋㅋㅋㅋㅋ\n')
    f.write('파이썬 재밌어!\n')

with open('./output/file.txt','rt') as f: # 파일 열기(읽기 모드로)
    temp = f.read() # 파일의 내용을 모두 읽어 temp변수에 담는다.
print(temp)

# 섹션 14 : 파일입출력의 활용

# 파일 복사
# 243p
buffer_size = 1024  # 한 번에 읽어들이는 데이터의 크기(1024byte == 1kb)
with open('./data/code.mp4', 'rb') as source: # 읽을 파일 열기
    with open('./output/code2.mp4','wb') as copy: # 복사해서 쓸 파일 열기
        while True:
            buffer = source.read(buffer_size) # buffer size만큼 읽어 변수에 담는다.
            if not buffer:
                break
            copy.write(buffer) # 복사파일에 쓰기
print('code2.mp4 파일이 복사되었습니다.')

# csv 파일입출력
# csv 파일 읽기
# 246p
student_list = [] # 최종 결과를 담을 빈 리스트를 만든다.
with open('./data/학생명단.csv','rt',encoding = 'cp949') as file:
    file.readline() # 제목 줄(지워진다.)
    while True:
        line = file.readline() # 한 줄씩 읽어 line 변수에 담는다.
        if not line:
            break
        student = line.split(',') # ,로 구분된 것을 분리해서 student에 저장
        print(student)
        student_list.append(student) # 결과 리스트에 분리한 student 저장

print(student_list)

# 247p
member_list = []
with open('./data/회원명단.csv','rt',encoding='cp949') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',') # ["강나라",'필라테스','25일']
        # print(member)
        member[0] = member[0].strip('"') # 양쪽 큰 따옴표 제거 후 다시 저장
        member_list.append(member)
print(member_list)

#######################################################
# 파일입출력 문제
# 새로운 텍스트 파일 loop.txt를 생성하되, 파일 열기 모드를 추가모드로 한다.
# 1부터 100까지 한 칸씩만 뛰우고 모두 한 줄에 저장한다.
# [loop.txt 열어서 본 결과]
# 숫자1 숫자2 숫자3 ....
with open('./output/loop.txt','at') as f:
    for i in range(1,101):
        f.write(f'숫자{i} ')

file = open('./output/loop.txt', 'at')
for i in range(1,101):
    file.write(f'숫자{i} ')
file.close()
