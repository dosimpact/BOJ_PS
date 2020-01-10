//https://www.acmicpc.net/problem/1021
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
using namespace std;
int a[51];
deque<int> q;
int main()
{
    int ans = 0;
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> a[i];
    }
    for (int i = 1; i <= n; i++)
    {
        q.push_back(i);
    }
    for (int idx = 0; idx < m; idx++)
    {
        //현재 뽑을 수
        int f = 0;
        deque<int> fq = q;
        int b = 0;
        deque<int> bq = q;
        //큐를 순방향으로 돌려보고 값을 구해본다.
        while (fq.front() != a[idx])
        {
            f += 1;
            fq.push_back(fq.front());
            fq.pop_front();
        }
        //큐를 뒤로 돌려서  값을 구해본다.
        while (bq.front() != a[idx])
        {
            b += 1;
            bq.push_front(bq.back());
            bq.pop_back();
        }
        //최소값으로 나온 큐를 선택해, 값을 뺴고, idx증가시킨다.
        if (f <= b)
        {
            q = fq;
            q.pop_front();
            ans += f;
        }
        else
        {
            q = bq;
            q.pop_front();
            ans += b;
        }
    }
    cout << ans;
}