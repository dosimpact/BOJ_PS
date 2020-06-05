//https://www.acmicpc.net/problem/2146
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<int> nan(9);
    for (int i = 0; i < 9; i++)
    {
        int tmp;
        cin >> tmp;
        nan[i] = tmp;
    }
    sort(nan.begin(), nan.end());

    int nansum = 0;
    for (auto &k : nan)
    {
        //cout << k << " ";
        nansum += k;
    }
    for (int i = 0; i < 9 - 1; i++)
    {
        for (int j = i + 1; j < 9; j++)
        {
            int isback = nansum - (nan[i] + nan[j]);
            //cout << isback << " ";
            if (isback == 100)
            {
                for (int k = 0; k < 9; k++)
                {
                    if (k == i || k == j)
                        continue;
                    cout << nan[k] << "\n";
                }
                return 0;
            }
        }
    }
}