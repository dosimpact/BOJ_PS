const TC = `
3 1
21 21 80 80
41 41 60 60
71 71 90 90
`;

const stdin =
  process.platform === "linux"
    ? require("fs").readFileSync("/dev/stdin").toString().split("\n")
    : TC.trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
// 2차원 Array
const graph = Array.apply(null, { length: 100 }).map((_) =>
  new Array(100).fill(0)
); //new Array(100).fill(new Array(100).fill(0));
// for + func
for (let i = 0; i < N; i++) {}
[...Array(N).keys()].forEach(() => {
  const [x1, y1, x2, y2] = input().split(" ").map(Number);
  console.log(x1, y1, x2, y2);
  for (let i = x1; i <= x2; i++) {
    for (let j = y1; j <= y2; j++) {
      graph[i][j] += 1;
    }
  }
});
// filter
let total = 0;
for (const row of graph) {
  total += row.filter((e) => e > M).length;
  // console.log(row);
}
console.log(total);
