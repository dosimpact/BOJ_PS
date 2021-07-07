function solution(dart) {
  const sum = (...arr) => [...arr].reduce((prev, val) => prev + val, 0);
  dart = String(dart);
  const answer = new Array();
  // dart
  while (dart) {
    let p = dart[0];
    dart = dart.slice(1);
    if (/[SDT]/.test(p)) {
      if (p === "D") {
        answer[answer.length - 1] = answer[answer.length - 1] ** 2;
      } else if (p === "T") {
        answer[answer.length - 1] = answer[answer.length - 1] ** 3;
      }
    } else if (/[*#]/.test(p)) {
      if (p === "#") {
        answer[answer.length - 1] = -answer[answer.length - 1];
      } else {
        answer[answer.length - 1] = answer[answer.length - 1] * 2;
        if (answer.length >= 2)
          answer[answer.length - 2] = answer[answer.length - 2] * 2;
      }
    } else {
      if (p === "1" && dart[0] === "0") {
        p += dart[0];
        dart = dart.slice(1);
      }
      answer.push(Number(p));
    }
  }
  console.log(answer);
  return sum(...answer);
}
console.log(solution("1S2D*3T"));
