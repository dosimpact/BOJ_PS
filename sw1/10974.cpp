//https://www.acmicpc.net/problem/10974
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<int> k;
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        k.push_back(i);
    }
    do
    {
        for (auto &_k : k)
        {
            cout << _k << " ";
        }
        cout << "\n";
    } while (next_permutation(k.begin(), k.end()));
}