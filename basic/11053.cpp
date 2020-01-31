//https://www.acmicpc.net/problem/11053

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
int d[SIZE]; //
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
    for (int i = 1; i <= n; i++)
    {
        d[i] = 1;
        for (int j = 1; j < i; j++)
        {
            if (p[j] < p[i] && d[i] < d[j] + 1)
            {
                d[i] = d[j] + 1;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        ans = max(d[i], ans);
    }
    cout << ans;
}