#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#define SIZE 51
using namespace std;

int graph[SIZE][SIZE];
int check[SIZE][SIZE];
int dx[8] = {0, 0, 1, -1, -1, 1, 1, -1};
int dy[8] = {1, -1, 0, 0, 1, 1, -1, -1};
int w, h;

void dfs(int x, int y, int num)
{
    check[x][y] = num;
    for (int k = 0; k < 8; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];
        //FB1. 범위검사
        if (nx < 0 || ny < 0 || nx >= w || ny >= h)
        {
            continue;
        }
        if (graph[nx][ny] == 1 && check[nx][ny] == 0)
        {
            dfs(nx, ny, num);
        }
    }
}

int main()
{
    vector<int> a;

    return 0;
}