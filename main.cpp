#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define SIZE 10000

vector<int> graph[SIZE + 1];
int N, M;
bool check[SIZE + 1];

int dfs(int x)
{
    check[x] = true;
    int tmp = 1;
    for (int i = 0; i < graph[x].size(); i++)
    {
        int nnode = graph[x][i];
        if (!check[nnode])
        {
            tmp += dfs(nnode);
        }
    }
    return tmp;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<int> ansList;
    //입력받기 > M 10만개
    cin >> N >> M;
    for (int i = 1; i <= M; i++)
    {
        int u, v;
        cin >> u >> v; // v를 해킹하면 u가 덤
        graph[v].push_back(u);
    }

    //DFS 돌리기
    int Ans = 0;
    for (int i = 1; i <= N; i++)
    {
        //i번 컴퓨터를 해킹해 본다. -> DFS 를 돌려 덤으로 얻어지는 컴퓨터의 갯수를 알아낸다.
        fill(&check[0], &check[0] + SIZE + 1, false);
        int AnsTmp = 0;
        AnsTmp = dfs(i);
        if (AnsTmp == Ans)
        {
            ansList.push_back(i);
        }
        else if (AnsTmp > Ans)
        {
            ansList.clear();
            Ans = AnsTmp;
            ansList.push_back(i);
        }
    }
    for (auto k : ansList)
    {
        cout << k << " ";
    }
}