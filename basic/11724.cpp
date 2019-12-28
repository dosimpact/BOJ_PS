//11724

#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> graph[1001];
bool check[1001];

void dfs(int x)
{
    check[x] = true; //printf("%d ",x);
    for (int i = 0; i < graph[x].size(); i++)
    {
        int node = graph[x][i];
        if (!check[node])
        {
            dfs(node);
        }
    }
}
void bfs(int x)
{
    queue<int> q;
    q.push(x);
    check[x] = true;
    printf("%d ", x);
    while (!q.empty())
    {
        int now = q.front();
        q.pop();
        for (int i = 0; i < graph[now].size(); i++)
        {
            int next = graph[now][i];
            if (!check[next])
            {
                check[next] = true;
                printf("%d ", next);
                q.push(next);
            }
        }
    }
}
int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for (int i = 0; i <= n; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }
    int component = 0;
    for (int i = 1; i <= n; i++)
    {
        if (!check[i])
        {
            component++;
            dfs(i);
        }
    }
    printf("%d", component);
}