#include <iostream>
#include <algorithm>
#include <cstring> //memset

using namespace std;

const int MAXCURRENCY = 10000 + 1; //0 < T <= 10000
const int MAX = 100;
int T, k;
pair<int, int> p[MAX]; //지폐의 금액과 개수
int cache[MAXCURRENCY][MAX];

int numOfWays(int cash, int idx) //idx는 p의 idx
{
    //기저 사례
    if (cash == 0)
        return 1;
    if (idx >= k)
        return 0;

    int &result = cache[cash][idx];

    if (result != -1)
        return result;

    result = 0;
    //해당 동전을 사용하지 않는 경우 + i개 사용하는 경우
    for (int i = 0; i <= p[idx].second; i++)
        //cash는 음수일 수 없다
        if (cash - (p[idx].first * i) >= 0)
            result += numOfWays(cash - (p[idx].first * i), idx + 1);
    return result;
}

int main(void)
{
    cin >> T >> k;
    for (int i = 0; i < k; i++)
        cin >> p[i].first >> p[i].second;
    memset(cache, -1, sizeof(cache));
    cout << numOfWays(T, 0) << endl;
    return 0;
}