//1260

#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> graph[1001];
bool check[1001];

void dfs(int x)
{
    check[x] = true;
    printf("%d ", x);
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
    int n, m, v;
    scanf("%d %d %d", &n, &m, &v);
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
    dfs(v);
    printf("\n");
    fill(check, check + sizeof(check), 0);
    bfs(v);
}