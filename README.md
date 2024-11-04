# python-data-analysis
공공데이터포털(https://www.data.go.kr/) 에서 도로교통공단_가해운전자 연령층별 월별 교통사고 통계_20221231 자료를 이용해 공공데이터 분석을 해보았다.  
![poster](./image-csv.png)

## 선정이유
2024/07/01 시청역 인근 교차로에서 대형 교통사고가 일어났다는 뉴스를 접했다.  
9명이 숨지고 4명이 다치는 큰 사고였다.  
사고 운전자는 급발진을 주장하고, 네티즌의 일부는 사고 운전자의 나이가 60대 후반인 점을 들어, 고령 운전자의 운전 실수가 아니냐는 의견도 있었다.  
이에 대해 고령 운전자의 교통사고 발생량이 그 외의 나이대의 운전자의 교통사고 발생량보다 유의미하게 높은 지 분석하고자 선정했다.

## 데이터구조
각 레이블은 **[가해자연령층, 발생월, 사고건수, 사망자수, 중상자수, 경상자수, 부상신고자수]** 속성들로 이루어져 있다.  
'발생월' 속성은 1월부터 12월까지의 값을 나타내는 int 값을 가지고 있다.  
'가해자연령층' 속성은 '20세 이하', '21세-30세', '31세-40세', '41세-50세', '51세-60세', '61세-64세', '65세 이상', '불명'으로 이루어져 있다.  
'가해자연령층' 속성과 '발생월' 속성을 기준으로 한 해 동안 발생한 사고건수와 사망자수, 부상자수를 분석하고자 한다.

## 데이터 전처리
dataframe의 컬럼별 type 확인 및 결측치 확인을 했다.  
데이터에 결측치가 없고, 데이터 타입이 int64 형으로 일관적이다.  
도로교통공단_가해운전자 연령층별 월별 교통사고 통계의 기타 유의사항으로 ‘부상자수 = 중상자수 + 경상자수 + 부상신고자수’가 있다. 이를 바탕으로 dataframe에 ‘부상자수’ 열을 추가했다.  

'가해자연령층' 속성과 '발생월' 속성을 기준으로 데이터를 분석하고 했기 때문에 두 개의 데이터프레임을 만들었다.
'발생월' 열을 기준으로 전체 연령층의 교통사고 정보를 담는 'total_monthly_Accident',  
'가해자연령층' 열을 기준으로 연령층별 통합 교통사고 정보를 담는 'total_age_Accidnet'를 만들고, 두 개의 데이터프레임으로 그룹핑했다.

## 데이터 시각화
matplotlib.pyplot 라이브러리를 이용해 1월부터 12월까지의 사고건수를 시각화했다.  
월별 통합 사고건수를 시각화하여 몇 월에 가장 사고가 많이 발생하는지 분석했다.  
<img src="/image-graph.png" width="500" height="300">  
그래프를 보면 2월에 사고건수가 가장 적게 일어나고, 10월에 가장 많이 일어나는 것을 알 수 있다.  
기후적으로 눈이 많이 오고, 땅이 미끄러워지는 겨울철 12월부터 2월까지는 오히려 사고건수가 줄어드는 모습을 볼 수 있다.  
여름과 겨울보다, 기후적으로 안정적인 5월과 10월에 교통사고가 유의미하게 늘어나는 것을 알 수 있다.  
  
이는 우리나라의 사계절 특성상, 날이 맑고, 행사를 많이 하는 봄, 가을 시기에 전체적인 교통량의 증가와 관련이 있고, 여행이나 나들이 등의 외부 활동을 많이 하는 시기에 교통사고 또한 증가한다는 사실을 알 수 있다.  
  

