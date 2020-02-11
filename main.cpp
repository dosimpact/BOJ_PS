#include <cstdio>
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 101

using namespace std;
int n, m;
int graph[SIZE][SIZE];
int check[SIZE][SIZE][2]; //0 방문 x | 1이상부터 방문함 + 거리임
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
bool noans = true;

void bfs(int x, int y, int c)
{
    check[x][y][c] = 1;
    deque<tuple<int, int, int>> dq;
    dq.push_back({x, y, c});
    while (!dq.empty())
    {
        tie(x, y, c) = dq.front();
        dq.pop_front();
        if (x == n - 1 && y == m - 1)
        {
            printf("%d", check[x][y][c]);
            noans = false;
            return;
        }
        for (int k = 0; k < 4; k++) // 주변 노드를 탐색
        {

            int nx = x + dx[k], ny = y + dy[k];
            //범위 체크 -> 현재 벽을 안부신경우 -> 그냥이동 또는 부시고 이동 | 부신경우
            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;
            if (c == 0)
            { //범위 체크 -> 현재 벽을 안부신경우 -> 벽이 아닌경우
                if (graph[nx][ny] == 0 && check[nx][ny][c] == 0)
                {
                    check[nx][ny][c] = check[x][y][c] + 1;
                    dq.push_back({nx, ny, c});
                }
                else if (graph[nx][ny] == 1 && check[nx][ny][c] == 0)
                {
                    check[nx][ny][c + 1] = check[x][y][c] + 1;
                    dq.push_back({nx, ny, c + 1});
                }
            }
            else if (c == 1)
            {
                if (graph[nx][ny] == 0 && check[nx][ny][c] == 0)
                {
                    check[nx][ny][c] = check[x][y][c] + 1;
                    dq.push_back({nx, ny, c});
                }
            }
        }
    }
}
int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%1d", &graph[i][j]);
        }
    }
    bfs(0, 0, 0);
    if (noans)
    {
        printf("%d", -1);
    }
}
