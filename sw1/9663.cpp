//https://www.acmicpc.net/problem/9663

#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

int n; //15이하,
bool queuen[16][16];
int ans = 0;
//현재 row
bool check(int x, int y)
{
    //위로 검사.
    bool isOk = true;
    int nx = x - 1;
    for (int i = 0; i <= nx; i++)
    {
        if (queuen[i][y])
        {
            isOk = false;
        }
    }
    //왼쪽 검사.fb ) 반드시 없을수 밖에 ...
    int ny = y - 1;
    for (int i = 0; i <= ny; i++)
    {
        if (queuen[x][i])
        {
            isOk = false;
        }
    }
    //왼쪽 대각선 검사.
    nx = x - 1;
    ny = y - 1;
    while (nx >= 0 && ny >= 0)
    {
        if (queuen[nx][ny])
        {
            isOk = false;
        }
        nx--;
        ny--;
    }
    //왼쪽 대각선 검사.
    nx = x - 1;
    ny = y + 1;
    while (nx >= 0 && ny < n)
    {
        if (queuen[nx][ny])
        {
            isOk = false;
        }
        nx--;
        ny++;
    }
    return isOk;
}
void go(int row)
{
    //row를 다 채웠으면, 완성ㅎ!
    if (row == n)
    {
        ans++;
        return;
    }
    //현재 row에서 컬럼을 돌면서, 한번 위치에 퀀을 놔봐
    for (int i = 0; i < n; i++)
    {
        //cout << check(row, i) << " ";
        if (check(row, i))
        {
            //괜찮으면 다음 row로 넘어가자.
            queuen[row][i] = true;
            go(row + 1);
            queuen[row][i] = false;
        }
    }
}
int main()
{
    cin >> n;
    go(0);
    cout << ans << "\n";
}