//4693

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#define SIZE 51
using namespace std;

int x_size, y_size;
int graph[SIZE][SIZE];
int check[SIZE][SIZE];
int dx[8] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[8] = {1, -1, 0, 0, -1, 1, -1, 1};

// void bfs(int x, int y)
// {
//     check[x][y] = 1;
//     for (int i = 0; i < 8; i++)
//     {
//         int nx = x + dx[i];
//         int ny = y + dy[i];
//         if (nx >= 0 && nx < x_size && ny >= 0 && ny < y_size)
//         {
//             if (check[nx][ny] == 0 && graph[nx][ny] == 1)
//             {
//                 bfs(nx, ny);
//             }
//         }
//     }
// }
void dfs(int x, int y, int num)
{
    check[x][y] = num;
    for (int k = 0; k < 8; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];
        //FB1. 범위검사
        if (nx < 0 || ny < 0 || nx >= x_size || ny >= y_size)
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
    while (true)
    {
        scanf("%d %d", &y_size, &x_size);
        if (!x_size && !y_size)
        {
            break;
        }
        fill(&check[0][0], &check[51][51] + 1, 0);
        fill(&graph[0][0], &graph[51][51] + 1, 0);
        for (int i = 0; i < x_size; i++)
        {
            for (int j = 0; j < y_size; j++)
            {
                int ele;
                scanf("%d", &ele);
                graph[i][j] = ele;
            }
        }
        int count = 0;
        for (int i = 0; i < x_size; i++)
        {
            for (int j = 0; j < y_size; j++)
            {
                if (check[i][j] == 0 && graph[i][j] == 1)
                {
                    dfs(i, j, count);
                    ++count;
                }
            }
        }
        printf("%d\n", count);
    }
}