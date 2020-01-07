//https://www.acmicpc.net/problem/1012
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
<<<<<<< HEAD
int graph[10][10];
int c1[10][10]; // 행 체크
int c2[10][10]; // 열 체크
int c3[10][10]; // 스퀘어 체크
void printGraph()
{
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << "\n";
    }
}
int squre(int x, int y)
{
    return ((x / 3) * 3) + (y / 3);
}
//fb)백트래킹 이기때문에, 데이터를 싹다 지워야되고 + | 리턴값이 false이면 계속해서 탐색을 시작한다.
bool go(int z)
{
    if (z == 81)
    {
        //다 두었으면,출력하고 리턴하기
        printGraph();
        return true;
    }
    //다음 z를 넘어가는데,
    //그래프에 이미 0아닌 숫자면, 다음 노드로
    int x = z / 9;
    int y = z % 9;
    if (graph[x][y] != 0)
    {
        return go(z + 1);
    }
    else
    {
        //아니라면 1부터 9까지 돎면서 check를 통해 다 허락을 받으면, 두기.
        for (int i = 1; i <= 9; i++)
        {
            if ((c1[x][i] == 0) && (c2[y][i] == 0) && (c3[squre(x, y)][i] == 0))
            {
                c1[x][i] = c2[y][i] = c3[squre(x, y)][i] = 1;
                graph[x][y] = i;
                //go에서 백트래킹을 종료하는 로직.
                if (go(z + 1))
                {
                    return true;
                }
                //fb) 그래프를 0으로 만들어주어야된다. 그래야. 백트래킹 했던 흔적을 지워야지. 안그러면, graph에 숫자가 남아서 그냥 다음노드로 넘어가잖아..
                graph[x][y] = 0;
                c1[x][i] = c2[y][i] = c3[squre(x, y)][i] = 0;
            }
        }
        return false;
    }
=======
int a, p;
int check[10000001];
int pow(int a, int p)
{
    int ans = 1;
    for (int i = 1; i <= p; i++)
    {
        ans *= a;
    }
    return ans;
>>>>>>> 2994ee1974dc28748a47225485fd5ca50dbbb7ff
}
// int nextNode(int x)
// {
//     int sum = 0;
//     do
//     {
//         int a = x / 10;
//         int b = x % 10;
//         sum += pow(b, p);
//     } while (a != 0);
//     return sum;
// }
int nextNode(int x)
{
<<<<<<< HEAD
    //스토구 입력받기.
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            int tmp;
            cin >> tmp;
            graph[i][j] = tmp;
            if (tmp != 0)
            {
                // i행에 3은 있다.
                c1[i][tmp] = 1;
                // j열에 3은 있다.
                c2[j][tmp] = 1;
                // i,j행의 사각형안에 3은 있다.
                c3[squre(i, j)][tmp] = 1;
            }
        }
    }
    go(0);
    //printGraph();
    //cout << squre(8, 8);
}
/*
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
=======
    int sum = 0;
    while (x != 0)
    {
        sum += pow(x % 10, p);
        x = x / 10;
    }
    return sum;
}
void dfs(int x, int checkNum)
{
    //현재 노드를 체크해주고, 다음 노드를 구해온다.
    check[x] = checkNum;
    int next = nextNode(x);
    //cout << "DEBUG" << x << " -> " << next << "\n";
    if (check[next] == 0)
    { //다음 노드가 방문 안했다면 다음노드로 방문하고, 체크를 +1
        dfs(next, checkNum + 1);
    }
    else
    {
        //방문했다면 다음노드의 체크넘버보다 -1 출력
        cout << check[next] - 1;
        return;
    }
}
int main()
{
    cin >> a >> p;
    dfs(a, 1);
    //cout << pow(2, 3) << "\n";
    //cout << nextNode(a);
}
>>>>>>> 2994ee1974dc28748a47225485fd5ca50dbbb7ff
