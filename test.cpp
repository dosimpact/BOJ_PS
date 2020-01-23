#include <iostream>
#include <queue>
#include <cstdio>
#include <tuple>
using namespace std;

int main()
{
    int ans1 = 3;
    int ans2 = 4;
    if (ans1 && ans2)
    {
        printf("%d", min(ans1, ans2));
    }
}