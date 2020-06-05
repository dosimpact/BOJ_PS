//https://www.acmicpc.net/problem/1759
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;
bool check(string s)
{
    int ja = 0;
    int mo = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            mo++;
        }
        else
        {
            ja++;
        }
    }
    return (ja >= 2 && mo >= 1);
}
//문자의 길이, 현재까지 만든거,  사용할수있는알파벳, 고를넘버,
void go(int n, string current, vector<char> &alpha, int choice)
{
    //문자열의 길이가 완성이 되면 검사후  check출력 그리고 리턴
    if (current.size() == n)
    {
        if (check(current))
        {
            cout << current << "\n";
        }
        return;
    }
    // choice가 끝났는데 문자열의 길이가 부족하면 그냥 리턴
    if (alpha.size() == choice)
    {
        return;
    }
    go(n, current + alpha[choice], alpha, choice + 1);
    go(n, current, alpha, choice + 1);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int l, c;
    cin >> l >> c;
    vector<char> alpha;
    for (int i = 0; i < c; i++)
    {
        char ele;
        cin >> ele;
        alpha.push_back(ele);
    }
    sort(alpha.begin(), alpha.end());
    go(l, "", alpha, 0);
}