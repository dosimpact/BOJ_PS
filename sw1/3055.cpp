//https://www.acmicpc.net/problem/3055
#include <cstdio>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#define SIZE 51
using namespace std;

char graph[SIZE][SIZE]; // 입력
int X, Y;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int water[SIZE][SIZE];
int gosum[SIZE][SIZE];
int main()
{
    int gulx, guly;
    int gox, goy;
    fill(&water[0][0], &water[0][0] + SIZE * SIZE, -1);
    fill(&gosum[0][0], &gosum[0][0] + SIZE * SIZE, -1);
    queue<pair<int, int>> q;
    //지도 입력
    scanf("%d %d", &X, &Y);
    for (int i = 0; i < X; i++)
    {
        for (int j = 0; j < Y; j++)
        {
            scanf("%1s", &graph[i][j]);
            if (graph[i][j] == '*')
            {
                q.push({i, j});
                water[i][j] = 0;
            }
            if (graph[i][j] == 'S')
            {
                tie(gox, goy) = tie(i, j);
                gosum[i][j] = 0;
            }
            if (graph[i][j] == 'D')
            {
                tie(gulx, guly) = tie(i, j);
            }
        }
    }
    //물먼저 이동
    while (!q.empty())
    {
        // 현재 노드 빼기
        int x, y;
        tie(x, y) = q.front();
        q.pop();
        //주변 노드 탐색 | 범위 체크 | 갈수있다면( D가 아니고, X도 아니고,*도아니고) | 방문안했다면
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < 0 || ny < 0 || nx >= X || ny >= Y)
                continue;
            if (graph[nx][ny] == 'D' || graph[nx][ny] == 'X')
                continue;
            if (water[nx][ny] == -1)
            { //방문 -> 가중치 + 1 , 큐 푸시
                water[nx][ny] = water[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    //고슴도치 이동
    q.push({gox, goy});
    while (!q.empty())
    {
        //현재 노드 출력
        int x, y;
        tie(x, y) = q.front();
        q.pop();
        // 주변 노드 탐색 | 범위 체크 | 갈수 있으면 - 돌맹이 체크 + 이동후에도 물보다 작아야함 | 방문안했다면 | 방문
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < 0 || ny < 0 || nx >= X || ny >= Y)
                continue;
            if (graph[nx][ny] == 'X' || (water[nx][ny] != -1 && water[nx][ny] <= gosum[x][y] + 1))
                continue;
            if (gosum[nx][ny] == -1)
            {
                gosum[nx][ny] = gosum[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    gosum[gulx][guly] == -1 ? printf("%s", "KAKTUS") : printf("%d", gosum[gulx][guly]);
}