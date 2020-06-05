//https://www.acmicpc.net/problem/14888

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n;
int op[4];
int nums[12];
vector<int> ans;
//현재까지의 값,다음 넘버,남은 연산자들,
void go(int value, int idx, int plus, int minus, int mul, int div)
{
    //더이상의 연산자가 없다면, 종료
    if (plus == 0 && minus == 0 && mul == 0 && div == 0)
    {
        ans.push_back(value);
        return;
    }
    //각각의 경우에 대해 시행
    if (plus > 0)
    {
        go(value + nums[idx], idx + 1, plus - 1, minus, mul, div);
    }
    if (minus > 0)
    {
        go(value - nums[idx], idx + 1, plus, minus - 1, mul, div);
    }
    if (mul > 0)
    {
        go(value * nums[idx], idx + 1, plus, minus, mul - 1, div);
    }
    if (div > 0)
    {
        go(value / nums[idx], idx + 1, plus, minus, mul, div - 1);
    }
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int ele;
        cin >> ele;
        nums[i] = ele;
    }
    for (int i = 0; i < 4; i++)
    {
        int ele;
        cin >> ele;
        op[i] = ele;
    }
    go(nums[0], 1, op[0], op[1], op[2], op[3]);
    //ans에서 최대값 최솟값 찾아주기.
    auto k = minmax_element(ans.begin(), ans.end());
    cout << *k.second << "\n"
         << *k.first << "\n";
}