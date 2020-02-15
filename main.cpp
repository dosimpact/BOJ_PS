#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 101

using namespace std;
int n, m;
vector<int> graph[SIZE];
int main()
{
    cin >> n >> m;
    vector<int> truman;
    int T;
    cin >> T;
    int tmp;
    for (int i = 0; i < T; i++)
    {
        cin >> tmp;
        truman.push_back(tmp);
    }
    for (int i = 0; i < m; i++)
    {
        cin >> T;
        vector<int> persons;
        for (int j = 0; j < T; j++)
        {
            cin >> tmp;
            persons.push_back(tmp);
        }
    }
}