//https://www.acmicpc.net/problem/7569

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#define SIZE 101
using namespace std;

int x, y, z;
int graph[SIZE][SIZE][SIZE];
int check[SIZE][SIZE][SIZE];
int dx[6] = {0, 0, 0, 0, 1, -1};
int dy[6] = {0, 0, 1, -1, 0, 0};
int dz[6] = {1, -1, 0, 0, 0, 0};
void bfs()
{
    queue<pair<int, pair<int, int>>> q;
    for (int i = 0; i < z; i++)
    {
        for (int j = 0; j < x; j++)
        {
            for (int k = 0; k < y; k++)
            {
                if (graph[i][j][k] == 1)
                {
                    q.push(make_pair(i, make_pair(j, k)));
                    check[i][j][k] = 1;
                }
            }
        }
    }
    while (!q.empty())
    {
        auto node = q.front();
        q.pop();
        for (int k = 0; k < 6; k++)
        {
            int nx = node.second.first + dx[k];
            int ny = node.second.second + dy[k];
            int nz = node.first + dz[k];
            if (nx < 0 || ny < 0 || nz < 0 || nx >= x || ny >= y || nz >= z)
                continue;
            if (graph[nz][nx][ny] == -1)
                continue;
            if (graph[nz][nx][ny] == 0 && check[nz][nx][ny] == 0)
            {
                q.push(make_pair(nz, make_pair(nx, ny)));
                check[nz][nx][ny] = check[node.first][node.second.first][node.second.second] + 1;
            }
        }
    }
}
int main()
{
    scanf("%d %d %d", &y, &x, &z);
    for (int i = 0; i < z; i++)
    {
        for (int j = 0; j < x; j++)
        {
            for (int k = 0; k < y; k++)
            {
                int ele;
                scanf("%d", &ele);
                graph[i][j][k] = ele;
            }
        }
    }
    bfs();
    int max = 0;
    bool iscannot = false;
    for (int i = 0; i < z; i++)
    {
        for (int j = 0; j < x; j++)
        {
            for (int k = 0; k < y; k++)
            {
                if (graph[i][j][k] == 0 && check[i][j][k] == 0)
                {
                    iscannot = true;
                }
                if (graph[i][j][k] != -1)
                {
                    check[i][j][k] > max ? max = check[i][j][k] : max = max;
                }
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