//https://www.acmicpc.net/problem/6603
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int w[11][11];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while (true)
    {
        int k;
        cin >> k;
        if (k == 0)
        {
            break;
        }
        vector<int> s;
        vector<int> permutation_pointer;
        for (int i = 1; i <= 6; i++)
        {
            int ele;
            cin >> ele;
            s.push_back(ele);
            permutation_pointer.push_back(1);
        }
        for (int i = 7; i <= k; i++)
        {
            int ele;
            cin >> ele;
            s.push_back(ele);
            permutation_pointer.push_back(2);
        }
        sort(permutation_pointer.begin(), permutation_pointer.end());
        do
        {
            for (int i = 0; i < permutation_pointer.size(); i++)
            {
                if (permutation_pointer[i] == 1)
                {
                    cout << s[i] << " ";
                }
            }
            cout << "\n";
            //순열이 1이면 출력,
        } while (next_permutation(permutation_pointer.begin(), permutation_pointer.end()));
        cout << "\n";
    }
}