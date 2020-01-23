//https://www.acmicpc.net/problem/13549
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#define SIZE 100001
using namespace std;
int d[SIZE];

int main()
{
    fill(&d[0], &d[0] + SIZE, -1);
    int n, k;
    cin >> n >> k;
    vector<queue<int>> rotation_q;
    rotation_q.push_back(queue<int>());
    rotation_q.push_back(queue<int>());
    rotation_q[0].push(n);
    d[n] = 0;
    while (!rotation_q[0].empty())
    {
        //현재 위치 빼기
        int now = rotation_q[0].front();
        rotation_q[0].pop();
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
                rotation_q[0].push(now * 2);
            }
        }
        // 걷기 x => x+1 // 범위 체크 / 방문 여부 / q2.에 가중치 + 1
        if (now + 1 <= SIZE)
        {
            if (d[now + 1] == -1)
            {
                d[now + 1] = d[now] + 1;
                rotation_q[1].push(now + 1);
            }
        }
        // x => x - 1  // 범위 체크 / 방문 여부 / q2.에 가중치 + 1
        if (now - 1 >= 0)
        {
            if (d[now - 1] == -1)
            {
                d[now - 1] = d[now] + 1;
                rotation_q[1].push(now - 1);
            }
        }
        //q1이 비워졌다면 , q1을 2로 교체 후 q2는 비워 두기
        if (rotation_q[0].empty())
        {
            rotation_q.erase(rotation_q.begin(), rotation_q.begin() + 1);
            rotation_q.push_back(queue<int>());
        }
    }
}