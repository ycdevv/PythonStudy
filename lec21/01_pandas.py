# Pandas - Python Data Analysis Library
# 파이썬 수치연산 라이브러리
# 대부분 데이터는 시계열(Series, 단일열)이나 테이블(DataFrame, 복합열)의 형태로 표현 가능

# 1. 시리즈 = 인덱스 + 값
# 1차원 리스트와 유사하지만 각 데이터의 의미를 표시하는 인덱스를 표현 가능
import numpy as np
from operator import index
import pandas as pd

#
# # 시리즈 선언: pd.Series(값 리스트, 인덱스 리스트)
# s = pd.Series([9904312, 3448737, 2890451, 2466052], index=["서울", "부산", "인천", "대구"])

#
# # 인덱스를 지정하지 않고 선언할 경우 인덱스가 자동으로 0부터 시작해 1씩 증가
# nots = pd.Series(range(1, 10))

#
# # 인덱스와 값 리스트를 얻기
# s.index
# s.values
#
# # 인덱스 리스트와, 값 리스트에 각각 이름 붙이기
# s.name = '인구'
# s.index.name = '도시'

#
# # 시리즈 연산
# # 시리즈 사칙 연산시 모든 열값에 적용되어 계산
# # 100만명당 인구수 값 얻기
# s / 1000000
#
# # 시리즈 인덱싱 값 가져오기
# # 인덱스 라벨, 숫자로 가져올 수 있고 인덱스 슬라이싱 가능
# s[0], s['서울']
# s[3], s['대구']
# s[0:2]
# s['서울':'인천']
# s[[0, 1, 2]]
# s[['대구', '서울']]
#
# # 인덱스 마스킹
# # 조건에 맞는 데이터 가져오기
# s > 250e4
# s > 2500000
# s[s > 250e4]
#
# # 인구수 250만 초과, 500만 미만인 경우
# s[(s > 250e4) & (s < 500e4)]
#
# # 시리즈 인덱스
# s.서울
# s.부산
#
# # 인덱스 검색
# '서울' in s
# 'print(''대전' in s
#
# # 시리즈는 인덱스가 키값, 값 Value 딕셔너리와 유사
# # 시리즈와 반복문
# for k, v in s.items():
#     print(k, v)
#
# # 딕셔너리를 통해 시리즈 선언
# s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158})

#
# # 인덱스 지정시 인덱스 순선대로 값이 나열
# s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158}, index=['대전', '인천', '서울', '부산'])

#
# # 두 시리즈의 연산
# # 2015년도와 2010년도 사이의 인구 증가값
# ds = s - s2

#
# # 널이 아닌 데이터 True/False
# ds.notnull()
# ds[ds.notnull()]
#
# # 인구 증가율
# rs = (s - s2) / s2 * 100
# rs.notnull()
# rs[rs.notnull()]
#
# # 수정
# rs['부산'] = 2.4

#
# # 추가
# rs['수원'] = 3.2

#
# # 삭제
# del rs['수원']


# 2. 데이터 프레임 = 인덱스 + 열 + 값
# 여러개의 시리즈를 붙여놓은 것과 유사

# 데이터 프레임 생성
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
index = ["서울", "부산", "인천", "대구"]
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
# 컬럼은 딕셔너리의 Key 값이여서 생략할 수 있음
df = pd.DataFrame(data, index=index, columns=columns)

# 인덱스, 컬럼, 값 리스트(Array) 접근
df.index
df.columns
df.values

# 인덱스와 칼럼 추가
df.index.name = '도시'
df.columns.name = '특성'
df.head()  # 상위 5개 데이터 조회

# 전치행렬 : 열과 행 교환
# 데이터 조회시 유용
df.T

# 열 데이터 수정, 추가, 삭제
# 수정
df['2010-2015 증가율'] = df['2010-2015 증가율'] * 100
df.head()

# 추가
df['2005-2010 증가율'] = ((df['2010'] - df['2005']) / df['2005'] * 100).round(2)
df.head()

# 삭제
del df['2005-2010 증가율']
df.head()

