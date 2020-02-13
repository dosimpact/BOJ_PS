#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <tuple>
#define SIZE 101
using namespace std;

int x, y;
int check[SIZE][SIZE];

int bfs(int u, int v, vector<vector<int>> &graph)
{
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    int counter = 1;
    check[u][v] = 1;
    queue<pair<int, int>> q;
    q.push({u, v});
    while (!q.empty())
    {
        int nowx, nowy;
        tie(nowx, nowy) = q.front();
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = nowx + dx[k];
            int ny = nowy + dy[k];
            //다음 그래프의 범위체크 | 같은 영역 | 방문 x 라면 | 방문해주기
            if ((nx >= 0 && ny >= 0 && nx < x && ny < y) && graph[nx][ny] == graph[nowx][nowy] && check[nx][ny] == -1)
            {
                check[nx][ny] = 1;
                q.push({nx, ny});
                counter++;
            }
        }
    }
    return counter;
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture)
{
    int number_of_area = 0;
    int max_size_of_one_area = -1;

    graph = picture;
    tie(x, y) = tie(m, n);
    fill(&check[0][0], &check[0][0] + SIZE * SIZE, -1);
    // 전체 그래프 돌면서 - picture가 있고,방문하지 않았다면 -> 방문
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if (picture[i][j] != 0 && check[i][j] == -1)
            {
                bfs(i, j, picture);
                number_of_area++;
            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}