//https://www.acmicpc.net/problem/1547
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
    vector<int> cup_list;
    int m;
    cin >> m;
    cup_list.push_back(0);
    cup_list.push_back(1);
    cup_list.push_back(2);
    cup_list.push_back(3);
    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        auto a = find(cup_list.begin(), cup_list.end(), x);
        auto b = find(cup_list.begin(), cup_list.end(), y);
        swap(*a, *b);
        // cout << "CUP\n";
        // for (auto k : cup_list)
        // {
        //     cout << k << " ";
        // }
    }
    cout << cup_list[1];
    // for (auto k : cup_list)
    // {
    //     cout << k << " ";
    // }
}