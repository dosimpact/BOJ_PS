//https://www.acmicpc.net/problem/2606

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#define SIZE 101
using namespace std;

vector<int> graph[SIZE];
int check[SIZE];

void dfs(int x)
{
    check[x] = 1;
    for (int i = 0; i < graph[x].size(); i++)
    {
        int next_node = graph[x][i];
        if (check[next_node] == 0)
        {
            dfs(next_node);
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dfs(1);
    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        if (check[i] == 1)
            ans++;
    }
    cout << ans - 1;
}