# 열 인덱싱
# 특정 열의 데이터를 가져옴
# 하나의 열 인덱싱시 시리즈 반환
df['지역']
# 두개 이상의 열 인덱싱시 데이터프레임 반환
df[['2010', '2015']]
# 리스트에 열 하나의 이름을 넣으면 데이터프레임 반환
df[['지역']]

# 열 이름이 문자열인 경우에 정수 값으로 열 반환은 불가
# print(df[0])  # 오류

df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
df2
df2[0]
df2[1]

# 행 인덱싱
# 행단위로 인덱싱하려면 반드시 슬라이싱
# df[:1]  # df[0] 오류
# df[1:2]  # df[2] 오류
df[:3]
df['서울':'인천']

# 개별 데이터 인덱싱
# df[열이름][행이름]
df['2015']['서울']

# loc[행 인덱싱값, 열 인덱싱값]
df.loc['서울', '2015']
df.loc['서울']  # 서울인덱스의 행 모든 데이터
df.loc[['서울', '인천'], ['2010', '2015']]
df.loc['서울':'인천', '2015':'2000']

# 파이썬 수치연산 라이브러리
# 대부분 데이터는 시계열(Series, 단일열)이나 테이블(DataFrame, 복합열)의 형태로 표현 가능

# 1. 시리즈 = 인덱스 + 값
# 1차원 리스트와 유사하지만 각 데이터의 의미를 표시하는 인덱스를 표현 가능
import numpy as np
from operator import index
import pandas as pd

#
# # 시리즈 선언: pd.Series(값 리스트, 인덱스 리스트)
# s = pd.Series([9904312, 3448737, 2890451, 2466052], index=["서울", "부산", "인천", "대구"])

#
# # 인덱스를 지정하지 않고 선언할 경우 인덱스가 자동으로 0부터 시작해 1씩 증가
# nots = pd.Series(range(1, 10))

#
# # 인덱스와 값 리스트를 얻기
# s.index
# s.values
#
# # 인덱스 리스트와, 값 리스트에 각각 이름 붙이기
# s.name = '인구'
# s.index.name = '도시'

#
# # 시리즈 연산
# # 시리즈 사칙 연산시 모든 열값에 적용되어 계산
# # 100만명당 인구수 값 얻기
# s / 1000000
#
# # 시리즈 인덱싱 값 가져오기
# # 인덱스 라벨, 숫자로 가져올 수 있고 인덱스 슬라이싱 가능
# s[0], s['서울']
# s[3], s['대구']
# s[0:2]
# s['서울':'인천']
# s[[0, 1, 2]]
# s[['대구', '서울']]
#
# # 인덱스 마스킹
# # 조건에 맞는 데이터 가져오기
# s > 250e4
# s > 2500000
# s[s > 250e4]
#
# # 인구수 250만 초과, 500만 미만인 경우
# s[(s > 250e4) & (s < 500e4)]
#
# # 시리즈 인덱스
# s.서울
# s.부산
#
# # 인덱스 검색
# '서울' in s
# 'print(''대전' in s
#
# # 시리즈는 인덱스가 키값, 값 Value 딕셔너리와 유사
# # 시리즈와 반복문
# for k, v in s.items():
#     print(k, v)
#
# # 딕셔너리를 통해 시리즈 선언
# s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158})

#
# # 인덱스 지정시 인덱스 순선대로 값이 나열
# s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158}, index=['대전', '인천', '서울', '부산'])

#
# # 두 시리즈의 연산
# # 2015년도와 2010년도 사이의 인구 증가값
# ds = s - s2

#
# # 널이 아닌 데이터 True/False
# ds.notnull()
# ds[ds.notnull()]
#
# # 인구 증가율
# rs = (s - s2) / s2 * 100
# rs.notnull()
# rs[rs.notnull()]
#
# # 수정
# rs['부산'] = 2.4

#
# # 추가
# rs['수원'] = 3.2

#
# # 삭제
# del rs['수원']


# 2. 데이터 프레임 = 인덱스 + 열 + 값
# 여러개의 시리즈를 붙여놓은 것과 유사

