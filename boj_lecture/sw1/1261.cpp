//https://www.acmicpc.net/problem/1261
#include <cstdio>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#define SIZE 101
using namespace std;
int d[SIZE][SIZE];     // -1 초기값
int graph[SIZE][SIZE]; // 입력
int ans[SIZE][SIZE];
int X, Y;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int main()
{
    scanf("%d %d", &Y, &X);
    for (int i = 1; i <= X; i++)
    {
        for (int j = 1; j <= Y; j++)
        {
            scanf("%1d", &graph[i][j]);
        }
    }

    fill(&d[0][0], &d[0][0] + SIZE * SIZE, -1);
    deque<pair<int, int>> dq;
    dq.push_back({1, 1});
    d[1][1] = 0;
    while (!dq.empty())
    {
        //해당 노드
        int x, y;
        tie(x, y) = dq.front();
        dq.pop_front();
        // 주변을 탐색하면서 | 범위 체크 | 간적이 없다면 |
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx > 0 && ny > 0 && nx <= X && ny <= Y)
            {
                if (d[nx][ny] == -1)
                {
                    if (graph[nx][ny] == 0) // 벽을 안부시고 갈수 있는경우 | 가중치 0방문 | 덱 앞에 넣기
                    {
                        d[nx][ny] = d[x][y];
                        dq.push_front({nx, ny});
                    }
                    else if (graph[nx][ny] == 1) // 벽을 부셔야 되는 경우 | 가충치 +1 방문 | 덱 뒤에 넣기
                    {
                        d[nx][ny] = d[x][y] + 1;
                        dq.push_back({nx, ny});
                    }
                }
            }
        }
    }
    printf("%d", d[X][Y]);
}