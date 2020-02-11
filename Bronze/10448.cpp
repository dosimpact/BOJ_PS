//https://www.acmicpc.net/problem/10448
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

int ans_list[4000];
int t[45];
int main()
{
    t[1] = 1;
    for (int i = 2; i <= 45; i++)
    {
        t[i] = t[i - 1] + i;
    }
    for (int i = 1; i <= 45; i++)
    {
        for (int j = 1; j <= 45; j++)
        {
            for (int k = 1; k <= 45; k++)
            {
                ans_list[t[i] + t[j] + t[k]] = 1;
            }
        }
    }
    int tc;
    cin >> tc;
    while (tc--)
    {
        int tmp;
        cin >> tmp;
        cout << ans_list[tmp] << '\n';
    }
}