//https://www.acmicpc.net/problem/10971
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
    //w를 입력받고
    int n;
    vector<int> k;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        k.push_back(i);
        for (int j = 0; j < n; j++)
        {
            int ele;
            cin >> ele;
            w[i][j] = ele;
        }
    }
    //정렬후
    sort(k.begin(), k.end());
    //순열을 이용해 최소 비용 구하기.
    int ans = -1;
    do
    {
        int tmp_ans = 0;
        bool isOk = true;
        for (int i = 0; i < n - 1; i++)
        {
            //w의 시작점 끝점 찾을때, k는 0,1,2,3이 도는 구조
            tmp_ans += w[k[i]][k[i + 1]];
            if (w[k[i]][k[i + 1]] == 0)
            {
                isOk = false;
            }
        }
        tmp_ans += w[k[n - 1]][k[0]];
        if (w[k[n - 1]][k[0]] == 0)
        {
            isOk = false;
        }
        // - 한번이라도 갈수 없다면 ok는 false.
        // 비용을 누적해서 최솟값 구하기.
        if (isOk)
        {
            if (ans == -1 || tmp_ans < ans)
            {
                ans = tmp_ans;
            }
        }
    } while (next_permutation(k.begin(), k.end()));
    cout << ans;
}