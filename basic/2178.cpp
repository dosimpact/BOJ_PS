//https://www.acmicpc.net/problem/2178

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#define SIZE 101
using namespace std;

int n, m;
int graph[SIZE][SIZE];
int check[SIZE][SIZE];
int dx[8] = {0, 0, 1, -1};
int dy[8] = {1, -1, 0, 0};

void bfs(int x, int y)
{
    queue<pair<int, int>> q;
    q.push(make_pair(x, y));
    check[x][y] = 1;
    while (!q.empty())
    {
        auto node = q.front();
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = node.first + dx[k];
            int ny = node.second + dy[k];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;
            if (graph[nx][ny] == 1 && check[nx][ny] == 0)
            {
                q.push(make_pair(nx, ny));
                check[nx][ny] = check[node.first][node.second] + 1;
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
            int ele;
            scanf("%1d", &ele);
            graph[i][j] = ele;
        }
    }
    bfs(0, 0);
    printf("%d", check[n - 1][m - 1]);
}