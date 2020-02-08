// https://www.acmicpc.net/problem/17136
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 10
using namespace std;

int graph[SIZE][SIZE];     //원본 판 0~9
int tmp_graph[SIZE][SIZE]; // 고생할 판.

void disCover(int size, int x, int y) //5 5 사이즈로 x,y시작점 부터  안 덮는다.
{
    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            tmp_graph[i][j] = 0;
        }
    }
}
void cover(int size, int x, int y) //5 5 사이즈로 x,y시작점 부터 덮는다.
{
    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            tmp_graph[i][j] = 1;
        }
    }
}
bool canCover(int size, int x, int y) //범위 체크 ~
{
    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            if (x > 9 || y > 9 || x < 0 || y < 0 || graph[i][j] == 0 || tmp_graph[i][j] == 1)
            {
                return false;
            }
        }
    }
    return true;
}
//덮은 색종이수 | 현재까지 덮은 수 , 현재 z인덱스 , 남은 색종이수
int go(int count, int z, vector<int> &cp)
{
    //z가 끝까지 도달한 경우
    if (z == 100)
    {
        return count;
    }
    int x = z / 10;
    int y = z % 10;
    if (graph[x][y] == 0)
    { //z가 graph 0이면 계속
        return go(count, z + 1, cp);
    }
    else if (graph[x][y] == 1 && tmp_graph[x][y] == 1)
    {
        return go(count, z + 1, cp);
    }
    else if (graph[x][y] == 1 && tmp_graph[x][y] == 0)
    { //z graph 1이면 | 5부터 1까지 덮어본다. | 못덮으면, -1 리턴
        int min = -1;
        for (int i = 4; i >= 0; i--)
        {
            if (cp[i] > 0)
            {
                if (canCover(i + 1, x, y)) // 5 사이즈로 덮냐?
                {
                    cp[i] -= 1;
                    cover(i + 1, x, y);
                    int tmp = go(count + 1, z + 1, cp);
                    //FB if ((min == -1 || min > tmp))
                    if (tmp != -1 && (min == -1 || min > tmp)) //tmp 가 -1이 아니여야됨.
                    {
                        min = tmp;
                    }
                    disCover(i + 1, x, y);
                    cp[i] += 1;
                }
            }
        }
        return min; //리턴 결과 -1이면 안되는 경우 | 빼고 최곳값 => 리턴
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            cin >> graph[i][j];
        }
    }
    vector<int> cp = {5, 5, 5, 5, 5};
    int ans = go(0, 0, cp);
    cout << ans;
}