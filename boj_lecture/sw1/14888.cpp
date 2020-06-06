//https://www.acmicpc.net/problem/14888
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

    int n;
    cin >> n;
    vector<int> a;
    vector<int> op;
    for (int i = 1; i <= n; i++)
    {
        int ele;
        cin >> ele;
        a.push_back(ele);
    }
    for (int i = 1; i <= 4; i++)
    {
        int ele;
        cin >> ele;
        for (int j = 0; j < ele; j++)
        {
            op.push_back(i); // + - * / 는 각각 1,2,3,4
        }
    }
    sort(op.begin(), op.end());
    vector<int> ans_vector;
    int ans_max = -1;
    int ans_min = -1;
    do
    {
        int ans_sum = a[0];
        //op순열돌리면서
        for (int i = 0; i < op.size(); i++)
        {
            int current_op = op[i];
            if (current_op == 1)
            {
                ans_sum += a[i + 1];
            }
            else if (current_op == 2)
            {
                ans_sum -= a[i + 1];
            }
            else if (current_op == 3)
            {
                ans_sum *= a[i + 1];
            }
            else if (current_op == 4)
            {
                ans_sum = (ans_sum / a[i + 1]);
            }
            else
            {
                cout << "ERROR";
            }
        }
        //ans_sum 에 += func(op[0],a[1])
        ans_vector.push_back(ans_sum);
    } while (next_permutation(op.begin(), op.end()));
    auto k = minmax_element(ans_vector.begin(), ans_vector.end());
    cout << *k.second << "\n"
         << *k.first;
}