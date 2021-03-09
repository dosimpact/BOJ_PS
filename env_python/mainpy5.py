def spread(virus_y, virus_x):  # 바이러스 전파 알고리즘 (BFS)
    queue = []
    queue.append([virus_y, virus_x])
    while queue:
        y, x = map(int, queue.pop(0))
        lab_temp[y][x] = 2
        # 바이러스의 x좌표가 0보다 크고, 바이러스 왼쪽 칸이 빈 칸인 경우
        if x > 0 and lab_temp[y][x - 1] == 0 and not visited[y][x - 1]:
            visited[y][x - 1] = True
            queue.append([y, x - 1])
        # 바이러스의 y좌표가 0보다 크고, 바이러스 위쪽 칸이 빈 칸인 경우
        if y > 0 and lab_temp[y - 1][x] == 0 and not visited[y - 1][x]:
            visited[y - 1][x] = True
            queue.append([y - 1, x])
        # 바이러스의 x좌표가 m-1보다 작고, 바이러스 오른쪽 칸이 빈 칸인 경우
        if x < m - 1 and lab_temp[y][x + 1] == 0 and not visited[y][x + 1]:
            visited[y][x + 1] = True
            queue.append([y, x + 1])
        # 바이러스의 y좌표가 n-1보다 작고, 바이러스 아래쪽 칸이 빈 칸인 경우
        if y < n - 1 and lab_temp[y + 1][x] == 0 and not visited[y + 1][x]:
            visited[y + 1][x] = True
            queue.append([y + 1, x])


result = 0
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 초기 바이러스 좌표 구하기
virus = [[i, j] for i in range(n) for j in range(m) if lab[i][j] == 2]
# 빈 칸의 좌표 List
empty = [[i, j] for i in range(n) for j in range(m) if lab[i][j] == 0]
# 벽 세 칸을 세우는 모든 경우를 저장하는 리스트
l_case = [[empty[i], empty[j], empty[k]] for i in range(
    len(empty)) for j in range(i + 1, len(empty)) for k in range(j + 1, len(empty))]
# 모든 경우에 대한 검사
for case in l_case:
    # 지도 복사 (이차원 배열의 깊은 복사)
    lab_temp = [[lab[i][j] for j in range(m)] for i in range(n)]
    # 방문 검사를 위한 리스트
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 벽 세우기
    for c in case:
        y, x = c[0], c[1]
        lab_temp[y][x] = 1
    # 바이러스 전파
    for v in virus:
        spread(v[0], v[1])
    # 안전 구역 개수 세기
    count = len([[i, j] for i in range(n)
                 for j in range(m) if lab_temp[i][j] == 0])
    # 기존 안전 구역과 비교 후 많으면 재할당
    if count > result:
        result = count
print(result)
