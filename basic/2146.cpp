//https://www.acmicpc.net/problem/2146

#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int a[100][100]; //원래 지도
int g[100][100]; //그룹
int d[100][100]; //거리
int main()
{
    //지도 입력받기
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int ele;
            scanf("%d", &ele);
            a[i][j] = ele;
        }
    }

    //지도 그룹나누기
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (a[i][j] == 1 && g[i][j] == 0)
            {
                queue<pair<int, int>> q;
                g[i][j] = ++cnt;
                q.push(make_pair(i, j));
                while (!q.empty())
                {
                    auto current = q.front();
                    q.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx = current.first + dx[k];
                        int ny = current.second + dy[k];
                        if (nx >= 0 && ny >= 0 && nx < n && ny < n)
                        {
                            if (a[nx][ny] == 1 && g[nx][ny] == 0)
                            {
                                g[nx][ny] = g[current.first][current.second];
                                q.push(make_pair(nx, ny));
                            }
                        }
                    }
                }
            }
        }
    }

    //**거리 꾸며주기 , -1, 또는 0으로 동시에 queue에 넣기.

    //지도를 돌면서
    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            d[i][j] = -1;
            if (g[i][j] != 0)
            {
                //g가 있으면 0으로 없으면 -1로 꾸며준다.
                //g가 있는 경우에는 d를 큐에 넣어준다.
                d[i][j] = 0;
                q.push(make_pair(i, j));
            }
        }
    } //g가 들어있는 큐를 빼면서
    while (!q.empty())
    {
        auto current = q.front();
        q.pop();
        // g의 주변을 탐색하며
        for (int k = 0; k < 4; k++)
        {
            int nx = current.first + dx[k];
            int ny = current.second + dy[k];
            //범위 | d의 -1인지 | check
            if (nx >= 0 && ny >= 0 && nx < n && ny < n)
            {
                if (d[nx][ny] == -1)
                { // g는 연장 / d는 += 1 를 해주면서 q에 다시 넣어준다.
                    d[nx][ny] = d[current.first][current.second] + 1;
                    g[nx][ny] = g[current.first][current.second];
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
    // printf("\n");
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         printf("%d ", a[i][j]);
    //     }
    //     printf("\n");
    // }

    // printf("\n");
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         printf("%d ", g[i][j]);
    //     }
    //     printf("\n");
    // }

    // printf("\n");
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         printf("%d ", d[i][j]);
    //     }
    //     printf("\n");
    // }
    //정답 추출하기.
    int ans = -1;
    //전체 지도를 돌면서
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                int nx = i + dx[k];
                int ny = j + dy[k];
                if (nx >= 0 && ny >= 0 && nx < n && ny < n)
                {
                    if (g[i][j] != g[nx][ny])
                    { //주변 노드와 그룹이 다르면 // 거리를 합산해서

                        // ans에 최소값을 넣는다.
                        int tmp = d[i][j] + d[nx][ny];
                        if (ans == -1 || ans > tmp)
                        {
                            ans = tmp;
                        }
                    }
                }
            }
        }
    }
    printf("%d", ans);
}