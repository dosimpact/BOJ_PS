//https://www.acmicpc.net/problem/1966
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
using namespace std;
//기본적인 방법.n제곱
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;
        vector<int> v(n);
        //값을 입력받습니다.
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }
        //추적중인 중요도 값보다 큰 값들의 갯수를 구합니다.
        int bcouter = 0;
        for (int i = 0; i < n; i++)
        {
            if (v[m] < v[i])
            {
                bcouter++;
            }
        }
        if (bcouter == 0)
        {
            //앞에서부터 출력순서를 구합니다.
            for (int i = 0; i < m; i++)
            {
                if (v[m] == v[i])
                    bcouter++;
            }
            cout << bcouter + 1 << "\n";
            continue;
        }
        else
        {
            // 출력할 중요도보다 하나 큰값을 뒤에서부터 찾아 인덱슬르 구합니다.
            int diff = 100;
            for (int i = 0; i < n; i++)
            {
                int tmp_diff = v[i] - v[m];
                if (tmp_diff > 0 && tmp_diff < diff)
                {
                    diff = tmp_diff;
                }
            }
            int onemorebig = n - 1;
            while (onemorebig >= 0)
            {
                int tmp_diff = v[onemorebig] - v[m];
                if ((tmp_diff) == diff)
                {
                    break;
                }
                onemorebig--;
            }
            int ans = bcouter;
            //cout << "bcouter " << bcouter << " onemorebigidx " << onemorebig << " diff " << diff << "\n";
            // 그 인덱스 부터 끝까지, 처음부터 인덱스까지 슬라이싱 합니다.
            for (int i = onemorebig; i < n; i++)
            {
                if (v[i] == v[m])
                    ans++;
                if (i == m)
                {
                    cout << ans << "\n";
                    break;
                }
            }
            for (int i = 0; i < onemorebig; i++)
            {
                if (v[i] == v[m])
                    ans++;
                if (i == m)
                {
                    cout << ans << "\n";
                    break;
                }
            }
        }
    }
}