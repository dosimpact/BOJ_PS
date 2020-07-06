#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 1001

using namespace std;
int n, m;
int d[SIZE][SIZE];
int graph[SIZE][SIZE];

int dp(int x, int y)
{
    if (x == 0 && y == 0)
    {
        return graph[0][0];
    }
    if (d[x][y] != -1)
    {
        return d[x][y];
    }
    else
    {
        d[x][y] = graph[x][y];
        int max_tmp = 0;
        if (x - 1 >= 0)
        {
            int tmp = dp(x - 1, y);
            if (tmp > max_tmp)
            {
                max_tmp = tmp;
            }
        }
        if (y - 1 >= 0)
        {
            int tmp = dp(x, y - 1);
            if (tmp > max_tmp)
            {
                max_tmp = tmp;
            }
        }
        if (x - 1 >= 0 && y - 1 >= 0)
        {
            int tmp = dp(x - 1, y - 1);
            if (tmp > max_tmp)
            {
                max_tmp = tmp;
            }
        }
        d[x][y] += max_tmp;
        return d[x][y];
    }
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> graph[i][j];
        }
    }
    fill(&d[0][0], &d[0][0] + SIZE * SIZE, -1);
    int res = dp(n - 1, m - 1);
    cout << res;
}