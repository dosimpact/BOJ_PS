//https://www.acmicpc.net/problem/1476
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int E, S, M;
    cin >> E >> S >> M;
    int counter = 0;
    int e = 0, s = 0, m = 0;
    while (true)
    {
        counter++;
        e++;
        s++;
        m++;
        if (e > 15)
        {
            e = 1;
        }
        if (s > 28)
        {
            s = 1;
        }
        if (m > 19)
        {
            m = 1;
        }
        if (e == E && s == S && m == M)
        {
            break;
        }
    }
    cout << counter;
}