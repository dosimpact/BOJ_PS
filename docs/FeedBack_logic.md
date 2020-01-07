# 로직컬 적인 오류를 정정합니다.

### 재귀함수 + for안에서 basecase에서 reture과 if+return의 차이

```cpp
bool dfs(int x,int c){
	check[x] = c;
	for(int i = 0 ; i < graph[x].size() ; i++){
		int node = graph[x][i];
		if(check[node] == 0){
			//FB1.얘는 for문을 중단시키고, dfs를 작동시키잖아
			//return dfs(node,3-c);.0
			//이녀석은 해당 조건에 맞으면 함수 중단 false반환 / 아니면 keep
			if(dfs(node,3-c) == false){return false;}
		}
		else if(check[node] == c){
			return false;
		}
	}
	return true;
}
```

### 인접 리스트에서 노드의 주변 노드는 graph[x][j] 이다.

```cpp
		bool isBi = true;
		for(int i = 1; i <= n; i++){
			for(int j = 0;  j < graph[i].size(); j++){
				int nnode = graph[i][j];
				//FB.
				//if(check[i] == check[nnode]){
				//	isBi = false;
				//}
				if(check[i] == check[nnode]){
					isBi = false;
				}
			}
		}
```

### for + return의 논리

```cpp
int length(int a, int p, int checknum)
{
    check[a] = checknum;
    int b = next(a, p);
    if (check[b] != 0)
    {
        return check[b] - 1;
    }
    else
    { //FB.return을 안적으면, 함수만 실행되고 결과가 리턴이 안되지..
        return length(b, p, checknum + 1);
    }
}
```

### 2차원 배열 초기화 by fill

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int check[2][2];
    check[0][0] = 1;
    check[0][1] = 2;
    check[1][0] = 3;
    check[1][1] = 4;
    fill(&check[0][0], &check[1][1] + 1, 0);
}
```

### bfs - 방문시 - 무조건 check는 0 외의 값

```cpp
    queue<int> q;
    q.push(x);
    //FB. 방문 했으면 0 을 넣으면 안되지.......n =5 k = 5 면 바로 찾는 0인 경우인데, 2가 나와버림.
	//check[x] = 0;
    check[x] = 1;
    while (!q.empty())
```

### database 필드 만들때 규칙 설계하기.

- 테트로미노 블럭 설계

```
 a[테트로미노의 19가지 모양중 어떤거?][ 3개의 블럭중 어느거?][ x,y 좌표 하나 골라]
```

```cpp
int a[19][3][2] = {
    {{0, 1}, {0, 2}, {0, 3}},
    {{1, 0}, {2, 0}, {3, 0}},
    {{1, 0}, {1, 1}, {1, 2}},
    {{0, 1}, {1, 0}, {2, 0}},
    {{0, 1}, {0, 2}, {1, 2}},
    {{1, 0}, {2, 0}, {2, -1}},
    {{0, 1}, {0, 2}, {-1, 2}},
    {{1, 0}, {2, 0}, {2, 1}},
    {{0, 1}, {0, 2}, {1, 0}},
    {{0, 1}, {1, 1}, {2, 1}},
    {{0, 1}, {1, 0}, {1, 1}},
    {{0, 1}, {-1, 1}, {-1, 2}},
    {{1, 0}, {1, 1}, {2, 1}},
    {{0, 1}, {1, 1}, {1, 2}},
    {{1, 0}, {1, -1}, {2, -1}},
    {{0, 1}, {0, 2}, {-1, 1}},
    {{0, 1}, {0, 2}, {1, 1}},
    {{1, 0}, {2, 0}, {1, 1}},
    {{1, 0}, {2, 0}, {1, -1}},

};
```

- 플러드 필 dx,dy 설계 두가지 방법

- 기존의 방법

```cpp
dx = { 0,0,-1,1};
dy = { 1,-1, 0,0};
```

```
d[어느 방면으로 갈래?][x,y좌표 어느거?]
```

```cpp
d = { {0,1}, {0,-1},{1,0},{-1,0}};
```

### 정렬를 하고 다음순열을돌려야, 모든 순열를 돌지 않는가!! | sort + next_permutation 은 거의 한 세트

### 재귀함수 설계할때, baseCase걸러내는거에서, 정답이 아닌경우가 먼저 나오니까 틀리게 되는 case가 있었어.

```cpp
    //FB, 다 만든경우를 먼저 따져야한다.
    //다 만든경우, 현재까지 만든 사이즈가 6이야, && next넘버가 없을지언정 답이 될수있다.
    if (current.size() == 6)
    {
        printNumber(current);
        return;
    }
    //다 못만든경우, 더이상 nextNumber가 없어.
    if (number.size() == nextNumber)
    {
        return;
    }
```

<<<<<<< HEAD

### 백트레킹 로직 - 반드시 백으로 노드를 돌아올때는 데이터를 싹 지우고 와야된다.

### + 무조건 조건을 만족한다고 해서 go(z+1)로 다음 노드로 가는게 아니라, (해당 두 노드만 전이조건을 만족할순 있어) 언제든 다시 원래 노드로 와서도 계속 탐색을 할 수 있어야 한다.

```cpp
//fb)백트래킹 이기때문에, 데이터를 싹다 지워야되고 + | 리턴값이 false이면 계속해서 탐색을 시작한다.

if 조건을 만족한 경우
for 계속 탐색을 하는 경우
    if 조건을 만족해서 go(z++)하는 경우
return 안되는경우

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
}
```

=======

### DFS check의 순서 논리 = 만약 다음 노드가 check가 안되있으면, check하고 .. 의 논리는 =>처음 시작하는 노드가 체크가 안됨

```cpp
void dfs(int x)
{
    //출력
    cout << x << " ";

    //주변 노드들을 돌면서, 방문안했다면 방문해주기.
    for (int i = 0; i < graph[x].size(); i++)
    {
        int next = graph[x][i];
        cout << "DEBUG" << x << " => " << next << "\n";
        if (check[next] == 0)
        {
            //fb) 이 코드에서는 처음 1이 들어올때, check를 안하기때문에 다시 1를 방문하게 될꺼임.
            //check[x] = 1;
            dfs(next);
        }
    }
}
```

### 간단하게 나누기, 나머지 구하는 함수, 매개변수 있는거 그대로 사용해~

```
//fb,왜 매개변수 x활용 안하는거야? - x의 각자리수마다 p씩 곱한 결과 출력하기.
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
    int sum = 0;
    while (x != 0)
    {
        sum += pow(x % 10, p);
        x = x / 10;
    }
    return sum;
}
```

> > > > > > > 2994ee1974dc28748a47225485fd5ca50dbbb7ff
