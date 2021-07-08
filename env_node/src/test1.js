// 소수인지 아닌지 체큰
// 5
// 1,5
// 16
// 1,16  | 2,8
// 루트 16
console.log(Math.floor(Math.sqrt(16)));
function isPrime(su) {
  for (let i = 2; i <= Math.floor(Math.sqrt(su)); i++) {
    if (su % i === 0) return false;
  }
  return true;
}
for (let i of new Array(10).fill(0).map((_, i) => i + 1)) {
  console.log(`${i} ${isPrime(i)}`);
}
console.log(5 % 1);
