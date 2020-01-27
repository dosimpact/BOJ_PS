//https://www.acmicpc.net/problem/2206 리팩토링
#include <cstdio>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#define SIZE 101
using namespace std;
int check[SIZE][SIZE]; //[][][2] -> 0 벽안부 bfs | 1 벽뿌 bfs
int graph[SIZE][SIZE]; //그래프, 노드가 분리되는 경우 - check배열을 2차원으로 둔다.
int n, m;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int main()
{
    //그래프 입력
    scanf("%d %d", &m, &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%1d", &graph[i][j]);
        }
    }
    fill(&check[0][0], &check[0][0] + SIZE * SIZE, -1);
    //0,0부터 탐색을 시작한다.
    deque<pair<int, int>> dq;
    dq.push_back({0, 0});
    check[0][0] = 0;
    while (!dq.empty())
    { //현재 노드에서 탐색 | 범위 체크 | 방문 여부 체크
        int x, y;
        tie(x, y) = dq.front();
        dq.pop_front();
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;
            if (check[nx][ny] != -1)
                continue;
            if (graph[nx][ny] == 0) // grpah가 0인경우 | push_front 하고 , + 0 가중치
            {
                check[nx][ny] = check[x][y];
                dq.push_front({nx, ny});
            }
            else if (graph[nx][ny] == 1) //graph 가 1인경우 | push_back 하고 , + 1 가중치
            {
                check[nx][ny] = check[x][y] + 1;
                dq.push_back({nx, ny});
            }
        }
    }
    printf("%d", check[n - 1][m - 1]);
}