# 데이터 프레임 생성
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
index = ["서울", "부산", "인천", "대구"]
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
# 컬럼은 딕셔너리의 Key 값이여서 생략할 수 있음
df = pd.DataFrame(data, index=index, columns=columns)

# 인덱스, 컬럼, 값 리스트(Array) 접근
df.index
df.columns
df.values

# 인덱스와 칼럼 추가
df.index.name = '도시'
df.columns.name = '특성'
df.head()  # 상위 5개 데이터 조회

# 전치행렬 : 열과 행 교환
# 데이터 조회시 유용
df.T

# 열 데이터 수정, 추가, 삭제
# 수정
df['2010-2015 증가율'] = df['2010-2015 증가율'] * 100
df.head()

# 추가
df['2005-2010 증가율'] = ((df['2010'] - df['2005']) / df['2005'] * 100).round(2)
df.head()

# 삭제
del df['2005-2010 증가율']
df.head()

# 열 인덱싱
# 특정 열의 데이터를 가져옴
# 하나의 열 인덱싱시 시리즈 반환
df['지역']
# 두개 이상의 열 인덱싱시 데이터프레임 반환
df[['2010', '2015']]
# 리스트에 열 하나의 이름을 넣으면 데이터프레임 반환
df[['지역']]

# 열 이름이 문자열인 경우에 정수 값으로 열 반환은 불가
# print(df[0])  # 오류

df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
df2
df2[0]
df2[1]

# 행 인덱싱
# 행단위로 인덱싱하려면 반드시 슬라이싱
# df[:1]  # df[0] 오류
# df[1:2]  # df[2] 오류
df[:3]
df['서울':'인천']

# 개별 데이터 인덱싱
# df[열이름][행이름]
df['2015']['서울']

# loc[행 인덱싱값, 열 인덱싱값]
df.loc['서울', '2015']
df.loc['서울']
df.loc[['서울', '인천'], ['2010', '2015']]
df.loc['서울':'인천', '2015':'2000']

df.loc[df.지역 == '수도권']
df.loc[df.지역 == '수도권', ['2010', '2005']]
df.loc[df['2010-2015 증가율'] > 3]

# iloc[행인덱스, 열인덱스]
# 순서를 나타내는 정수 인덱스
df.iloc[0]
df.iloc[0:3, 0:4]
df.iloc[[0, 1, 2], [1, 2, 3]]

# 3. 열 집계 함수
df['2010'].mean()  # 평균
df['2010'].min()  # 최소
df['2010'].max()  # 최대
df['2010'].median()  # 중앙값
df['2010'].std()  # 표준편차
df['2010'].describe()  # 수치형 데이터 전체 통계 요약정보
df['지역'].describe()  # 범주형 데이터 요약정보

# 하위 몇 프로 데이터
df['2010'].quantile(0.25)  # 하위 25%(인덱스 기준)에 위치한 데이터 값
df['2010'].quantile(0.5)  # 중앙값
df['2010'].quantile([i * 0.1 for i in range(1, 10)])
df.describe()  # 모든 열에 대한 통계 요약정보

# 열의 정보
df['지역'].size
df.loc['부산', '지역'] = None  # 결측치
df['지역'].count()  # 결측치 제외 데이터 개수, 3
df['지역'].unique()
df['지역'].value_counts()
df['지역'].value_counts(normalize=True)  # 데이터 별 상대 빈도값

# 결측치 채우기
# 모든 결측치에 대한 값을 넣을 수 있음
df['지역'].fillna('경상권')
df['지역'] = df['지역'].fillna('경상권')

# 현재 데이프레임에 변경사항 반영
df['지역'].fillna('경상권', inplace=True)
df['지역']
df.loc['부산', '지역'] = None  # 결측치

# 원본 데이터 결측치 삭제
df.dropna(inplace=True)

# 열 이름 변경
# 변경전 열이름 : 변경후 열이름
colDic = {'2010-2015 증가율': '2010-2015_증가율'}
df.rename(columns=colDic, inplace=True)


