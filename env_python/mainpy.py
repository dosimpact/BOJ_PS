# eg) 인공지능, 데이터 마이닝 수업의 점수 합계를 구해라
# 1. 인공지능 새로운 학생 들어옴
# 2. 이때, 데이터마이닝 수업에 index 얼라인을 맞추고 합계
# 3. 새로운 학생 추가 , ffill 이용

lecture_index = ['321600', '321601', '321602']
lecture_colums = ['midterm', 'final']

df_ai = pd.DataFrame([[50, 50], [45, 40], [30, 20]],
                     index=lecture_index,
                     columns=lecture_colums)
df_da = pd.DataFrame({
    lecture_colums[0]: [50, 50, 50],
    lecture_colums[1]: [10, 20, 15]
}, index=lecture_index)

df_ai.loc['321603'] = [50, 50]  # 1
df_da = df_da.reindex(df_ai.index).replace(np.nan, 0)
df_sum = df_ai + df_da  # -> 2 출력

df_ai.loc['321604'] = [10, 10]
# df_da.reindex(df_ai.index,fill_value="RE")
df_da = df_da.reindex(df_ai.index, method="ffill")
df_sum = df_ai + df_da  # -> 2 출력

df_sum
"""
midterm final
321600 100.000 60.000
321601 95.000 60.000
321602 80.000 35.000
321603 50.000 50.000
321604 10.000 10.000
"""
