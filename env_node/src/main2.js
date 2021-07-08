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
    ? require("fs").readFileSync("dev/stdin").toString().split("\n")
    : TC.trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [vertex, edge, start] = input().split(" ").map(Number);
const adj = new Array(vertex + 1).fill(0).map(() => new Array());
const check = new Array(vertex + 1).fill(false);

for (let i = 1; i <= edge; i++) {
  var [from, to] = input()
    .split(" ")
    .map((x) => parseInt(x));
  adj[from].push(to);
  adj[to].push(from);
}
for (let i = 1; i <= vertex; i++) adj[i].sort((x, y) => x - y);

function DFS(x) {
  print(`${x} `);
  for (let nxt of adj[x]) {
    if (!check[nxt]) {
      check[nxt] = true;
      DFS(nxt);
    }
  }
}
function BFS(x) {
  const q = new Array();
  q.push(x);
  check[x] = true;
  print(`${x} `);

  while (q.length > 0) {
    const now = q.shift();
    for (let nxt of adj[now]) {
      if (!check[nxt]) {
        check[nxt] = true;
        print(`${nxt} `);
        q.push(nxt);
      }
    }
  }
}

check[start] = true;
DFS(start);

print("\n");
check.fill(false);
BFS(start);
