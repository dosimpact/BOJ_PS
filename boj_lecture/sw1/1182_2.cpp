//https://www.acmicpc.net/problem/1182
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

int n, s;
int a[20];
int ans;

void go(int sum, int index)
{
    //ÀÎµ¦½º ³¡ÀÌ
    if (index == n)
    {
        if (sum == s)
        {
            ans++;
        }
        return;
    }
    go(sum + a[index], index + 1);
    go(sum, index + 1);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> s;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        a[i] = tmp;
    }
    go(0, 0);
    if (s == 0)
    {
        ans--;
    }
    cout << ans;
}