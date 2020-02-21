

#include <cstdio>

int a[100001]; // 입력
int d[100001]; // 카운트 체크
int s[100001]; // 시발점 체크

int n;

int dfs(int x, int cnt, int &step) //  누구인지 몇번째 시작점
{

    if (d[x] != 0) // 첫 방문이 아니다.
    {
        if (step != s[x]) // 시작점과 끝점
        {
            return 0;
        }
        printf("DEBUG: %d x:%d step:%d \n", cnt - d[x], x, step);
        for (int i = 1; i <= n; i++)
        {
            printf(" %d ", s[i]);
        }
        return cnt - d[x]; //
    }
    d[x] = cnt;
    s[x] = step;
    return dfs(a[x], cnt + 1, step);
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &a[i]);
            d[i] = 0;
            s[i] = 0;
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
        {
            if (d[i] == 0)
            {
                ans += dfs(i, 1, i);
            }
        }
        printf("%d\n", n - ans); //ans는 되는 녀석들만 나온다.
    }
    return 0;
}