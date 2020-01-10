//https://www.acmicpc.net/problem/2455
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
    vector<int> ans_list;
    int current = 0;
    for (int i = 0; i < 4; i++)
    {
        int in, out;
        cin >> in >> out;
        current -= in;
        current += out;
        ans_list.push_back(current);
    }
    cout << *max_element(ans_list.begin(), ans_list.end());
}