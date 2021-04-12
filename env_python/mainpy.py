
# finance_datareader

# 설치 및 임포트
# !pip install finance_datareader
import FinanceDataReader as fdr


# 데이터 읽기
# KODEX 200 (ETF)
df2 = fdr.DataReader("069500", '2018-01-02', '2018-10-30')

eg)

import FinanceDataReader as fdr
# 예제 - ETF로 reindexing (삼전의 2번째 날의 데이터가 사라졌다.)
# 삼전(005930),코덱스200(069500)
df1=fdr.DataReader('005930', '2018-01-02', '2018-10-30')
df2=fdr.DataReader('069500', '2018-01-02', '2018-10-30')
df1=df1.drop(pd.to_datetime('2018-01-03'))
df1.shape, df2.shape
# df1.head()
# df2.index # dtype='datetime64[ns]'
df1=df1.reindex(df2.index, method = "ffill")
df1.head()
