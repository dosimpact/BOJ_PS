

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int n;
int ans[10];
int sign[10][10];

bool check(int idx)
{
    int now = ans[idx];
    for (int i = idx - 1; i >= 0; i--)
    {
        now += ans[i];
        if (sign[i][idx] == 0)
        {
            if (now != 0)
                return false;
        }
        else if (sign[i][idx] == -1)
        {
            if (now >= 0)
            {
                return false;
            }
        }
        else
        {
            if (now <= 0)
                return false;
        }
    }
    return true;
}

bool go(int idx) // 리턴
{
    //현재 인덱스가 n까지 도달 = 성공
    if (idx == n)
    {
        return true;
    }
    if (sign[idx][idx] == 0)
    {
        ans[idx] = 0;
        return check(idx) && go(idx + 1);
    }
    for (int i = 1; i <= 10; i++)
    {
        ans[idx] = sign[idx][idx] * i;
        if (check(idx) && go(idx + 1))
            return true;
    }
    return false;
    //현재 부호를 보고 0이면 0 넣보고, 검사 해보고 go
}

int main(void)
{
    //입력 받기
    cin >> n;
    string s;
    cin >> s;
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            if (s[cnt] == '+')
            {
                sign[i][j] = 1;
            }
            if (s[cnt] == '-')
            {
                sign[i][j] = -1;
            }
            if (s[cnt] == '0')
            {
                sign[i][j] = 0;
            }
            cnt++;
        }
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = i; j < n; j++)
    //     {
    //         cout << sign[i][j] << "  ";
    //     }
    //     cout << "\n";
    // }
    //go(0)돌기
    go(0);
    for (int i = 0; i < n; i++)
    {
        cout << ans[i] << " ";
    }
}