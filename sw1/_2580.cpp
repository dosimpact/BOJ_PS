//https://www.acmicpc.net/problem/2580

#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

int check[10];
int graph[10][10];
deque<pair<int, int>> zero;
void printGraph()
{
    cout << "----\n";
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << "\n";
    }
}
// 0 이면  중복된 수가 있음, 1이면 0이 아직 있는상태, 2면 유효함.
bool isVaildSqure(int x, int y)
{
    cout << "유효형 검사를 합니다." << x << "," << y << "\n";
    fill(&check[0], &check[10] + 1, 0);
    int start_x = (x / 3) * 3;
    int start_y = (y / 3) * 3;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            int nnode = graph[start_x + i][start_y + j];
            if (nnode == 0)
                return 1;
            if (check[nnode] == 1)
            {
                return 0;
            }
            check[nnode] = 1;
        }
    }
    return 2;
}
bool isVaildRow(int x)
{
    fill(&check[0], &check[10] + 1, 0);
    for (int i = 0; i < 9; i++)
    {
        int nnode = graph[x][i];
        if (check[nnode] == 1)
        {
            return false;
        }
        check[nnode] = 1;
    }
    return true;
}
bool isVaildCol(int y)
{
    fill(&check[0], &check[10] + 1, 0);
    for (int i = 0; i < 9; i++)
    {
        int nnode = graph[i][y];
        if (check[nnode] == 1)
        {
            return false;
        }
        check[nnode] = 1;
    }
    return true;
}
bool isVaildAll()
{
    bool isOk = true;
    for (int i = 0; i < 9; i++)
    {
        if (!isVaildCol(i) || !isVaildRow(i))
        {
            isOk = false;
        }
    }
    for (int i = 0; i <= 6; i = i + 3)
    {
        for (int j = 0; j <= 6; j += 3)
        {
            if (isVaildSqure(i, j) != 2)
            {
                isOk = false;
            }
        }
    }
    return isOk;
}
//0인 부분
void go(int x, int y)
{
    //다 채운경우 | 유효성검사 통과하면 스토구 출력,
    if (zero.size() == 0)
    {
        if (isVaildAll())
        {
            printGraph();
        }
        else
        {
            return;
        }
    }
    //다 채우지 않았더라도, 유효하지 않는 사각형이면,
    if (isVaildSqure(x, y) == 0)
    {
        return;
    }
    //1부터 9까지 채워본다.
    for (int i = 1; i <= 9; i++)
    {

        auto current = zero.front();
        printGraph();
        cout << current.first << " " << current.second << " 크기 : " << zero.size() << "\n";
        int tmp;
        cin >> tmp;
        zero.pop_front();
        graph[current.first][current.second] = i;
        go(current.first, current.second);
        //zero.push_front(current);
    }
}
int main()
{
    //스토쿠 입력받기
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            int ele;
            cin >> ele;
            graph[i][j] = ele;
            if (ele == 0)
            { // 0인 입력이라면, 백터로 모아두기.
                zero.push_back(make_pair(i, j));
            }
        }
    }
    int x = isVaildAll();
    x = isVaildCol(0);
    x = isVaildRow(0);
    x = isVaildSqure(0, 0);
    // for (auto k : zero)
    // {
    //     cout << k.first << " " << k.second << " \n";
    // }
    //go(0, 0);
}
/*
1 2 3
4 5 6
7 8 9

0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

*/