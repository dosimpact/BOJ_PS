# set 함수 정리 (존재성 사용법은 동일)

var = [5, 1, 1, 2, 2, 2, 3, 3, 3, 3]

print(set(var))  # 내부적으로 obj인듯 {1, 2, 3, 5}

var = list(set(var))
var.sort()
print(var)  # unique 중복제거 && 정렬 [1, 2, 3, 5]
