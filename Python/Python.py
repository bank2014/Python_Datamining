import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def Coffeebene_store(result):
    wd = webdriver.Chrome('./chromedriver.exe')             # 프로젝트 경로에 있는 크롬 Webdriver를 객체로 생성
    wd.get('http://www.caffebene.co.kr/store/local.html')   # 카페베네 웹 페이지 URL로 연결
    
    html = wd.page_source                           # 자바스크립트 함수가 수행된 페이지의 소스 코드 저장
    soupCB1 = BeautifulSoup(html, 'html.parser')    # html parser에 의해 파싱된 html 정보를 담은 bs 객체 생성
    
    #print(soupCB1.prettify())                      # html 분석용
    
    for i in range(100):                                        # 100개의 매장 정보를 추출
        store_names = soupCB1.select("li > div > h4")           # li 태그 밑으로 parse-through하여 h4태그 안에 있는 걸 모두 선택
        store_name = store_names[i].string                      # string만 따로 store_name 변수에 담기
        print(store_name)                                       # 콘솔에 매장명 출력

        store_addresses = soupCB1.select("li > div > p.addr")   # 마찬가지로 li 밑에 주소 정보가 있는 <p="addr"> 태그 내용물 선택
        store_address = store_addresses[i].string

        store_tels = soupCB1.select("li > div > p.tel")         # <p="tel"> 태그 내용물 선택
        store_tel = store_tels[i].string

        result.append([store_name]+[store_address]+[store_tel]) # 매장명-주소-전화번호를 result 리스트에 저장

def main():
    result = []
    Coffeebene_store(result)                                            # Coffeebene_store 함수 호출

    CB_tbl = pd.DataFrame(result, columns = ('store', 'address', 'phone'))              # DF의 column명 설정
    CB_tbl.to_csv('./Coffeebene.csv', encoding = 'utf-8-sig', mode = 'w', index = True) # csv파일로 저장

if __name__ == '__main__':
    main()                                                              # main 함수 호출
