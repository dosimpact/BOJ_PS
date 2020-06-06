//https://www.acmicpc.net/problem/9095
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int ans = 0;
        int n;
        cin >> n;
        //첫번쨰 항이 1,2,3일때,
        for (int l1 = 1; l1 <= 3; l1++)
        {
            //첫번째 항으로만 n이 완성되면 하나 추가.
            if (n == l1)
            {
                ans++;
            }
            for (int l2 = 1; l2 <= 3; l2++)
            {
                if (n == l1 + l2)
                {
                    ans++;
                }
                for (int l3 = 1; l3 <= 3; l3++)
                {
                    if (n == l1 + l2 + l3)
                    {
                        ans++;
                    }
                    for (int l4 = 1; l4 <= 3; l4++)
                    {
                        if (n == l1 + l2 + l3 + l4)
                        {
                            ans++;
                        }
                        for (int l5 = 1; l5 <= 3; l5++)
                        {
                            if (n == l1 + l2 + l3 + l4 + l5)
                            {
                                ans++;
                            }
                            for (int l6 = 1; l6 <= 3; l6++)
                            {
                                if (n == l1 + l2 + l3 + l4 + l5 + l6)
                                {
                                    ans++;
                                }
                                for (int l7 = 1; l7 <= 3; l7++)
                                {
                                    if (n == l1 + l2 + l3 + l4 + l5 + l6 + l7)
                                    {
                                        ans++;
                                    }
                                    for (int l8 = 1; l8 <= 3; l8++)
                                    {
                                        if (n == l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8)
                                        {
                                            ans++;
                                        }
                                        for (int l9 = 1; l9 <= 3; l9++)
                                        {
                                            if (n == l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9)
                                            {
                                                ans++;
                                            }
                                            for (int l10 = 1; l10 <= 3; l10++)
                                            {
                                                if (n == l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10)
                                                {
                                                    ans++;
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        cout << ans << "\n";
    }
}