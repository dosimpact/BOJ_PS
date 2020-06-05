//https://www.acmicpc.net/problem/1966
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
using namespace std;
//기본적인 방법.n제곱
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;
        deque<pair<int, int>> dq;
        for (int i = 0; i < n; i++)
        {
            int tmp, ismark = 0;
            cin >> tmp;
            if (i == m)
                ismark = 1;
            dq.push_back(make_pair(tmp, ismark));
        }
        int printCouter = 0;
        bool finished = false;
        while (!finished)
        {
            auto max = max_element(dq.begin(), dq.end());
            //덱의 앞부분을 빼고, 최대값이라면,
            auto current = dq.front();
            dq.pop_front();
            //빼버리고, 카운터 증가, 만약 마크되있다면, 종료후 출력
            if (current.first == (*max).first)
            {
                printCouter++;
                if (current.second == 1)
                {
                    finished = true;
                }
            }
            else //아니라면 다시 넣기.
            {
                dq.push_back(current);
            }
        }
        cout << printCouter << "\n";
    }
}