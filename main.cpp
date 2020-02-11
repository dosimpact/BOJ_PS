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
int x, y;
int graph[SIZE][SIZE];
int check[SIZE][SIZE];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

//덱을 이용한 탐사 : check배열에 결과가 나오는데, 가중치가 1인경우 check++, 가중치가 0인경우 check 그래도
void bfs(int x, int y)
{
    //현재 위치를 방문체크 | 주변 노드를 탐색 | 가중치가 0인경우 -> ... | 가중치가 1인경우 -> ...
    check[x][y] = 0;
    deque<pair<int, int>> dq;
    dq.push_back({x, y});
    while (!dq.empty())
    {
        tie(x, y) = dq.front();
        dq.pop_front();
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if ((nx >= 0 && ny >= 0 && nx < x && ny < y) && check[nx][ny] == -1)
            {
                if (graph[nx][ny] == 0)
                {
                    check[nx][ny] = check[x][y];
                    dq.push_front({nx, ny});
                }
                else
                {
                    check[nx][ny] = check[x][y] + 1;
                    dq.push_back({nx, ny});
                }
            }
        }
    }
}
int main()
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            cin >> graph[i][j];
            scanf("%1d", &graph[i][j]);
        }
    }
    fill(&check[0][0], &check[0][0] + SIZE * SIZE, -1);
    bfs(0, 0);
    cout << check[x - 1][y - 1];
}
