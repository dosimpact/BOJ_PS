//https://www.acmicpc.net/problem/5549

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

struct JOI
{
    int j;
    int o;
    int i;
    JOI operator+(JOI &p)
    {

        return {j + p.j, o + p.o, i + p.i};
    }
    JOI operator-(JOI &p)
    {

        return {j - p.j, o - p.o, i - p.i};
    }
};
JOI d[SIZE][SIZE];
int n, m, k;
vector<string> graph;

JOI count(int x, int y)
{
    int a = 0, b = 0, c = 0;
    if (graph[x][y] == 'J')
    {
        a++;
    }
    else if (graph[x][y] == 'O')
    {
        b++;
    }
    else
    {
        c++;
    }
    return {a, b, c};
}

JOI dp(int x, int y)
{
    if (x < 0 || y < 0)
    {
        return {0, 0, 0};
    }
    if (x == 0 && y == 0)
    {
        return count(x, y);
    }
    JOI ans = d[x][y];
    if (ans.j != 0 || ans.o != 0 || ans.i != 0)
    { //메모가 있는경우
        return d[x][y];
    }
    else
    { //메모가 없는경우 | 범위를 체크하면서
        JOI tmp;
        tmp = count(x, y);
        ans = ans + tmp;
        if (x - 1 >= 0)
        {
            tmp = dp(x - 1, y);
            ans = ans + tmp;
        }
        if (y - 1 >= 0)
        {
            tmp = dp(x, y - 1);
            ans = ans + tmp;
        }
        if (x - 1 >= 0 && y - 1 >= 0)
        {
            tmp = dp(x - 1, y - 1);
            ans = ans - tmp;
        }
        d[x][y] = ans;
        return d[x][y];
    }
}

int main()
{
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++)
    {

        string tmp;
        cin >> tmp;
        graph.push_back(tmp);
    }
    for (int i = 0; i < k; i++)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        a -= 2;
        b -= 2;
        c--;
        d--;
        JOI ans1 = dp(c, d), ans2 = dp(a, d), ans3 = dp(c, b), ans4 = dp(a, b);
        JOI ans = ans1 - ans2 - ans3 + ans4;
        cout << ans.j << " " << ans.o << " " << ans.i << "\n";
    }
}
