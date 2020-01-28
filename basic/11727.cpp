//https://www.acmicpc.net/problem/11726

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
int dp(int n)
{
    if (n == 1)
    {
        return 1;
    }
    if (n == 2)
    {
        return 3;
    }
    if (d[n])
    {
        return d[n];
    }
    else
    {
        d[n] = dp(n - 1) + dp(n - 2) * 2;
        d[n] = d[n] % 10007;
        return d[n];
    }
}
int main()
{
    int n;
    cin >> n;
    cout << dp(n);
}
