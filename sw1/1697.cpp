//https://www.acmicpc.net/problem/1697
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define SIZE 100001
using namespace std;
int n, k;
bool check[SIZE];
int dist[SIZE];
void bfs()
{
    queue<int> q;
    q.push(n);
    check[n] = true;
    dist[n] = 0;
    while (!q.empty())
    {
        int now = q.front();
        q.pop();
        if (now == k)
        {
            cout << dist[now];
            return;
        }
        if (now + 1 <= SIZE)
        {
            if (check[now + 1] == false)
            {
                check[now + 1] = true;
                dist[now + 1] = dist[now] + 1;
                q.push(now + 1);
            }
        }
        if (now - 1 >= 0)
        {
            if (check[now - 1] == false)
            {
                check[now - 1] = true;
                dist[now - 1] = dist[now] + 1;
                q.push(now - 1);
            }
        }
        if (now * 2 <= SIZE)
        {
            if (check[now * 2] == false)
            {
                check[now * 2] = true;
                dist[now * 2] = dist[now] + 1;
                q.push(now * 2);
            }
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k;
    bfs();
}
