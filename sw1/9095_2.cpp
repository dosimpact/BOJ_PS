//https://www.acmicpc.net/problem/9095
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
int go(int sum, int goal)
{
    if (sum == goal)
        return 1;
    if (sum > goal)
        return 0;
    int ans_node = 0;
    for (int i = 1; i <= 3; i++)
    {
        ans_node += go(sum + i, goal);
    }
    return ans_node;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        cout << go(0, n) << "\n";
    }
}