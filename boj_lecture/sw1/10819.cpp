//https://www.acmicpc.net/problem/10819
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<int> &arr)
{
    int ans = 0;
    for (int i = 0; i < arr.size() - 1; i++)
    {
        int tmp = arr[i] - arr[i + 1];
        tmp = tmp > 0 ? tmp : -tmp;
        ans += tmp;
    }
    //cout << "DEBUG : " << ans << " ";
    return ans;
}
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
        int tmp;
        cin >> tmp;
        k.push_back(tmp);
    }
    //FB.정렬를해야 모든 순열을 다 돌꺼 아닌가!
    sort(k.begin(), k.end());
    int answer = -1;
    do
    {
        int tmp_ans = solution(k);
        if (answer == -1 || tmp_ans > answer)
        {
            answer = tmp_ans;
        }
    } while (next_permutation(k.begin(), k.end()));
    cout << answer;
}