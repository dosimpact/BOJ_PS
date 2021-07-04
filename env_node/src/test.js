const [n, m] = [4, 4];
const inRange = (x, y) => 0 <= x && 0 <= y && x < n && y < m;
console.log(inRange(0, 4));
