//https://www.acmicpc.net/problem/9095

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
using namespace std;
int d[1001];

int dp2(int n)
{
    d[1] = 1;
    d[2] = 2;
    d[3] = 4;
    for (int i = 4; i <= n; i++)
    {
        d[i] = d[i - 1] + d[i - 2] + d[i - 3];
    }
    return d[n];
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        cout << dp2(n) << "\n";
    }
}
