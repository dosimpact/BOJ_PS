const fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split("\n");

var [vertex, edge, start] = input[0].split(" ").map((x) => parseInt(x));

var adj = new Array(vertex + 1);
for (let i = 0; i <= vertex; i++) adj[i] = [];

for (let i = 1; i <= edge; i++) {
  var [from, to] = input[i].split(" ").map((x) => parseInt(x));
  adj[from].push(to);
  adj[to].push(from);
}

for (let i = 1; i <= vertex; i++) adj[i].sort((x, y) => x - y);

var visit = new Array(vertex + 1);
visit.fill(false);

function dfs(now) {
  visit[now] = true;
  process.stdout.write(now + " ");
  for (let next of adj[now]) if (!visit[next]) dfs(next);
}
function bfs(now) {
  visit = new Array(vertex + 1);
  visit.fill(false);
  visit[now] = true;
  q = [];
  q.push(now);
  process.stdout.write(now + " ");

  while (q.length > 0) {
    var now = q.shift();
    for (let next of adj[now])
      if (!visit[next]) {
        visit[next] = true;
        q.push(next);
        process.stdout.write(next + " ");
      }
  }
}

dfs(start);
console.log();
bfs(start);
