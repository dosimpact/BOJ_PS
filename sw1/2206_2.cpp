//https://www.acmicpc.net/problem/2206 리팩토링
#include <cstdio>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#define SIZE 1001
using namespace std;
int check[SIZE][SIZE][2]; //[][][2] -> 0 벽안부 bfs | 1 벽뿌 bfs
int graph[SIZE][SIZE];    //그래프, 노드가 분리되는 경우 - check배열을 2차원으로 둔다.
int n, m;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int main()
{
    //그래프 입력
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%1d", &graph[i][j]);
        }
    }
    fill(&check[0][0][0], &check[0][0][0] + SIZE * SIZE * 2, -1);
    queue<tuple<int, int, int>> q;
    q.push({0, 0, 0});
    check[0][0][0] = 0;
    // 해당 노드의 주변을 탐색합니다. | 범위 체크
    while (!q.empty())
    {
        int x, y, z;
        tie(x, y, z) = q.front();
        q.pop();
        if (x == n - 1 && y == m - 1)
        { //fb) bfs 특성상 가장 먼저 도착하는 노드가 최단거리지.
            printf("%d", check[x][y][z] + 1);
            return 0;
        }
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k], ny = y + dy[k]; //fb) 한번에 정의가 가능함.
            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;
            if (graph[nx][ny] == 0 && check[nx][ny][z] == -1)
            {
                check[nx][ny][z] = check[x][y][z] + 1;
                q.push({nx, ny, z});
            }
            else if (graph[nx][ny] == 1 && z == 0 && check[nx][ny][z + 1] == -1)
            {
                check[nx][ny][z + 1] = check[x][y][z] + 1;
                q.push({nx, ny, z + 1});
            }
        }
    }
    //fb) 도달 못해다면 못가는 경우임.
    printf("%d", -1);
    return 0;
}