#include <iostream>
#include <queue>
using namespace std;

//8개의 방향
int dy[8] = {-1, -2, -2, -1, 1, 2, 1, 2};
int dx[8] = {-2, -1, 1, 2, -2, -1, 2, 1};

int main()
{
    int T, l, sx, sy, ex, ey; //l: 길이 sx,sy:시작 위치  ex,ey:목표 위치
    cin >> T;

    for (int testCase = 0; testCase < T; testCase++)
    {

        scanf("%d %d %d %d %d", &l, &sx, &sy, &ex, &ey);

        int visited[300][300] = {0};

        queue<pair<int, pair<int, int>>> q;
        q.push(make_pair(0, make_pair(sy, sx))); //시간, y좌표, x좌표
        visited[sy][sx]++;

        while (!q.empty())
        {
            int y = q.front().second.first;
            int x = q.front().second.second;
            int cnt = q.front().first;
            q.pop();

            if (y == ey && x == ex)
            {
                cout << cnt << endl;
                break;
            }

            for (int i = 0; i < 8; i++)
            {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (ny < 0 || ny >= l || nx < 0 || nx >= l)
                    continue;

                if (visited[ny][nx])
                    continue;

                visited[ny][nx] = visited[x][y] + 1;
                q.push(make_pair(cnt + 1, make_pair(ny, nx)));
            }
        }
        for (int i = 0; i < l; i++)
        {
            for (int j = 0; j < l; j++)
            {
                cout << visited[i][j] << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}

/*
1
8
0 0
7 0

*/