#include <iostream>
#include <algorithm>
#include <vector>
#define SIZE 201
#define DIVIDER 1000000000ll;
using namespace std;
long long d[SIZE][SIZE];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, K;
    cin >> N >> K;
    for (int i = 0; i < SIZE; i++)
    {
        d[1][i] = 1ll;
    }
    for (int i = 2; i <= K; i++)
    {
        for (int j = 0; j <= N; j++)
        {
            for (int l = 0; l <= j; l++)
            {
                d[i][j] += d[i - 1][l];
                d[i][j] = d[i][j] % DIVIDER; //FB1. &뭔제
            }
        }
    }
    cout << d[K][N] << "\n";
    return 0;
}
