//https://www.acmicpc.net/problem/9466
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 100001

using namespace std;

int stu[SIZE];    // 학생들의 배열
int Number[SIZE]; //  단지번호
int check[SIZE];  // 방문 x 0 | 방문 o 1이상 카운트 변수

int bfs(int who, int count, int Num)
{
    if (check[who] != 0)
    {
        if (Num != Number[who])
        {
            return 0;
        }
        return (count - check[who]);
    }
    check[who] = count;
    Number[who] = Num;
    return bfs(stu[who], count + 1, Num);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        for (int i = 1; i <= N; i++)
        {
            cin >> stu[i];
            //fb) 배열 초기화..!!
            Number[i] = 0;
            check[i] = 0;
        }

        int ans = 0;
        for (int i = 1; i <= N; i++)
        {
            if (check[i] == 0)
            {
                ans += bfs(i, 1, i);
            }
        }
        cout << N - ans << "\n";
    }
}

// 테스트 케이스가 여럿 있는경우라서, 매번 배열을 초기화 해주어야 한다.