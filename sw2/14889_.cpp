//https://www.acmicpc.net/problem/14889
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n; //20보다 작다.
int graph[20][20];
int ans = 2100000000;
//천천히 숫자를 하나씩 고를꺼야, 물론 한쪽으로 쏠릴수도 있는데, 예외처리를 해주자.
// 고를 인덱스(idx  ==n이면 다고름), 컨테이너 두개
void go(int idx, vector<int> &con1, vector<int> &con2)
{
    //다모은 경우
    if (idx == n)
    {

        //각자 골고루 나온 경우.
        if (con1.size() != (n / 2) || con2.size() != (n / 2))
            return;
        // cout << "\n다모음!!\n";
        // for (auto &k : con1)
        // {
        //     cout << k;
        // }
        // cout << "\n";
        // for (auto &k : con2)
        // {
        //     cout << k;
        // }
        //각각 합산값을 구해본다.
        int t1 = 0, t2 = 0;
        for (int i = 0; i < (n / 2); i++)
        {
            for (int j = 0; j < (n / 2); j++)
            {
                if (i == j)
                    continue;
                t1 += graph[con1[i]][con1[j]];
                t2 += graph[con2[i]][con2[j]];
            }
        }

        //최소라면 ans 넣기
        int diff = t1 - t2;
        if (diff < 0)
            diff = -diff;
        //cout << diff << "\n";
        if (ans > diff)
        {
            ans = diff;
        }
        return;
    }
    //    //계속)con1에 idx를 넣보고 go 다시 빼고
    con1.push_back(idx);
    go(idx + 1, con1, con2);
    con1.pop_back();
    //con2에 시도
    con2.push_back(idx);
    go(idx + 1, con1, con2);
    con2.pop_back();

    return;
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }
    vector<int> con1;
    vector<int> con2;
    go(0, con1, con2);
    cout << ans;
}