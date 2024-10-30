# 사용자 예외 클래스
# 305p
class NameError(Exception): # Exception 클래스 상속받음
    def __init__(self,message):
        super().__init__(message)

try:
    name = input('이름을 입력하세요 >>> ')
    if len(name) < 2 or len(name) > 6: # 강제로 예외 발생
        raise NameError('이름은 2~6자 사이로 입력해주세요.')
except NameError as e:
    print(e) # 예외 메시지 출력
else:
    print('입력된 이름은 {}입니다.'.format(name))
# 섹션 17 응용예제 1번)306p
class Quiz:
    answer = ['경기도','강원도','충청남도','충청북도','전라남도','전라북도',
              '경상남도','경상북도','제주특별자치도']
    @classmethod
    def challenge(cls): # 클래서 메서드
        if not cls.answer: # 값이 없다는 뜻은 모두 맞췄다는 뜻
            print('모든 도를 맞췄습니다. 성공입니다.')
            return # 함수 종료
        do = input('정답은? >>> ') # 우리가 한 대답
        if do not in cls.answer: # 대답이 answer에 없는 값이라면(틀렸다면)
            raise Exception('틀렸습니다.') # 예외 발생
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do: 
                print('정답입니다.') # 정답과 대답이 같다면
                cls.answer.pop(i) # i번째 값을 꺼내어 삭제
        cls.challenge()

try:
    print('우리나라의 9개의 모든 도를 맞히는 귀즈입니다. 하나씩 대답하세요')
    Quiz.challenge() # 클래스 메서드 호출
except Exception as e:
    print(e)

class Quiz:
    answer = ['경기도','강원도','충청남도','충청북도','전라남도','전라북도',
              '경상남도','경상북도','제주특별자치도']
    @classmethod
    def challenge(cls): # 클래서 메서드
        if not cls.answer: # 값이 없다는 뜻은 모두 맞췄다는 뜻
            print('모든 도를 맞췄습니다. 성공입니다.')
            return # 함수 종료
        do = input('정답은? >>> ') # 우리가 한 대답
        if do not in cls.answer: # 대답이 answer에 없는 값이라면(틀렸다면)
            raise Exception('틀렸습니다.') # 예외 발생
        for i, answer_do in enumerate(cls.answer):
            if do in answer_do: 
                print('정답입니다.') # 정답과 대답이 같다면
                cls.answer.pop(i) # i번째 값을 꺼내어 삭제
        cls.challenge()

try:
    print('우리나라의 9개의 모든 도를 맞히는 귀즈입니다. 하나씩 대답하세요')
    Quiz.challenge() # 클래스 메서드 호출
except Exception as e:
    print(e)

# 섹션 17 응용예제 2번)
import random

class UpDown:
    def __init__(self): # 생성자
        self.answer = random.randint(1,100) # 정답(1~100사이 중 하나)
        self.count = 0 # 시도 횟수
    
    def challenge(self): # 인스턴스 메서드 정의
        self.count += 1 # 시도 횟수를 1씩 증가
        n = int(input('입력(1~100) >>> ')) # 사용자로부터 숫자 입력받음
        if n < 1 or n > 100: # 범위를 벗어나면 예외 발생시킴
            raise Exception('1~100 사이만 입력하세요')
        return n # 입력값 반환
    
    def play(self): # 인스턴스 메서드 정의
        while True:
            try:
                n = self.challenge() # 숫자를 입력받는다.
            except Exception as e:
                print(e) # 예외 메시지 출력
            else: # 예외 발생하지 않았다면(정상적이라면)
                if self.answer > n:
                    print('Up')
                    print(self.answer)
                elif self.answer < n:
                    print('Down')
                    print(self.answer)
                else: # 정답을 맞힌 경우
                    print('{}만의 정답입니다.'.format(self.count))
                    break
game = UpDown() # 인스턴스(객체) 생성
game.play() # 인스턴스 메서드 호출

# 섹션 17 응용예제 3번)
class BankError(Exception): # 예외 클래스
    def __init__(self,message):
        super().__init__(message)

class BankAccount:
    # 생성자
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no # 계좌번호
        self.balance = balance # 통장 잔액
    # 입금 기능
    def deposit(self,money): # money: 입금할 금액
        if money < 0:
            raise BankError('{}원 입금 불가'.format(money))
        self.balance += money # 입금

    # 출금 기능
    def withdraw(self, money): # money: 출금할 금액
        if money <= 0:
            raise BankError(f'{money}원 출금 불가') # 0원 이하를 출금하려 할때 예외 발생
        if money > self.balance: # 통장 잔액보다 큰 금액을 출금
            raise BankError('잔액 부족!')
        self.balance -= money # 출금
        return money # 출금한 금액을 반환
    
    # 이체 기능
    def transfer(self,your_acc,money): # your_acc: 상대방 계좌, money: 이체할 금액
        your_acc.deposit(self.withdraw(money))

    # 조회 기능
    def inquiry(self):
        print(f'계좌번호 : {self.acc_no}')
        print(f'통장 잔액: {self.balance}')

# 정상 상황
me = BankAccount('012-34-56789', 50000)
you = BankAccount('987-65-43210', 50000)
try:
    me.transfer(you, 5000)
except BankError as e:
    print(e)
finally:
    me.inquiry()
    you.inquiry()



            
