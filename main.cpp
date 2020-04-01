#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define SIZE 10000
vector<int> graph[SIZE];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    for (int i = 1; i <= M; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[b].push_back(a);
    }
    for (int i = 1; i <= N; i++)
    {
        for (auto k : graph[i])
        {
            cout << k << " ";
        }
        cout << "\n";
    }
}