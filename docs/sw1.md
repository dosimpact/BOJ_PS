# SW1 공부합시다아.~!@

# 1.Brute Force

### 풀이법

1. 문제의 가능한 경우의수를 연필로 도출함. BF될것같나? 시간제한 조건을 보면됨. | 일부로 풀리겠끔 N제한을 두는경우가 있음.
2. 풀이 방법 선택 : 그냥다해보기 | for문 사용 | 순열 사용 | 재귀 사용 | 비트 마스크 사용.

- 1.그냥 다해보기 : 테트로미노,ESM날짜, 아홉 난쟁이
- 1.N중 for문 : 1,2,3 더하기, 제일끔찍한 코드중 하나
- 2.1 순열 사용 : 다음 순열 직접 만들기. 외판원순회
- 2.2 순열을 이용한 조합 사용 : 로또 문제, 연산자끼워넣기 문제.

- example) 다음순열 직접 구현

```cpp
void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
bool next_permu(int *a, int n)
{
    //배열을 i로 뒤부터 돌면서, i가 0보다 클때까지 | a[i] 가 뒷녀석보다 큰 지점을 찾는다.
    int i = n - 1;
    while (i > 0 && a[i - 1] >= a[i]) i--;
    //만약 i가 0 이하면 리턴 F
    if (i <= 0)return false;
    //배열을 j로 뒤부터 돌면서, a[i-1]보다 큰 j를 찾는다.
    int j = n - 1;
    while (a[i - 1] >= a[j])j--;
    //swap i-1 ,j
    swap(a[i - 1], a[j]);
    //배열을 j로뒤부터 돌면서,i를 앞으로 돌면서 i와j를 swap 해나간다.
    j = n - 1;
    while (i < j){swap(a[i], a[j]);i++;j--; }
    return true;
}
```

- 3.재귀함수 이용하기. | 1,2,3 더하기 백트래킹버전 | 암호만들기.
- 보통 2^20까지는 1초내로 가능(20제한), N^3은 500제한,

# 1.2 Brute Force NM

- 반드시 중복제거하는 유니크 쓸때는, sort->erase(unique) 3단계를 거칠것!!!!
-     int ans = 2 147 483 647;

```
N과M논리장

//1. 중복 없이 고르는 순열

//n,m입력받고, 출력할 데이터 a배열, 체크 c배열
//go(idx) for문으로 1~n까지 돌면서, 만약 이미 들어간 경우면 계속
//아닌경우에는 c체크해주고 a넣고 go(++)
//그리고 c체크 풀고 for로 계속~

//2. 중복 없이 고르는 조합

//1.번의 상황에서 start를 추가해주면됨.

//1-n을 순환하는것이 아닌, 노드의 데이터만을 이용하는 방법
//go(int ac, int idx) a cursor, idx 고를 숫자.
//다 고른 경우에는 출력후 리턴, 다 못만들고 고를게 없는경우 리턴
//고를 숫자를 고르고 go | 고를 숫자를 스킵하고 go

//3. 중복 허용 고르는 순열

//1.번의 논리에서
//c체그만 빼주면 된다.

//4. 중복 허용 고르는 조합

//nm 다시 리뷰 ...
start는 i로 넣기!! // 만약 i+1를 넣어버리면, check할 필요성이 없어지긴 함...
중복 x 순열// check
중복 x 조합// start check
중복 o 순열//
중복 o 조합// start
```

# 2. BFS

### 문제 유형 : 노드가 분리되는 경우 ( 클립보드에 복사를 해둔다던가, 벽을 부순다던가. )

- 2차원 배열로 간다. ex) 이모티콘 문제 - (s,c) 이차원배열로 , (n,0~n) 까지의 노드를 모두 bfs 탐색을 통해 가 봐야함. - 사실 제일 먼저 도달하는 녀석을 구하면 됨.

### 문제 유형 : 다음 노드로 가는데 가중치가 다른 경우

- 가중치 종류가 2개라면 : 이중 큐나 덱을 사용한다. ex) 숨바꼭질3 - 순간이동(0),걷기(1) => 순간이동을 먼저 다 q1으로 돌고 , q2로 간다.
- 가중치 종류가 3개 이상이라면: 다중 큐를 사용한다.

- ex) 일반화된 큐

```cpp
//https://www.acmicpc.net/problem/13549
#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#define SIZE 100001
using namespace std;
int d[SIZE];

int main()
{
    fill(&d[0], &d[0] + SIZE, -1);
    int n, k;
    cin >> n >> k;
    vector<queue<int>> rotation_q;
    rotation_q.push_back(queue<int>());
    rotation_q.push_back(queue<int>());
    rotation_q[0].push(n);
    d[n] = 0;
    while (!rotation_q[0].empty())
    {
        //현재 위치 빼기
        int now = rotation_q[0].front();
        rotation_q[0].pop();
        if (now == k)
        {
            cout << d[now];
            return 0;
        }
        // 순간이동 x => x*2    // 범위 체크 | 방문 여부 | ,q1에 가중치 없이 계속 넣어준다.
        if (now * 2 <= SIZE)
        {
            if (d[now * 2] == -1)
            {
                d[now * 2] = d[now];
                rotation_q[0].push(now * 2);
            }
        }
        // 걷기 x => x+1 // 범위 체크 / 방문 여부 / q2.에 가중치 + 1
        if (now + 1 <= SIZE)
        {
            if (d[now + 1] == -1)
            {
                d[now + 1] = d[now] + 1;
                rotation_q[1].push(now + 1);
            }
        }
        // x => x - 1  // 범위 체크 / 방문 여부 / q2.에 가중치 + 1
        if (now - 1 >= 0)
        {
            if (d[now - 1] == -1)
            {
                d[now - 1] = d[now] + 1;
                rotation_q[1].push(now - 1);
            }
        }
        //q1이 비워졌다면 , q1을 2로 교체 후 q2는 비워 두기
        if (rotation_q[0].empty())
        {
            rotation_q.erase(rotation_q.begin(), rotation_q.begin() + 1);
            rotation_q.push_back(queue<int>());
        }
    }
}
```
