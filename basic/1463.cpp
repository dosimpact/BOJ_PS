//https://www.acmicpc.net/problem/1463

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#define SIZE 1000000
using namespace std;

int d[SIZE];
int dp(int n)
{
    //base 케이스
    if (n <= 1)
    {
        return 0;
    }
    //메모가 있는 경우 | 없는 경우
    if (d[n])
    {
        return d[n];
    }
    else
    { //1빼는 경우, 2나누어떨어지는 경우, 3나눠떨
        d[n] = dp(n - 1) + 1;
        if (n % 2 == 0)
        {
            int tmp = dp(n / 2) + 1;
            if (tmp < d[n])
                d[n] = tmp;
        }
        if (n % 3 == 0)
        {
            int tmp = dp(n / 3) + 1;
            if (tmp < d[n])
                d[n] = tmp;
        }
        return d[n];
    }
}
int dp2(int n)
{
    d[1] = 0;
    for (int i = 2; i <= n; i++)
    {
        d[i] = d[i - 1] + 1;
        if (i % 2 == 0 && d[i] > d[i / 2] + 1)
        {
            d[i] = d[i / 2] + 1;
        }
        if (i % 3 == 0 && d[i] > d[i / 3] + 1)
        {
            d[i] = d[i / 3] + 1;
        }
    }
    return d[n];
}
int main()
{
    int n;
    cin >> n;
    cout << dp(n);
}
