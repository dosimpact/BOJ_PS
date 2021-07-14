function primeSu(su) {
  return new Array(su)
    .fill(0)
    .map((e, i) => i + 1)
    .filter((e) => su % e === 0);
}

function isPrimeSuEven(su) {
  return primeSu(su).length % 2 === 0;
}

function solution(left, right) {
  let answer = 0;
  for (let i = left; i <= right; i++) {
    if (isPrimeSuEven(i)) answer += i;
    else answer -= i;
  }
  return answer;
}
console.log(primeSu(8));
console.log(solution(13, 17));
