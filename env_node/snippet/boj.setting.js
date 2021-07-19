const TC = `
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.
`;

const stdin =
  process.platform === "linux"
    ? require("fs").readFileSync("dev/stdin").toString().split("\n")
    : TC.trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let ans = 0;
for (let i = 0; i <= 7; i++) {
  const row = input().split("");
  for (let j = 0; j <= 7; j++) {
    if ((i + j) % 2 === 0 && row[j] === "F") {
      ans += 1;
    }
  }
}
console.log(ans);
