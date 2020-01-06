//https://www.acmicpc.net/problem/14889
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int a, p;
int check[10000001];
int pow(int a, int p)
{
    int ans = 1;
    for (int i = 1; i <= p; i++)
    {
        ans *= a;
    }
    return ans;
}
// int nextNode(int x)
// {
//     int sum = 0;
//     do
//     {
//         int a = x / 10;
//         int b = x % 10;
//         sum += pow(b, p);
//     } while (a != 0);
//     return sum;
// }
int nextNode(int x)
{
    int sum = 0;
    while (x != 0)
    {
        sum += pow(x % 10, p);
        x = x / 10;
    }
    return sum;
}
void dfs(int x, int checkNum)
{
    //현재 노드를 체크해주고, 다음 노드를 구해온다.
    check[x] = checkNum;
    int next = nextNode(x);
    //cout << "DEBUG" << x << " -> " << next << "\n";
    if (check[next] == 0)
    { //다음 노드가 방문 안했다면 다음노드로 방문하고, 체크를 +1
        dfs(next, checkNum + 1);
    }
    else
    {
        //방문했다면 다음노드의 체크넘버보다 -1 출력
        cout << check[next] - 1;
        return;
    }
}
int main()
{
    cin >> a >> p;
    dfs(a, 1);
    //cout << pow(2, 3) << "\n";
    //cout << nextNode(a);
}