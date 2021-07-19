
let ans = 0;
for (let i = 0; i <= 7; i++) {
  const row = input().split("");
  for (let j = 0; j <= 7; j++) {
    if ((i + j) % 2 === 0 && row[j] === "F") {
      console.log(i, j, row[j], row);
      ans += 1;
    }
  }
}
console.log(ans);
