#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
const int MAXN = 500005;
using pi = pair<int, int>;
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()

vector<int> gph[MAXN];
int din[MAXN], dout[MAXN], piv;

void dfs(int x)
{
    din[x] = piv++;
    for (auto &i : gph[x])
        dfs(i);
    dout[x] = piv;
}

int main()
{
    int n;
    scanf("%d", &n);
    int q;
    scanf("%d", &q);
    vector<int> chk(n + 1);
    for (int i = 0; i < n - 1; i++)
    {
        int s, e;
        scanf("%d %d", &s, &e);
        gph[s].push_back(e);
        chk[e] = 1;
    }
    for (int i = 1; i <= n; i++)
        if (!chk[i])
            dfs(i);
    while (q--)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        puts(din[x] <= din[y] && dout[y] <= dout[x] ? "yes" : "no");
    }
}
