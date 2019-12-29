#include <iostream>
#include <algorithm>
using namespace std;

int check[10000001];

int pow(int a, int b)
{
    int ans = 1;
    while (b--)
    {
        ans *= a;
    }
    return ans;
}
int next(int a, int p)
{
    int ans = 0;
    while (a != 0)
    {
        //FB. 나머지 논리는 숫자의 뒤에서 부터 짤라내는 방식이다, string으로 변환해서 처리하는 방법도 있음.
        ans += pow(a % 10, p);
        a = a / 10;
    }
    return ans;
}
int length(int a, int p, int checknum)
{
    check[a] = checknum;
    int b = next(a, p);
    if (check[b] != 0)
    {
        return check[b] - 1;
    }
    else
    { //FB.return을 안적으면, 함수만 실행되고 결과가 리턴이 안되지..
        return length(b, p, checknum + 1);
    }
}
int main()
{
    int a, p;
    cin >> a >> p;
    cout << length(a, p, 1);
}