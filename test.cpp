//https://www.acmicpc.net/problem/10448
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 1001
using namespace std;

char graph[5][9];
bool check[12];

bool checkAll()
{
    if ((graph[0][4] - 'A' + 1) + (graph[1][3] - 'A' + 1) + (graph[2][2] - 'A' + 1) + (graph[3][1] - 'A' + 1) != 26)
        return false;
    if ((graph[0][4] - 'A' + 1) + (graph[1][5] - 'A' + 1) + (graph[2][6] - 'A' + 1) + (graph[3][7] - 'A' + 1) != 26)
        return false;
    if ((graph[1][1] - 'A' + 1) + (graph[1][3] - 'A' + 1) + (graph[1][5] - 'A' + 1) + (graph[1][7] - 'A' + 1) != 26)
        return false;
    if ((graph[3][1] - 'A' + 1) + (graph[3][3] - 'A' + 1) + (graph[3][5] - 'A' + 1) + (graph[3][7] - 'A' + 1) != 26)
        return false;
    if ((graph[4][4] - 'A' + 1) + (graph[3][3] - 'A' + 1) + (graph[2][2] - 'A' + 1) + (graph[1][1] - 'A' + 1) != 26)
        return false;
    if ((graph[4][4] - 'A' + 1) + (graph[3][5] - 'A' + 1) + (graph[2][6] - 'A' + 1) + (graph[1][7] - 'A' + 1) != 26)
        return false;
    return true;
}

void go(int z)
{ //다 채운 경우. ->
    if (z >= 45)
    {
        if (checkAll())
        {

            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    cout << graph[i][j] << "";
                }
                cout << "\n";
            }
            exit(0);
        }
        return;
    }
    int x = z / 9, y = z % 9;
    if (graph[x][y] == '.')
    {
        go(z + 1);
    }
    else if (graph[x][y] == 'x')
    {
        for (char i = 'A'; i <= 'L'; i++)
        {
            if (check[i - 'A'] == true)
                continue;
            check[i - 'A'] = true;
            graph[x][y] = i;
            go(z + 1);
            graph[x][y] = 'x';
            check[i - 'A'] = false;
        }
    }
    else
    {
        go(z + 1);
    }
}

int main()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cin >> graph[i][j];
            if (graph[i][j] >= 'A' && graph[i][j] <= 'L')
            {
                check[graph[i][j] - 'A'] = true;
            }
        }
    }
    go(0);
}