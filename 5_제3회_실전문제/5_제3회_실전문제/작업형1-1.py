######################################
# Q1.제1유형(10점) : 데이터 처리 & 통계
######################################

# 유형1 : 전처리 후 통계 구하기 
# 제출 : print(result) 

'''
 문1) 결측치를 포함하는 모든 행을 제거한 후, 상위 70% 데이터에서 
      mpg컬럼의 제3사분위수를 정수로 출력하시오.      
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\5_제3회_실전문제\data'
a = pd.read_csv(path +'/mtcars.csv')  

target = a.dropna()
target.isnull().sum()

target2 = target.head(int(len(target)*0.7))
# target2 = target.iloc[:len(target)*0.7]

target.shape
target2.shape

result = target2['mpg'].quantile(0.75)
result = int(result)
print(result)
