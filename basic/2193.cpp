//https://www.acmicpc.net/problem/5549

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 91
using namespace std;
long long d[SIZE][2];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    d[1][0] = d[2][1] = 0;
    d[1][1] = d[2][0] = 1;
    for (int i = 3; i <= n; i++)
    {
        d[i][0] = d[i - 1][0] + d[i - 1][1];
        d[i][1] = d[i - 1][0];
    }
    cout << d[n][0] + d[n][1];
}