#include <iostream>
#include <algorithm>
using namespace std;

int graph[1001];
bool check[1001];

void dfs(int x)
{
    check[x] = true;
    if (check[graph[x]] == false)
    {
        dfs(graph[x]);
    }
}
int main()
{
    int cases;
    cin >> cases;
    while (cases--)
    {
        int n;
        cin >> n;
        fill(&graph[0], &graph[1001 + 1], 0);
        fill(&check[0], &check[1001 + 1], 0);
        for (int i = 1; i <= n; i++)
        {
            int u;
            cin >> u;
            graph[i] = u;
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
        {
            if (check[i] == false)
            {
                ans++;
                dfs(i);
            }
        }
        cout << ans << "\n";
    }
}