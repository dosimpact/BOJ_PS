//https://www.acmicpc.net/problem/9519

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
using namespace std;
string next(string s)
{
    stack<char> st;
    string ans;
    for (int i = 0; i < s.size(); i++)
    {
        if (i % 2 == 0)
        {
            ans += s[i];
        }
        else
        {
            st.push(s[i]);
        }
    }
    while (!st.empty())
    {
        ans += st.top();
        st.pop();
    }
    return ans;
}
int main()
{
    int x;
    string s;
    cin >> x >> s;
    vector<string> data;
    data.push_back(s);
    while (true)
    {
        s = next(s);
        if (s != data[0])
        {
            data.push_back(s);
        }
        else
        {
            break;
        }
    }
    cout << data[x % data.size()];
}
