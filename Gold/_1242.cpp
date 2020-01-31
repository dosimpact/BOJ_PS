//https://www.acmicpc.net/problem/1242

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
int n, k, m;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k >> m; // 5 2 3
    int now = m;
    for (int round = 1; round <= n; round++)
    {
        int len = n - (round - 1);
        if (k <= len)
        {
            if (now == k)
            {
                cout << round;
                break;
            }
            else if (now > k)
            {
                now = now - k;
            }
            else if (now < k)
            {
                now = (len - k) + (now);
            }
        }
        else if (k > len)
        {
            k = k % len;
            if (k == 0)
            {
                k = len;
            }
            if (now == k)
            {
                cout << round;
                break;
            }
            else if (now > k)
            {
                now = now - k;
            }
            else if (now < k)
            {
                now = len - k + now;
            }
        }
    }
}