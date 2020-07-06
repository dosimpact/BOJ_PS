#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, tmp;
    vector<int> sus;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        sus.push_back(tmp);
    }
    int maxVal = *max_element(sus.begin(), sus.end());
    for (int i = 1; i <= maxVal; i++)
    {
        bool isposs = true;
        for (auto it = sus.begin(); it != sus.end(); it++)
        {
            if (!isposs)
            {
                break;
            }
            if (*it % i != 0)
            {
                isposs = false;
            }
        }
        if (isposs)
        {
            cout << i << "\n";
        }
    }
}