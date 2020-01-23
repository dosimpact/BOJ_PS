//https : //www.acmicpc.net/problem/14226
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#define SIZE 1001
using namespace std;
int d[1001][1001];

int main()
{
    //만들 이모티콘 수 n
    int n;
    cin >> n;
    fill(&d[0][0], &d[0][0] + SIZE * SIZE, -1);
    queue<pair<int, int>> q;
    q.push({1, 0});
    d[1][0] = 0; // -1 이면 방문 안함.
    //d노드를 d[n][0~n] 까지만 BFS
    while (!q.empty())
    {
        //큐에서 현재 노드를 뺴고
        int s, c;
        tie(s, c) = q.front();
        q.pop();
        if (s == n)
        {
            cout << d[s][c];
            return 0;
        }
        // s,c => s,s | 범위 체크 및 방문여부 체크
        if (d[s][s] == -1)
        {
            d[s][s] = d[s][c] + 1;
            q.push({s, s});
        }
        // s,c => s+c, c
        if (s + c <= n && d[s + c][c] == -1)
        {
            d[s + c][c] = d[s][c] + 1;
            q.push({s + c, c});
        }
        // s,c => s-1, c
        if (s - 1 > 0 && d[s - 1][c] == -1)
        {
            d[s - 1][c] = d[s][c] + 1;
            q.push({s - 1, c});
        }
    }
}