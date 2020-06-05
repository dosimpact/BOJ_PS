//https://www.acmicpc.net/problem/10973
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    vector<int> k;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        k.push_back(tmp);
    }
    if (prev_permutation(k.begin(), k.end()))
    {
        for (auto &_k : k)
        {
            cout << _k << " ";
        }
    }
    else
    {
        cout << "-1";
    }
}