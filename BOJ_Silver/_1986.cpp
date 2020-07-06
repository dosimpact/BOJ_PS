//https://www.acmicpc.net/problem/1986
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
int graph[SIZE][SIZE]; // 1 퀸 | 2 나이트 | 3 폰 | 0이번 한번 지나간곳 -1이면 아직 안전

bool isanybody(int i, int j)
{
    return (graph[i][j] == 1 || graph[i][j] == 2 || graph[i][j] == 3);
}
bool inRange(int i, int j)
{
    return ((i > 0) && (j > 0) && (i <= n) && (j <= m));
}
void ChangeQ(int &i, int &j, int k)
{
    int dx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
    int dy[8] = {-1, -1 - 1, 0, 0, 1, 1, 1};
    i = i + dx[k];
    j = j + dy[k];
}
void ChangeHorse(int &i, int &j, int k)
{
    int dx[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
    int dy[8] = {-1, 1, -2, 2, -2, 2, -1, 1};
    i = i + dx[k];
    j = j + dy[k];
}
void Move(int i, int j, int kind)
{
    if (kind == 1)
    {
        //cout << "DEBUG:i,j: " << i << " , " << j << '\n';
        for (int k = 0; k < 8; k++)
        {
            int dx = i, dy = j;
            bool keep = true;
            while (keep)
            {
                ChangeQ(dx, dy, k);
                if (!inRange(dx, dy) || isanybody(dx, dy))
                {
                    keep = false;
                }
                else
                {
                    graph[dx][dy] = 0;
                }
            }
        }
    }
    else if (kind == 2)
    {
        for (int k = 0; k < 8; k++)
        {
            int dx = i, dy = j;
            ChangeHorse(dx, dy, k);
            if (inRange(dx, dy) && !isanybody(dx, dy))
            {
                graph[dx][dy] = 0;
            }
        }
    }
}

int main()
{
    fill(&graph[0][0], &graph[0][0] + SIZE * SIZE, -1);
    cin >> n >> m;
    for (int t = 1; t <= 3; t++)
    {
        int k;
        int i, j;
        cin >> k;
        while (k--)
        {
            cin >> i >> j;
            graph[i][j] = t;
        }
    }
    // for (int i = 1; i <= n; i++)
    // {
    //     for (int j = 1; j <= m; j++)
    //     {
    //         cout << graph[i][j] << "\t";
    //     }
    //     cout << '\n';
    // }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (graph[i][j] == 1)
            {
                Move(i, j, 1);
            }
            else if (graph[i][j] == 2)
            {
                Move(i, j, 2);
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (graph[i][j] == 0)
            {
                ans++;
            }
        }
    }
    // for (int i = 1; i <= n; i++)
    // {
    //     for (int j = 1; j <= m; j++)
    //     {
    //         cout << graph[i][j] << "\t";
    //     }
    //     cout << '\n';
    // }
    cout << ans;
}
