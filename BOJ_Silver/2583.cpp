//https://www.acmicpc.net/problem/2583
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#define SIZE 101
using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int check[SIZE][SIZE];
int graph[SIZE][SIZE];
int n, m, k;

int dfs(int x, int y)
{
    int counter = 0;
    check[x][y] = 1;
    for (int k = 0; k < 4; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx >= 0 && ny >= 00 & nx < m && ny < n)
        {
            if (check[nx][ny] == 0 && graph[nx][ny] == 1)
            {
                counter += 1;
                counter += dfs(nx, ny);
            }
        }
    }
    return counter;
}
int main()
{
    fill(&graph[0][0], &graph[0][0] + SIZE * SIZE, 1);
    cin >> m >> n >> k;
    for (int i = 0; i < k; i++)
    {

        int sx, sy, ex, ey;
        cin >> sx >> sy >> ex >> ey; //0 2 4 4
        for (int x = sx; x < ex; x++)
        {
            for (int y = sy; y < ey; y++)
            {
                graph[y][x] = 0;
            }
        }
    }
    int ans_component = 0;
    vector<int> ans_width;
    for (int x = 0; x < m; x++)
    {
        for (int y = 0; y < n; y++)
        {
            if (check[x][y] == 0 && graph[x][y] == 1)
            {
                ans_component++;
                int tmp = dfs(x, y);
                ans_width.push_back(tmp + 1);
            }
        }
    }
    cout << ans_component << "\n";
    sort(ans_width.begin(), ans_width.end());
    for (auto it = ans_width.begin(); it != ans_width.end(); it++)
    {
        cout << *it << " ";
    }
}
