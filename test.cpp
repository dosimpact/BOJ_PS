#include <iostream>
#include <queue>
#include <deque>
#include <vector>
using namespace std;
bool c[1000000];
int d[1000000];
int MAX = 1000000;
int main()
{
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    for (auto &k : v)
    {
        cout << k << " "; //1 2 3 4 5
    }
    cout << "\n";
    v.erase(v.begin(), v.begin() + 1);
    for (auto &k : v)
    {
        cout << k << " "; //2 3 4 5
    }
    cout << "\n";
    cout << v[0]; // 2
}
