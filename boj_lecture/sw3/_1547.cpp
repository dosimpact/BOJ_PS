//https://www.acmicpc.net/problem/1547
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
    int M, NUM = 1;
    cin >> M;
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        if (a == NUM)
        {
            NUM = b;
        }
        else if (b == NUM)
        {
            NUM = a;
        }
        else
        {
            continue;
        }
    }
    cout << NUM;
}