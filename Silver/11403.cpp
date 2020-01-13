//https://www.acmicpc.net/problem/11403
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#define SIZE 101
using namespace std;

int check[SIZE];
int graph[SIZE][SIZE];
int n;
void dfs(int x)
{
    for (int i = 1; i <= n; i++)
    {
        if (graph[x][i] == 1 && check[i] == 0)
        {
            check[i] = 1;
            dfs(i);
        }
    }
}
int main()
{
    int ans_graph[SIZE][SIZE];
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> graph[i][j];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        fill(&check[0], &check[0] + SIZE, 0);
        //dfs 탐색을 하고
        dfs(i);
        //결과 c를 ans graph의 첫행으로 복사한다.
        for (int k = 1; k <= n; k++)
        {
            ans_graph[i][k] = check[k];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cout << ans_graph[i][j] << " ";
        }
        cout << "\n";
    }
}
