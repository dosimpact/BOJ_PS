//https://www.acmicpc.net/problem/14889
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int ans = 2100000000;
    int n;
    cin >> n;
    //n제한이 20인데, nCn/2 = 하튼 반토막 나는데,, n제한 가능!!
    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         cout << a[i][j];
    //     }
    //     cout << "\n";
    // }
    //b백터에 000 111넣기
    vector<int> b(n);
    for (int i = 0; i < n / 2; i++)
    {
        b[i] = 1;
    }
    sort(b.begin(), b.end());
    // for (int i = 0; i < n; i++)
    // {
    //     cout << b[i];
    // }
    do
    {
        //b가 000111이면
        // start 012 link팀  345 를 넣는다.
        vector<int> start;
        vector<int> link;
        for (int i = 0; i < n; i++)
        {
            if (b[i] == 0)
            {
                start.push_back(i);
            }
            else
            {
                link.push_back(i);
            }
        }
        // 이중 for문을 돌면서, 00 continue, 01... 02 => start[0],start[2] -> a점수 환산
        int start__sum = 0;
        int link__sum = 0;
        for (int i = 0; i < (n / 2); i++)
        {
            for (int j = 0; j < (n / 2); j++)
            {
                if (i == j)
                    continue;
                start__sum += a[start[i]][start[j]];
                link__sum += a[link[i]][link[j]];
            }
        }
        int diff = start__sum - link__sum;
        if (diff < 0)
            diff = -diff;
        if (diff < ans)
        {
            ans = diff;
        }

    } while (next_permutation(b.begin(), b.end()));
    cout << ans;
    return 0;
}
