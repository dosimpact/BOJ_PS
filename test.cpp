#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;
int n, m, cnt = 0; //책의 개수, 한번에 들 수 있는 책의 수, 총 움직인 거리
vector<int> v;     //책의 위치

int main()
{
    //입력
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    // 한번에 m개책을 | 처음에는 한번만 가면됨
    sort(v.begin(), v.end());
    //음이 가장 큰 경우
    if (abs(v.front()) >= abs(v.back()))
    {
        cnt += abs(v.front());
        //음을 처리 ( 음과 양은 한번에 불가!)
        for (int i = m; i < v.size() && v[i] < 0; i += m)
        {
            cnt += abs(v[i]) * 2;
        }
        for (int i = v.size() - 1; i >= 0 && v[i] > 0; i -= m)
        {
            cnt += abs(v[i]) * 2;
        }
    }
    //양이 가장 큰 경우
    if (abs(v.front()) < abs(v.back()))
    {
        cnt += abs(v.back());
        //음을 처리 ( 음과 양은 한번에 불가!)
        for (int i = 0; i < v.size() && v[i] < 0; i += m)
        {
            cnt += abs(v[i]) * 2;
        }
        for (int i = v.size() - (m + 1); i >= 0 && v[i] > 0; i -= m)
        {
            cnt += abs(v[i]) * 2;
        }
    }
    cout << cnt;
}
