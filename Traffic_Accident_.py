import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('/Users/leesiyoon/Desktop/2024 여름 계절학기/python/과제/도로교통공단.csv', index_col=0)

# 컬럼별 type 확인 및 결측치 확인
df.info()
print(df.isnull().sum())


# 데이터프레임에 새로운 열을 생성 : 부상자수 = 중상자수 + 경상자수 + 부상신고자수
df['부상자수'] = df['중상자수'] + df['경상자수'] + df['부상신고자수']  

# 기초적인 데이터 분석
print(df.describe())

# '발생월' 열을 기준으로 가해자연령층을 구별하지 않고 한 해 동안의 교통사고 분석을 위한 total_monthly_Accident 라는 이름으로 그룹핑
# '가해자연령층' 열을 기준으로 연령대별 교통사고 분석을 위한 total_age_Accident 라는 이름으로 그룹핑
total_monthly_Accident = df.groupby('발생월').sum()
total_age_Accident = df.groupby('가해자연령층').sum()
print(total_age_Accident)
print(total_monthly_Accident)

# 월별 통합 사고건수를 시각화하여 몇 월에 가장 사고가 많이 일어나는지 분석
plt.plot(total_monthly_Accident['사고건수'])
plt.show()

# 가해자연령층별 사고건수를 시각화하여 어느 연령층이 가장 사고를 많이 일으켰는지 분석
total_age_Accident['사고건수'].plot(kind='pie', color=('b', 'orange', 'g', 'm', 'r', 'g', 'purple', 'black'))
plt.show()

# '61-64세' 행의 사고건수와 '65세이상' 행의 사고 건수를 더해 61세 이상의 연령층에서 발생한 사고건수를 출력 
print(total_age_Accident['사고건수'][5]+total_age_Accident['사고건수'][6])

# 가장 많은 사고건수가 발생한 연령층과 월 정보를 추출
print(total_age_Accident.loc[total_age_Accident['사고건수'].idxmax()])
print(total_monthly_Accident.loc[total_monthly_Accident['사고건수'].idxmax()])