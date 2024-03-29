

# 카드 짝맞추기 보드 게임
# 16장의 카드 , 뒷면 , 4*4
# 8가지 캐럭터 그림 2가지씩, 짝 맞춰서 다 제거하는 미션

# [1] 컨트롤 키, 방향키
# 방향키로 한칸씩 이동 가능

# [1] 컨트롤 +방향키로 , 가까운 카드 혹은 마지막칸으로 이동 가능

# [1] 엔터 키 - 카드 뒤집기
# 뒤집어서 앞면이 한장 - 유지
# 뒤집어서 앞면이 총 2장 - 같으면 사라짐,아니면 뒷면으로
# ----------------------------------------------------------------------

# 자료구조
# # 보드
# # 모든 카드의 위치 , dict[1번 카드] = [(x,y,0),(x,y,0)]
# # 남은 카드 집합 (비트마스크) 선언

# N(16*8+16) < 160 ?
def bfs():
    # 체크 배열 만들기
    # 큐 만들기
    # 4방향을 순회하면서 ,
    # return 목적지라면 거리값 리턴
    # continue 범위
    # continue 이미 방문
    # 한칸씩 이동하는 경우 enQ
    # 쭉 이동하는 경우 for문으로 이동 시도
    # -- (removed - 제거된카드집합) & (1<< 이동하려는보드의 카드 번호) == 0
    # -- break (F) : 제거안되었네 - Blocking
    # -- break 범위 out
    # continue 이미 방문
    # 쭉 이동하는 경우 enQ
    pass

# 지금까지의 조작횟수, 현재 삭제된 카드, (현재 커서의 위치 - x,y,0? )

# (재귀호출 2번)**(카드종류8종) = 2**8 - 백트래킹


def permutate(cnt, removed, src):
    # 글로별 변수 , 최소 조작횟수를 선언

    # BASE CASE 최소 조작 횟수보다 큰 재귀호출이면 return

    # BASE CASE 모든 카드를 제거했다면 , 최소조작횟수 업데이트

    # KEEP  - 모든 카드들을 순회한다.
    # 이미 순회를 한 카드라면 continue
    # one 현재 위치에서 - 첫 카드로 - 두번째 카드로 이동 횟수
    # tow 현재 위치에서 - 두번째 카드 - 첫 카드로 이동 횟수

    # 각각 재귀 호출
    pass


def solution(board, r, c):
    # board를 순회하며, 카드의 위치를 저장한 딕셔너리를 만든다.
    # 카드 번호만큼 남은 카드 집합에 추가

    permutate(0, 1, (r, c, 1))
    return 0

# 제거 순거
# 1 2 3 4 5 6 7 8
# 8!
# 1-1, 1-2
# 16!
