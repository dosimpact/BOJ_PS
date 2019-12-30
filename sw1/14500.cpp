//https://www.acmicpc.net/problem/14500
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int field[501][501];

int a[19][3][2] = {
    {{0, 1}, {0, 2}, {0, 3}},
    {{1, 0}, {2, 0}, {3, 0}},
    {{1, 0}, {1, 1}, {1, 2}},
    {{0, 1}, {1, 0}, {2, 0}},
    {{0, 1}, {0, 2}, {1, 2}},
    {{1, 0}, {2, 0}, {2, -1}},
    {{0, 1}, {0, 2}, {-1, 2}},
    {{1, 0}, {2, 0}, {2, 1}},
    {{0, 1}, {0, 2}, {1, 0}},
    {{0, 1}, {1, 1}, {2, 1}},
    {{0, 1}, {1, 0}, {1, 1}},
    {{0, 1}, {-1, 1}, {-1, 2}},
    {{1, 0}, {1, 1}, {2, 1}},
    {{0, 1}, {1, 1}, {1, 2}},
    {{1, 0}, {1, -1}, {2, -1}},
    {{0, 1}, {0, 2}, {-1, 1}},
    {{0, 1}, {0, 2}, {1, 1}},
    {{1, 0}, {2, 0}, {1, 1}},
    {{1, 0}, {2, 0}, {1, -1}},

};
int main()
{
    int max = -1;
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int ele;
            cin >> ele;
            field[i][j] = ele;
        }
    }
    int ans = -1;
    //모든 n,m들 돌면서
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            //a의 19개 원소들을 놓아봄
            for (int k = 0; k < 19; k++)
            {
                int tmp_max = field[i][j];
                //현재 점부터, a의 3개더 점을 돌면서
                for (int t = 0; t < 3; t++)
                {
                    int nx = i + a[k][t][0];
                    int ny = j + a[k][t][1];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    {
                        break;
                    } //범위 체크 | 값체크 합 구하기
                    tmp_max += field[nx][ny];
                }
                // 최대값이면ans에 넣기.
                if (ans == -1 || ans < tmp_max)
                {
                    ans = tmp_max;
                }
            }
        }
    }
    cout << ans;
}