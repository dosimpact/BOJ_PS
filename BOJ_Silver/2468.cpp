//https://www.acmicpc.net/problem/2468
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#define SIZE 101
using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int check[SIZE][SIZE];
int graph[SIZE][SIZE];
int n;
vector<int> ans;
void dfs(int depth, int x, int y)
{
    for (int k = 0; k < 4; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx >= 0 && ny >= 0 && nx < n && ny < n)
        {
            if (check[nx][ny] == 0 && graph[nx][ny] > depth)
            {
                check[nx][ny] = 1;
                dfs(depth, nx, ny);
            }
        }
    }
}
int main()
{
    int graph_max = -1;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
            if (graph_max == -1 || graph[i][j] > graph_max)
            {
                graph_max = graph[i][j];
            }
        }
    }
    //높이는 1이상 100이하의 정수이므로.
    for (int depth = 0; depth <= graph_max; depth++)
    {
        fill(&check[0][0], &check[0][0] + SIZE * SIZE, 0);
        int components = 0;
        //방문하지 않았고, 높이가,
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (check[i][j] == 0 && graph[i][j] > depth)
                {
                    check[i][j] = 1;
                    components += 1;
                    dfs(depth, i, j);
                }
            }
        }
        ans.push_back(components);
    }
    //1 초과인 지역은 dfs해서 , 컴포넌트의 갯수 구하기.
    cout << *max_element(ans.begin(), ans.end());
}
