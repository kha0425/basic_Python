# 섹션 18 : 웹 크롤링의 이해

# 일반 웹 페이지 정보 가져오기
# 318p
import requests # http 요청을 수행해야 할 웹페이지의 고스코드를 가져오는 라이브러리

url = 'https://www.naver.com' # 가져올 웹페이지 주소
response = requests.get(url) # 가지고 온 결과를 response 변수에 담는다
print(response.text) # 결과를 텍스트로
print('응답코드 : {}'.format(response.status_code)) # 응답코드

# 
import requests

url = 'https://search.naver.com/search.naver'
param = {'query':'파이썬'} # 검색어
reponse = requests.get(url,params = param)
print(reponse.text)

# BeautifulSoup 메소드 사용하기 - find()
# ex)
from bs4 import BeautifulSoup

html = '''
<div>
    <a href="https://www.naver.com">네이버</a>
    <a href="https://www.kakao.com">카카오</a>
</div>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.find('a')) # 해당 태그 전체(첫번째 태그만)
print(soup.find('a').text) # 태그의 텍스트 부분(내용 부분)
print(soup.find('a').get('href')) # 'href'의 속성값

# BeautifulSoup 메소드 사용하기 - find_all()
# ex)
from bs4 import BeautifulSoup

html = '''
<ul>
    <li id="movie">영화</li>
    <li>여행</li>
    <li>독서</li>
</ul>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all('li')) # 태그 전체(리스트 형식으로)
print(soup.find_all('li')[0])
print(soup.find_all('li')[1])
print(soup.find_all('li')[2])
print(soup.find_all('li')[0].text)
print(soup.find_all('li')[1].text)
print(soup.find_all('li')[2].text)
print(soup.find_all('li')[0].get('id'))

# BeautifulSoup 사용하기 - class 속성
# ex)
from bs4 import BeautifulSoup

html = '''
<div>
    <div class="gnb">뉴스</div>
    <div class="gnb">지도</div>
</div>
'''

soup = BeautifulSoup(html,'html.parser')
print(soup.find_all('div', class_='gnb')) # 속성이 gnb인 태그 전체(리스트형식)
print(soup.find_all('div', class_='gnb')[0].text) # 내용
print(soup.find_all('div', class_='gnb')[1].text)

# BeautifulSoup 사용하기 - id 속성
# ex)
from bs4 import BeautifulSoup

html = '''
<div id="container">
    <div id="left">왼쪽 영역</div>
    <div id="right">오른쪽 영역</div>
</div>
'''

soup = BeautifulSoup(html,'html.parser')
print(soup.find('div', id='left')) # 태그 전체
print(soup.find('div', id='left').text) # 내용
print(soup.find('div', id='right'))
print(soup.find('div', id='right').text)

# ex1) 뉴스 제목
import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net'
reponse = requests.get(url)
html = reponse.text

soup = BeautifulSoup(html,'html.parser')

result = soup.find_all('strong', class_='tit_g')
# print(result)

for i in result:
    print(i.text.strip()) # 양쪽 공백 제거 후 텍스트만 가져온다

# ex2) 주소 찾기
import requests
from bs4 import BeautifulSoup

url = 'http://python.cyber.co.kr/pds/books/python2nd/test2.html'
reponse = requests.get(url)
html = reponse.text

soup = BeautifulSoup(html,'html.parser')

for i in soup.find_all('a'):
    print(i.text) # 내용
    url2 = i.get('href')
    print(url2)

# ex3) 절대 url 표시
import urllib
import requests
from bs4 import BeautifulSoup

url = 'http://python.cyber.co.kr/pds/books/python2nd/test2.html'
reponse = requests.get(url)
html = reponse.text

soup = BeautifulSoup(html,'html.parser')

for i in soup.find_all('a'):
    print(i.text)
    url2 = i.get('href')
    link_url = urllib.parse.urljoin(url,url2) # url 합치다
    print(link_url)

# ex4) 이미지 파일을 읽어들여 저장하기
import requests

# 이미지 파일을 변수에 저장한다.
image_url = 'http://python.cyber.co.kr/pds/books/python2nd/sample1.png'
imgdata = requests.get(image_url)

# url에서 마지막에 있는 파일명을 추출한다.
# print(image_url.split('/')[-1])
filename = image_url.split('/')[-1] 

# 이미지 데이터를 파일에 쓴다.
with open(filename,'wb') as f: # 바이너리 모드로 쓴다.
    f.write(imgdata.content) # 이미지데이터를 쓴다 -> 저장됨
