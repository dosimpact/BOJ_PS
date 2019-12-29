//https://www.acmicpc.net/problem/7576

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#define SIZE 1001
using namespace std;

int n, m;
int graph[SIZE][SIZE];
int check[SIZE][SIZE];
int dx[8] = {0, 0, 1, -1};
int dy[8] = {1, -1, 0, 0};

void bfs()
{
    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (graph[i][j] == 1)
            {
                q.push(make_pair(i, j));
                check[i][j] = 1;
            }
        }
    }
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
            if (graph[nx][ny] == -1)
                continue;
            if (graph[nx][ny] == 0 && check[nx][ny] == 0)
            {
                q.push(make_pair(nx, ny));
                check[nx][ny] = check[node.first][node.second] + 1;
            }
        }
    }
}
int main()
{
    scanf("%d %d", &m, &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int ele;
            scanf("%d", &ele);
            graph[i][j] = ele;
        }
    }
    bfs();
    int max = 0;
    bool iscannot = false;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (graph[i][j] == 0 && check[i][j] == 0)
            {
                iscannot = true;
            }
            if (graph[i][j] != -1)
            {
                check[i][j] > max ? max = check[i][j] : max = max;
            }
        }
    }
    if (iscannot)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n", max - 1);
    }
}