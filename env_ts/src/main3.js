// 1~n까지의 역이 철로로 연결
// 양뱡향 그래프, 임의 두역은 1개 간선,서로다른 역 이동 경로 한가지, 컴포넌트 없음
// 출발역 1번 -> 도착역 왕복
// 일일 이용객수 합 최대 , 여러개라면 그 중 번호가 큰 역
"use strict";
function solution(N, passenger, train) {
  // 인접 행렬 만들기
  const graph = Array(N + 1).fill([]); // 0 안사용
  const check = Array(N + 1).fill(0);
  for (let [u, v] of train) {
    graph[u] = [...graph[u], v];
    graph[v] = [...graph[v], u];
  }
  // 다익스트라 알고리즘 ❌ - 싸이클 형성시 문제
  // BFS 탐색, check 가 더 크다면 재방문 가능
  const q = [1];
  check[1] = passenger[1 - 1];
  while (q.length !== 0) {
    const now = q.pop(0);

    for (let nxt of graph[now]) {
      // console.log(`now ${now} -> nxt ${nxt}`);
      if (check[nxt] !== 0) continue;
      check[nxt] = check[now] + passenger[nxt - 1];
      q.push(nxt);
    }
  }
  // 정답 구하기 - 거리가 가장 큰 노드와 그 번호 , sort해서 출력
  var answer = [];
  for (let [idx, c] of check.entries()) {
    if (idx == 0) continue;
    answer = [...answer, [idx, c]];
  }
  answer.sort(function (a, b) {
    return b[1] - a[1] || b[0] - a[0];
  });
  return answer[0];
}

let res = solution(
  6,
  [1, 1, 1, 1, 1, 1],
  [
    [1, 2],
    [1, 3],
    [1, 4],
    [3, 5],
    [3, 6],
  ]
);
console.log(res);
