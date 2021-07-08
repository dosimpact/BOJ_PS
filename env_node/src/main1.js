const TC = `
4 5 1
1 2
1 3
1 4
2 4
3 4
`;
const print = (str) => process.stdout.write(`${str}`);
const stdin =
  process.platform === "linux"
    ? require("fs").readFileSync("/dev/stdin").toString().split("\n")
    : TC.trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// 정점, 간선 , 탐색 시작
const [N, M, V] = input().split(" ").map(Number);

// input &
const graph = new Array(N + 1).fill(null).map(() => new Array());
let check = new Array(N + 1).fill(null).map(() => false);

for (let i = 0; i < M; i++) {
  const [u, v] = input().split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}
// sort
for (let i = 0; i <= N; i++) {
  graph[i].sort();
}
// DFS
//
const DFS = (x) => {
  print(`${x} `);
  for (let nxt of graph[x]) {
    if (check[nxt] === false) {
      check[nxt] = true;
      DFS(nxt);
    }
  }
};
check[V] = true;
DFS(V);
// BFS
check = new Array(N + 1).fill(null).map(() => false);
const BFS = (x) => {
  const q = Array();
  check[x] = true;
  print(`${x} `);
  q.push(x);
  while (q.length >= 1) {
    const now = q.shift();
    for (let nxt of graph[now]) {
      if (check[nxt] === false) {
        check[nxt] = true;
        print(`${nxt} `);
        q.push(nxt);
      }
    }
  }
};
print(`\n`);
BFS(V);
