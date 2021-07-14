// 체육복 도난
// 바로앞 혹은 뒤 학생 빌려줄 수 있다.
//
function solution(n, lost, reserve) {
  let answer = 0;
  const stu = new Array(n).fill(1);
  for (let i of lost) stu[i - 1] -= 1;
  for (let i of reserve) stu[i - 1] += 1;
  for (let [idx, s] of stu.entries()) {
    if (s == 0) {
      // 앞사람 빌리기 시도 , 안되면 뒷사람 빌리기 시도
      if (idx >= 1 && stu[idx - 1] >= 2) {
        stu[idx - 1] -= 1;
        stu[idx] += 1;
      } else if (idx <= stu.length - 1 && stu[idx + 1] >= 2) {
        stu[idx + 1] -= 1;
        stu[idx] += 1;
      }
    }
  }
  console.log(stu);
  return stu.filter((s) => s >= 1).length;
}
// console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [2, 4], [3]));
