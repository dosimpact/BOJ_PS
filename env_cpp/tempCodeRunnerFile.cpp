#include <iostream>
#include <algorithm>
#include <vector>
#define SIZE 1000
using namespace std;
int d[SIZE];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    vector<int> P(1, 0);
    for (int i = 0; i < N; i++)
    {
        int tmp;
        cin >> tmp;
        P.push_back(tmp);
    }
    d[1] = 1;

    for (int i = 2; i <= N; i++)
    {
        d[i] = 1;
        for (int j = 1; j < i; j++)
        {
            if (P[j] < P[i])
            {
                d[i] = max(d[i], d[j] + 1);
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= N; i++)
    {
        ans = max(d[i], ans);
    }
    cout << ans << "\n";
    return 0;
}