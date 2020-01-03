//https://www.acmicpc.net/problem/15652

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int a[10];
int n, m;
void printArray()
{
    for (int i = 0; i < m; ++i)
    {
        cout << a[i] << " ";
    }
    cout << "\n";
}
//a 커서 , 고를 숫자.
void go(int ac, int start)
{
    //베이스)다 골랐어
    if (ac == m)
    {
        printArray();
        return;
    }

    //계속) fb)각각 모든 숫자에대해, 골랐다치고, 다음숫자도 고를려 해보자.
    for (int i = start; i <= n; i++)
    {
        a[ac] = i;
        go(ac + 1, i);
    }
}
using namespace std;
int main()
{
    cin >> n >> m;
    go(0, 1);
}