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
    d[1] = p[1];
    d[2] = p[1] + p[2];
    for (int i = 3; i <= n; i++)
    {
        d[i] = max(d[i - 1], max(d[i - 2] + p[i], d[i - 3] + p[i - 1] + p[i]));
    }
    cout << d[n];
}