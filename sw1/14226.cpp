//https : //www.acmicpc.net/problem/14226
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <cstring>
#define SIZE 1001
using namespace std;
int d[1001][1001];

int main()
{
    //만들기 원하는 이모티콘수,
    int k;
    cin >> k;
    fill(&d[0][0], &d[0][0] + SIZE * SIZE, -1); //fB). 2차원 배열 초기화..
    //현재의 상태를 넣기.
    queue<pair<int, int>> q;
    q.push({1, 0});
    d[1][0] = 0;
    //0번
    while (!q.empty())
    {
        //현재의 노드
        int s, c;
        tie(s, c) = q.front();
        q.pop();
        if (d[s][s] == -1) //방문하지 않았다면
        {
            d[s][s] = d[s][c] + 1;
            q.push({s, s});
        }
        if (s + c <= k && d[s + c][c] == -1) //범위 체크 및 //방문하지 않았다면
        {
            d[s + c][c] = d[s][c] + 1;
            q.push({s + c, c});
        }
        if (s - 1 > 0 && d[s - 1][c] == -1) //범위 체크 및 //방문하지 않았다면
        {
            d[s - 1][c] = d[s][c] + 1;
            q.push({s - 1, c});
        }
    }
    //s+c의 범위체크를 k 이하로 했다. 따라서 d[s][c] , s<= k, c <= k
    //d[k][c] 에서
    int ans = -1;
    for (int i = 0; i < k; i++)
    {
        if (d[k][i] != -1 && (ans == -1 || d[k][i] < ans))
        {
            ans = d[k][i];
        }
    }
    cout << ans;
}