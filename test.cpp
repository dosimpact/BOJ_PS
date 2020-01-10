#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int main()
{
    deque<int> dq;
    dq.push_back(1);
    dq.push_back(2);
    dq.push_back(3);
    dq.push_back(4);
    dq.push_back(2);
    dq.push_back(2);
    auto res = upper_bound(dq.begin(), dq.end(), 2);
    cout << *res;
}