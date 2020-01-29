//https://www.acmicpc.net/problem/11052

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 1001
using namespace std;
int p[1001];
int d[1001];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> p[i];
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            d[i] = max(d[i], d[i - j] + p[j]);
        }
    }
    cout << d[n];
}