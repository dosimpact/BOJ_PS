//https://www.acmicpc.net/problem/2156

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 10001
using namespace std;
int d[SIZE][3]; // 0번 역속 1번연속 2번연속
int p[SIZE];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> p[i];
    }
    d[1][0] = 0;
    d[1][1] = p[1];
    d[1][2] = 0;
    for (int i = 2; i <= n; i++)
    {
        d[i][0] = max(d[i - 1][0], max(d[i - 1][1], d[i - 1][2]));
        d[i][1] = d[i - 1][0] + p[i];
        d[i][2] = d[i - 1][1] + p[i];
    }
    cout << max(d[n][0], max(d[n][1], d[n][2]));
}