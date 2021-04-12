const TC = `
4 2
4 2
3 1`;
const stdin =
  process.platform === "linux"
    ? require("fs").readFileSync("/dev/stdin").toString().split("\n")
    : TC.trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// let matrix = new Array(5).fill(0).map(() => new Array(4).fill(0));
// matrix = [...Array(5)].map(() => new Array(4).fill(0));

// 위상정렬 , [ 인접 리스트, 인차수 카운터]
const [V, E] = input().split(" ").map(Number);
const graph = new Array(V + 1).fill(0).map(() => new Array());
const inDeg = new Array(V + 1).fill(0);

for (let i = 0; i < E; i++) {
  const [u, v] = input().split(" ").map(Number);
  inDeg[v] += 1;
  graph[u].push(v);
}
// 큐 넣기
const q = new Array();
for (let i = 1; i <= V; i++) {
  if (inDeg[i] === 0) {
    q.push(i);
  }
}
// 방문 및 차수 0일때 엔큐
for (let i = 1; i <= V; i++) {
  const now = q.shift();
  process.stdout.write(`${now} `);
  for (const nxt of graph[now]) {
    inDeg[nxt] -= 1;
    if (inDeg[nxt] === 0) {
      q.push(nxt);
    }
  }
}
