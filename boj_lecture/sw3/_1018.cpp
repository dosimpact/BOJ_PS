//https://www.acmicpc.net/problem/1018
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#define SIZE 51
using namespace std;

char graph[SIZE][SIZE];
int n, m;
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> graph[i][j];
        }
    }
    //시작할 탐색 범위을 구한다.
    int xs = n - 7;
    int ys = m - 7;
    //cout << xs << " " << ys;
    int ans_min = -1;
    for (int i = 0; i < xs; i++)
    {
        for (int j = 0; j < ys; j++)
        { //시작 점들을 돌면서
            for (int k = 0; k < 2; k++)
            { //그래프 하나를 복제하고
                int changeCouter = 0;
                char graphCopy[SIZE][SIZE];
                copy(&graph[0][0], &graph[0][0] + SIZE * SIZE, &graphCopy[0][0]);
                //시작점이 다른 색일떄는?
                if (k == 1)
                {
                    graphCopy[i][j] == 'W' ? graphCopy[i][j] = 'B' : graphCopy[i][j] = 'W';
                }

                // 0열을 먼저 처리를 한다.
                for (int dx = i + 1; dx < i + 8; dx++) //fb for에서 i를 건드렸어...//fb) +8 만큼만 탐색을 해야자..
                {
                    //해당 부분이 전과 같으면 바꿔주고, 변수 증가 아니면 계속
                    if (graphCopy[dx - 1][j] == graphCopy[dx][j])
                    {
                        changeCouter += 1;
                        //fb)이렇게 바꾸면 똑같지..
                        //graphCopy[dx][j] = graphCopy[dx - 1][j];
                        graphCopy[dx][j] == 'W' ? graphCopy[dx][j] = 'B' : graphCopy[dx][j] = 'W';
                    }
                }
                // 0열 데이터를 가지고 각 행마다 체스판을 그린다.
                //fb) +8 만큼만 탐색을 해야자..
                for (int dx = i; dx < i + 8; dx++)
                {
                    for (int dy = j + 1; dy < j + 8; dy++)
                    {
                        if (graphCopy[dx][dy] == graphCopy[dx][dy - 1])
                        {
                            changeCouter += 1;
                            graphCopy[dx][dy] == 'W' ? graphCopy[dx][dy] = 'B' : graphCopy[dx][dy] = 'W';
                        }
                    }
                }
                // 바꿘 부분의 총 수를 구한다.
                // cout << "\n";
                // for (int i = 0; i < n; i++)
                // {
                //     for (int j = 0; j < m; j++)
                //     {
                //         cout << graphCopy[i][j];
                //     }
                //     cout << "\n";
                // }
                //cout << "changeCouter " << changeCouter << "<- ";
                if (ans_min == -1 || ans_min > changeCouter)
                {
                    ans_min = changeCouter;
                }
            }
        }
    }
    cout << ans_min;
    //cout << "ans_min " << ans_min << "<- ";
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << graphCopy[i][j];
    //     }
    //     cout << "\n";
    // }
}
/*
9 9
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
WWWWWWWWW
*/