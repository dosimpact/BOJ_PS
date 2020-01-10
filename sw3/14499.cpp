//https://www.acmicpc.net/problem/14499
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
vector<int> dice(6);
int graph[21][21];
int n, m, x, y, k;
vector<int> kv;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
void printDice()
{
    for (auto _dice : dice)
    {
        cout << _dice << " ";
    }
    cout << "\n";
}
int main()
{
    cin >> n >> m >> x >> y >> k;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> graph[i][j];
        }
    }
    for (int i = 0; i < k; i++)
    {
        int tmp;
        cin >> tmp;
        kv.push_back(tmp);
    }
    //입력 완료
    for (int i = 0; i < kv.size(); i++)
    {
        //명령얼르 하나씩 꺼내어.
        int cmd = kv[i] - 1;
        //cout << cmd << " ";

        //다음 칸으로 갈수 없으면 스킵 , 갈수 있다면,
        // 주사위를 굴렸을 때, 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
        int nx = x + dx[cmd];
        int ny = y + dy[cmd];
        if (nx < 0 || ny < 0 || nx >= n || ny >= m)
            continue;

        //주사위 이동시키기.
        vector<int> tmp_dice(6, 0);
        tmp_dice = dice;
        if (cmd == 0)
        {
            tmp_dice[1] = dice[4];
            tmp_dice[3] = dice[5];
            tmp_dice[4] = dice[3];
            tmp_dice[5] = dice[1];
        }
        else if (cmd == 1)
        {
            tmp_dice[1] = dice[5];
            tmp_dice[3] = dice[4];
            tmp_dice[4] = dice[1];
            tmp_dice[5] = dice[3];
        }
        else if (cmd == 2)
        {
            tmp_dice[0] = dice[1];
            tmp_dice[1] = dice[2];
            tmp_dice[2] = dice[3];
            tmp_dice[3] = dice[0];
        }
        else if (cmd == 3)
        {
            tmp_dice[0] = dice[3];
            tmp_dice[1] = dice[0];
            tmp_dice[2] = dice[1];
            tmp_dice[3] = dice[2];
        }
        dice = tmp_dice; //주사위 바꾸기.

        if (graph[nx][ny] == 0)
        {
            //이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
            graph[nx][ny] = dice[3];
        }
        else
        {
            //  0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
            dice[3] = graph[nx][ny];
            graph[nx][ny] = 0;
        }
        x = nx;
        y = ny;
        cout << dice[1] << "\n";
    }
}