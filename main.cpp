#include <cstdio>
#include <algorithm>
using namespace std;
int n, l, a, b, c, pcnt;
pair<int, int> p[100000];
int main()
{
    scanf("%d %d", &n, &l);
    for (int i = 1, x; i <= n; i++)
    {
        scanf("%d", &x);
        if (x < 0)
            c++, a = -x > a ? -x : a;
        else
            b = l - x > b ? l - x : b;
        p[pcnt++] = {abs(x), i};
    }
    sort(p, p + pcnt);
    if (a > b)
        printf("%d %d", p[c - 1].second, a);
    else
        printf("%d %d", p[c].second, b);
    return 0;
}