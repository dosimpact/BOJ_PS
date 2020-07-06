//https://www.acmicpc.net/problem/9519

#include <iostream>
#include <cstdio>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#include <cmath>
#define SIZE 51
using namespace std;
int graph[SIZE][SIZE];
int n, m;
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            //cin >> graph[i][j];
            scanf("%1d", &graph[i][j]);
        }
    }
    int ans_max = 1;
    int span = min(n, m);
    //전체 배열을 탐색하면서 | 행으로 + 1씩 해가면서 | 범위 체크 | 범위 안이라면 -> 마지막 꼭지점 체크 -> 정답 후보 넣기.
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {

            for (int k = 1; k < span; k++)
            {
                int x = i + k;
                int y = j + k;
                if (x >= n || y >= m)
                    continue;
                if (graph[i][j] == graph[x][j] && graph[i][j] == graph[i][y] && graph[i][j] == graph[x][y])
                {
                    // printf("[%d,%d] : span %d", i, j, k);
                    int tmp = pow(k + 1, 2);
                    if (ans_max < tmp)
                    {
                        ans_max = tmp;
                    }
                }
            }
        }
    }
    cout << ans_max;
}
