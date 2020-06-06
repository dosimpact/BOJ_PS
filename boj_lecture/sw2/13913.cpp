//https://www.acmicpc.net/problem/13913
// n,k <= 100,000  | x-> x-1,x+1,x*2
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#define SIZE 100001
using namespace std;
int from[SIZE];
int check[SIZE];
int n, k;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
void froms(int k, int n)
{
    vector<int> ans;
    while (k != n)
    {
        ans.push_back(k);
        k = from[k];
    }
    ans.push_back(k);
    reverse(ans.begin(), ans.end());
    for (auto k : ans)
    {
        cout << k << " ";
    }
}
int main()
{
    cin >> n >> k;
    fill(&check[0], &check[0] + SIZE, -1);
    queue<int> q;
    q.push(n);
    check[n] = 0;
    from[n] = -1;
    while (!q.empty())
    {
        int now = q.front();
        q.pop();
        //k노드라면 종료
        if (now == k)
        {
            cout << check[now] << "\n";
            froms(k, n);
            break;
        }
        //다음 노드를 탐색 | 범위,방문 체크 | 방문 안했다면, 가중치를 +1
        if (now + 1 < SIZE && check[now + 1] == -1)
        {
            check[now + 1] = check[now] + 1;
            from[now + 1] = now;
            q.push(now + 1);
        }
        if (now - 1 >= 0 && check[now - 1] == -1)
        {
            check[now - 1] = check[now] + 1;
            from[now - 1] = now;
            q.push(now - 1);
        }
        if (now * 2 < SIZE && check[now * 2] == -1)
        {
            check[now * 2] = check[now] + 1;
            from[now * 2] = now;
            q.push(now * 2);
        }
    }
}
