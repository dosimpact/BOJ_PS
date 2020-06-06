//https://www.acmicpc.net/problem/13023
#include <iostream>
#include <tuple>
#include <algorithm>
#include <cstring>
#include <queue>
#include <string>
#define SIZE 2001
using namespace std;
vector<int> graph[SIZE];
int check[SIZE];

bool dfs(int current)
{
    if (check[current] == 5)
    {
        return true;
    }

    for (int i = 0; i < graph[current].size(); i++)
    {
        int next = graph[current][i];
        if (check[next] == 0)
        {
            check[next] = check[current] + 1;
            if (dfs(next))
            {
                return true;
            }
            check[next] = 0;
        }
    }
    return false;
}

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int from, to;
        cin >> from >> to;
        graph[from].push_back(to);
        graph[to].push_back(from);
    }
    //0번 노드부터 check를 하나씩 늘려가며 bfs를 돈다. 처음 check는 1이고, 1,2,3,4,5 가 발견되면, 종료.
    for (int i = 0; i < n; i++)
    {
        fill(&check[0], &check[0] + SIZE, 0);
        check[i] = 1;
        if (dfs(i))
        {
            cout << 1;
            return 0;
        }
    }
    cout << 0;
}
