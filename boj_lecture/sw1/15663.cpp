//https://www.acmicpc.net/problem/15663

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int c[10];
int a[10];
int num[10];
int n, m;
vector<vector<int>> ans;
void printArray()
{
    vector<int> tmp_ans;
    for (int i = 0; i < m; ++i)
    {

        tmp_ans.push_back(num[a[i]]);
    }
    ans.push_back(tmp_ans);
}
//a curosr
void go(int ac, int start)
{
    //다고른경우
    if (ac == m)
    {
        printArray();
        return;
    }
    for (int i = start; i < n; i++)
    {
        a[ac] = i;
        go(ac + 1, i + 1);
    }
}
void _go(int ac)
{
    //다고른경우
    if (ac == m)
    {
        printArray();
        return;
    }
    for (int i = 0; i < n; i++)
    {
        if (c[i] == 1)
            continue;
        c[i] = 1;
        a[ac] = i;
        _go(ac + 1);
        c[i] = 0;
    }
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        num[i] = (tmp);
    }
    sort(num, num + n);
    _go(0);
    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());
    for (int i = 0; i < ans.size(); i++)
    {
        for (int j = 0; j < ans[i].size(); j++)
        {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
}