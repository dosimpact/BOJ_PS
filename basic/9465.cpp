//https://www.acmicpc.net/problem/9465

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 100001
using namespace std;
// fb) d와 p가 크로스 되는 상황이라 헷갈렸다.
long long d[SIZE][3]; // [길이][행]
//int p[SIZE][3] (x)
int p[3][SIZE]; //fb) 행이 1행 2행 있음..
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        for (int i = 1; i <= 2; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                cin >> p[i][j];
            }
        }
        d[1][0] = 0;
        d[1][1] = p[1][1];
        d[1][2] = p[2][1];
        for (int i = 2; i <= n; i++)
        {
            d[i][0] = max(d[i - 1][0], max(d[i - 1][1], d[i - 1][2]));
            d[i][1] = max(d[i - 1][0], d[i - 1][2]) + p[1][i];
            d[i][2] = max(d[i - 1][0], d[i - 1][1]) + p[2][i];
        }
        cout << max(d[n][0], max(d[n][1], d[n][2])) << "\n";
    }
}