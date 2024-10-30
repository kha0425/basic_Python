# 비시퀀스와 for문

# for와 세트
for item in {'가위','바위','보'}:
    print(item)  # 순서는 랜덤으로 나온다.

print('-----------------')

# for와 딕셔너리
person = {
          'name': '에밀리',
          'age' : '20'
          }

for item1 in person:
    print(item1) # 키(key)가 출력

print('-----------------')
for item2 in person:
    print(person[item2]) # 값(value) 출력

print('-----------------')
for item3 in person:
    print(person.get(item3)) # 값(value) 출력

# p128
eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}
for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict.get(word)}')

for word in eng_dict:
    print('{}의 뜻: {}'.format(word,eng_dict[word]))

# 섹션 8 : 기타 제어문

# break
# ex) 0부터 99까지 출력
i = 0
while True:
    print(i, end = ' ')
    i += 1
    if i > 99:
        break

while True:
    capital = input('대한민국의 수도를 입력하세요 >>>')
    if capital == '서울' or capital == 'seoul' or capital == 'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요')

# p137
hobbies = []
while True:
    hobby = input('취미를 입력하세요(종료는 그냥 엔터)>>> ')
    if hobby == '':
        print('입력된 취미가 모두 저장되었습니다.')
        break
    else:
        hobbies.append(hobby)
print(hobbies)

# ex) 반복문을 이용한 커피자판기 프로그램
coffee = 3
while True:
    money = int(input('돈을 넣어주세요: '))
    if money == 300: # 커피값이 300원이라고 가정했을 경우
        print('커피 나왔습니다.!')
        coffee -= 1 
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    elif money > 300:
        print(f'거스름돈 {money - 300}원을 주고 커피도 줍니다!')
        coffee -= 1 
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    else:
        print(f'{money}원을 다시 돌려주고 커피는 주지 않습니다!')
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피가 모두 소진되었습니다. 판매를 중지합니다.')
        break

# continue
# ex) 0~10 사이의 수 중에서 홀수만 출력
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: # 짝수라면
        continue
    print(a) # 홀수만 출력

# p139
fruits = ['사과','감귤']
count = 3 # 입력해야 할 남은 과일의 수
while count > 0:
    fruit = input('어떤 과일을 저장할까요 >>>')
    if fruit in fruits: # fruit 변수에 있는 값이 fruits 리스트에 포함되었나?
        print('동일한 과일 입니다. 다시 입력하세요')
        continue # 포함되었다면 다시 반복문의 처음(조건)으로 간다
    fruits.append(fruit) # 포함되지 않았으면 리스트에 추가
    count -= 1 # 횟수를 1번 줄여준다
    print('입력할 기회가 {}번 남았습니다.'.format(count))
print('5개의 과일은 {}입니다.'.format(fruits))

# p140
count = 0 # 횟수 측정
total = 0 # 합계

while count < 5:
    n = int(input('{}번째 정수를 입력하세요>>> '.format(count + 1)))
    if n <= 0: # 0과 음수를 제외하기 위해 넣은 코드
        print('0이하의 정수를 처리할 수 없습니다.')
        continue
    total += n
    count += 1

print('입력된 5개의 양수의 총 합은 {}입니다.'.format(total))


# 참고) 리스트 내포(리스트 컴프리헨션)
# append 사용
li = [1, 2, 3]
num1 = []
for i in li:
    # i = i*2
    num1.append(i*2)
print(f'append를 사용했을때 : {num1}')

# 리스트 내포 사용
'''
리스트 = [표현식 for 변수 in 반복가능한객체(리스트,튜플 등) if 조건식]
'''
num2 =[n*2 for n in li]
print(f'리스트 내포를 사용했을때 : {num2}')

# 섹션 9 : 내장 함수
# 문자열 내장 함수
# chr() : 유니코드를 문자로 변환
print(chr(48))
print(chr(49))
print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))
print(chr(44032))
print('----------------')

# ord(): 문자를 유니코드로 변환
print(ord('A'))
print(ord('a'))
print(ord('가'))
print('----------------')

# eval(): 문자열로 된 값을 계산
print('100 + 200')
print(eval('100+200'))
print(eval('min(1,2,3)')) # min(): 최솟값

# p149
expr = input('계산식을 입력하세요 >>> ')
result = eval(expr)
print(expr+'='+str(result))
print(f'{expr}={result}')
print(type(result))
# enumerate(), sum(), sorted(), filter(), map(), len()

#######################################################
# for문제)
# 시작값과 끝값, 증감값까지 사용자에게 정수를 입력받아
# 시작값과 끝값까지의 합계구하기(for, range()이용)
# [화면실행결과]
# 시작값을 입력하시오 : 3
# 끝값을 입력하시오 : 300
# 증감값을 입력하시오 : 3
# 3에서 300까지 3씩 증가시킨 값의 합계 : 15150
a = int(input('시작값을 입력하시오 : '))
b = int(input('끝값을 입력하시오 : '))
c = int(input('증감값을 입력하시오 : '))
sum = 0
for i in range(a,b+1,c):
    sum += i
print(f'{a}에서 {b}까지 {c}씩 증가시킨 값의 합계: {sum}')
    
    