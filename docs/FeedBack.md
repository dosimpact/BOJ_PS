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
