(() => {
  const TC = `
5
1 1
2 3
3 4
9 8
5 2
`;
  const stdin =
    process.platform === "linux"
      ? require("fs").readFileSync("/dev/stdin").toString().split("\n")
      : TC.trim().split("\n");

  const input = (() => {
    let line = 0;
    return () => stdin[line++];
  })();

  let t = Number(input());
  while (t--) {
    console.log(
      input()
        .split(" ")
        .map(Number)
        .reduce((a: number, c: number) => a + c)
    );
  }
})();
