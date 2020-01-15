# 문제 푸는 태도와 습관을 정정합니다.

### BFS 어려운 문제를 풀면서, 느낀것은 내 머리속으로 생각하고 코드를 쓰고 하는데는 한계가 있다.

- ???? 최대한 많이 주석으로 논리를 적어두고, 코드로 하나하나 구현하는 방법을 무조건 쓰자.!!! ????

### 백트래킹 하면서 느낀건데, 1문제 푸는거기 떄문에, 그냥 전역변수 남발해도 상관 없다.!!

- 구지 재귀함수에 파리미터 늘리지 말고, 전역변수로 만들어 버려.

```cpp
void go(int sum, int index)
{
    //인덱스 끝이
    if (index == n)
    {
        if (sum == s)
        {
            ans++;
        }
        return;
    }
    go(sum + a[index], index + 1);
    go(sum, index + 1);
}
```

```cpp
int go(vector<int> &number, vector<int> current, int nextNumber)
{
    int row = 0;
    //fb)계속 더하다가 0이 되는 경우도 있어.
    //현재의 합을 계산해보고 맞으면 1를 반환
    if (isSumS(current) && number.size() == nextNumber)
    {
        return 1;
    }
    //더 고를게 없으면 0 빈환
    if (!isSumS(current) && number.size() == nextNumber)
    {
        return 0;
    }
    //계속.
    current.push_back(number[nextNumber]);
    row += go(number, current, nextNumber + 1);
    current.pop_back();
    row += go(number, current, nextNumber + 1);

    return row;
}
```
