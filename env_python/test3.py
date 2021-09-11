# def max_sub_array(arr, k):
#     # 배열의 최대 구간합, 윈도우 상태, 윈도우 시작지점
#     max_sum = 0
#     window_sum = 0
#     window_start = 0

#     # (1) 윈도우 end 시점을 무조건 당긴다.
#     for window_end in range(len(arr)):
#         # (2) 윈도우 상태 변화
#         window_sum += arr[window_end]  # 슬라이딩 인덱스 범위 요소 합산
#         # (3) 윈도우 크기가 K가 되면 - 윈도우 start 시점 당기기(필요하면)
#         # 슬라이딩 윈도우의 범위가 k 보다 커진 경우
#         if window_end >= (k - 1):  # end_idx가 언제부터 줄여야 할까?
#             # (4) 줄이기전 상태 업데이트 ( 현재 윈도우 상태 - 최대값 추출 )
#             max_sum = max(max_sum, window_sum)
#             window_sum -= arr[window_start]  # 슬라이드 윈도우 범위를 벗어난 요소를 합계에서 제거
#             window_start += 1  # 슬라이드 윈도우 시작 인덱스 증가

#     return max_sum


# if __name__ == '__main__':
#     print(max_sub_array([2, 4, 7, 10, 8, 4], 3))

# # 결과: 25 (7 + 10 + 8)


def max_sub_array(arr, K):
    ansMax = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        print("window_sum", window_sum)
        if window_end >= (K-1):  # 0,1,*2,3,4,5
            ansMax = max(window_sum, ansMax)
            window_sum -= arr[window_start]
            window_start += 1
    return ansMax


print(max_sub_array([2, 4, 7, 10, 8, 4], 3))
