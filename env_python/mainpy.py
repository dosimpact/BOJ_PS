df_nan = pd.DataFrame({"col1": [1, 2, 3], "col2": [np.nan, 0, np.nan]})
df_nan
df_nan.isna()
df_nan.sum(axis=1)  # nan 무시된다.
print()
df_nan.sum()  # 0축 덧셈 > Series
print()
df_nan.sum().sum()  # 0축 2번 덧셈
