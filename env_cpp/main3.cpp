#include <iostream>

using namespace std;
int memo[1000000];

int dp(int n)
{
    if (n <= 1)
        return 0;
    if (memo[n] != 0)
        return memo[n];
    int tmp = 0;
    memo[n] = dp(n - 1) + 1;
    if (n % 2 == 0 && memo[n] > dp(n / 2) + 1)
        memo[n] = dp(n / 2) + 1;
    if (n % 3 == 0 && memo[n] > dp(n / 3) + 1)
        memo[n] = dp(n / 3) + 1;
    return memo[n];
}

int main()
{
    int N;
    cin >> N;
    int ans = dp(N);
    cout << ans << "\n";
    return 0;
}