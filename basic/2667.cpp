//2667

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int graph[26][26];
int check[26][26];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
void bfs(int x, int y, int count)
{
    check[x][y] = count;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n)
        {
            if (check[nx][ny] == 0 && graph[nx][ny] == 1)
            {
                bfs(nx, ny, count);
            }
        }
    }
}
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int ele;
            scanf("%1d", &ele);
            graph[i][j] = ele;
        }
    }
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (check[i][j] == 0 && graph[i][j] == 1)
            {
                bfs(i, j, ++count);
            }
        }
    }
    vector<int> ans(count + 1);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            ans[check[i][j]]++;
        }
    }
    printf("%d\n", count);
    sort(ans.begin() + 1, ans.end()); //FB,check가 0인것도 정렬하는데 제외
    for (int i = 1; i <= count - 1; i++)
    {
        printf("%d\n", ans[i]);
    }
}