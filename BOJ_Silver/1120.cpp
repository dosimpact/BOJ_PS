//https://www.acmicpc.net/problem/1120

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
using namespace std;
string a, b;
int diff(string a, string b)
{
    vector<int> ans;
    int lenmin = min(a.size(), b.size());
    int lendiff = b.size() - a.size();
    for (int i = 0; i <= lendiff; i++) // 7 -  6 => 1 => for: 0 , 1
    {
        int tmp_ans = 0;
        for (int j = 0; j < lenmin; j++)
        {
            if (a[j] != b[j + i])
            {
                tmp_ans++;
            }
        }
        ans.push_back(tmp_ans);
    }
    return *min_element(ans.begin(), ans.end());
}
int main()
{
    cin >> a >> b;
    cout << diff(a, b);
}
