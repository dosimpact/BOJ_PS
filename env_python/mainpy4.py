df = pd.read_csv(prefix_path+"my_data/naver_finance/2015_12.csv")


# 데이터 자체에 대한 정보
df.shape
df.describe().T # 옆으로 길어질때 사용!
df.describe(include=[np.number]).T # 특정 타입만 알아보기
df.describe(exclude=[np.number]).T
#* int,int64,float,float64
#* np.object,np.float,np.float64,

# percentiles 옵션
df.describe(percentiles=[0.01,0.03,0.99]).T
df['PBR(배)'].quantile([0.2,0.3,0.99])
df['PBR(배)'].quantile(0.2)


# 데이터 타입에 대한 정보

df.info() # 컬럼명-Count,Dtype 등
df.dtypes.value_counts() # 플롯형 15개, obj형 1개
df.dtypes.values # -> 컬럼dtype리스트 반환
df['ticker'].dtype # 특정 컬럼 dtype('O')

# 데이터 타입 수정 
df = df.rename(columns={"ticker":"종목명"}) # 컬럼명 rename
