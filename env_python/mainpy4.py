from collections import deque
import sys

r,c,t=map(int,input().split())
graph=[]
for i in range(r):
    graph.append(list(map(int,sys.stdin.readline().split())))

q=deque()
for i in range(r):
    for j in range(c):
        if graph[i][j]>0:
            q.append((i,j,graph[i][j]))
        if graph[i][j]==-1:
            up=i-1
            down=i

dx=[-1,1,0,0]
dy=[0,0,1,-1]
#미세먼지
def bfs():
    global q, graph
    while q:
        x,y, value=q.popleft()
        count=0     #확산된 방향의 개수
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위를 벗어나면
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            #공기청정기가 있으면
            if graph[nx][ny]==-1:
                continue
            graph[nx][ny]+=int(value//5)
            count+=1
        graph[x][y]-=int(value//5*count)

#공기청정기 위
def Up():
    global graph
    valuelist=[]
    #왼쪽 아래->오른쪽 아래
    for i in range(1, c):
        valuelist.append(graph[up][i])
    #오른쪽 아래->오른쪽 위
    for i in range(up-1, -1, -1):
        valuelist.append(graph[i][c-1])
    #오른쪽 위->왼쪽 위
    for i in range(c-2, -1, -1):
        valuelist.append(graph[0][i])
    #왼쪽 위->왼쪽 아래
    for i in range(1, up):
        valuelist.append(graph[i][0])
    #한칸씩밀기
    valuelist.pop()
    valuelist.insert(0,0)
    # 왼쪽 아래->오른쪽 아래
    for i in range(1, c):
        graph[up][i]=valuelist.pop(0)
    # 오른쪽 아래->오른쪽 위
    for i in range(up - 1, -1, -1):
        graph[i][c - 1]=valuelist.pop(0)
    # 오른쪽 위->왼쪽 위
    for i in range(c - 2, -1, -1):
        graph[0][i]=valuelist.pop(0)
    # 왼쪽 위->왼쪽 아래
    for i in range(1, up):
        graph[i][0]=valuelist.pop(0)

#공기청정기 아래
def Down():
    global graph
    valuelist=[]
    #왼쪽 위->오른쪽 위
    for i in range(1, c):
        valuelist.append(graph[down][i])
    #오른쪽 위->오른쪽 아래
    for i in range(down+1, r):
        valuelist.append(graph[i][c-1])
    #오른쪽 아래->왼쪽 아래
    for i in range(c-2, -1, -1):
        valuelist.append(graph[r-1][i])
    #왼쪽 아래->왼쪽 위
    for i in range(r-2, down,-1):
        valuelist.append(graph[i][0])
    #한칸씩밀기
    valuelist.pop()
    valuelist.insert(0,0)
    # 왼쪽 위->오른쪽 위
    for i in range(1, c):
        graph[down][i]=valuelist.pop(0)
    # 오른쪽 위->오른쪽 아래
    for i in range(down + 1, r):
        graph[i][c - 1]=valuelist.pop(0)
    # 오른쪽 아래->왼쪽 아래
    for i in range(c - 2, -1, -1):
        graph[r - 1][i]=valuelist.pop(0)
    # 왼쪽 아래->왼쪽 위
    for i in range(r-2, down, -1):
        graph[i][0]=valuelist.pop(0)

for aaa in range(t):
    bfs()
    Up()
    Down()
    for i in range(r):
        for j in range(c):
            if graph[i][j]>0:
                q.append((i,j,graph[i][j]))

result=0
for i in range(r):
    for j in range(c):
        if graph[i][j]>0:
            result+=graph[i][j]
print(result)