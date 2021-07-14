function isPrimeSuEven(su) {
  return (
    new Array(su)
      .fill(0)
      .map((_, i) => i + 1)
      .filter((e) => su % e === 0).length %
      2 ===
    0
  );
}

function solution(left, right) {
  let answer = 0;
  for (let i = left; i <= right; i++) {
    if (isPrimeSuEven(i)) answer += i;
    else answer -= i;
  }
  return answer;
}
console.log(solution(13, 17));
