//https://www.acmicpc.net/problem/13549
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <vector>
#define SIZE 100001
using namespace std;
int d[SIZE];

int main()
{
    fill(&d[0], &d[0] + SIZE, -1);
    int n, k;
    cin >> n >> k;
    vector<int> v;
    queue<int> q1;
    queue<int> q2;
    v[0];
    q1.push(n);
    d[n] = 0;
    while (!q1.empty())
    {
        //현재 위치 빼기
        int now = q1.front();
        q1.pop();
        if (now == k)
        {
            cout << d[now];
            return 0;
        }
        // 순간이동 x => x*2    // 범위 체크 | 방문 여부 | ,q1에 가중치 없이 계속 넣어준다.
        if (now * 2 <= SIZE)
        {
            if (d[now * 2] == -1)
            {
                d[now * 2] = d[now];
                q1.push(now * 2);
            }
        }
        // 걷기 x => x+1 // 범위 체크 / 방문 여부 / q2.에 가중치 + 1
        if (now + 1 <= SIZE)
        {
            if (d[now + 1] == -1)
            {
                d[now + 1] = d[now] + 1;
                q2.push(now + 1);
            }
        }
        // x => x - 1  // 범위 체크 / 방문 여부 / q2.에 가중치 + 1
        if (now - 1 >= 0)
        {
            if (d[now - 1] == -1)
            {
                d[now - 1] = d[now] + 1;
                q2.push(now - 1);
            }
        }
        //q1이 비워졌다면 , q1을 2로 교체 후 q2는 비워 두기
        if (q1.empty())
        {
            q1 = q2;
            q2 = queue<int>();
        }
    }
}