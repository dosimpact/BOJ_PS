//https://www.acmicpc.net/problem/10972
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
bool next_permu(int *a, int n)
{
    //배열을 i로 뒤부터 돌면서, i가 0보다 클때까지 | a[i] 가 뒷녀석보다 큰 지점을 찾는다.
    int i = n - 1;
    while (i > 0 && a[i - 1] >= a[i])
        i--;
    //만약 i가 0 이하면 리턴 F
    if (i <= 0)
        return false;
    //배열을 j로 뒤부터 돌면서, a[i-1]보다 큰 j를 찾는다.
    int j = n - 1;
    while (a[i - 1] >= a[j])
        j--;
    //swap i-1 ,j
    swap(a[i - 1], a[j]);
    //배열을 j로뒤부터 돌면서,i를 앞으로 돌면서 i와j를 swap 해나간다.
    j = n - 1;
    while (i < j)
    {
        swap(a[i], a[j]);
        i++;
        j--;
    }
    return true;
}
int main()
{
    int k[10001];
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        k[i] = tmp;
    }
    if (next_permu(k, n))
    {
        for (int i = 0; i < n; i++)
        {
            cout << k[i] << " ";
        }
    }
    else
    {
        cout << "-1";
    }
}