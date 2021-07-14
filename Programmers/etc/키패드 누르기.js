// 손가락 위치 , 왼 별, 오 샵
// 이동 규칙 , 4방향, 거리 1씩 이동
// 왼쪽열 -> 왼손, 오른쪽 열 -> 오른손
// 가운데 -> 가까운 손가락 우선 사용 , 같다면 잡이손 이용
//

function solution(numbers, hand) {
  let answer = "";
  let lhand = [3, 0];
  let rhand = [3, 2];
  const numToPoint = (num) => {
    if (num === 0) return [3, 1];
    return [Math.floor((num - 1) / 3), (num - 1) % 3];
  };
  const getDist = (hand, x, y) => {
    if (hand === "L") {
      return Math.abs(lhand[0] - x) + Math.abs(lhand[1] - y);
    } else {
      return Math.abs(rhand[0] - x) + Math.abs(rhand[1] - y);
    }
  };
  // 숫자들을 순회하면서
  for (let num of numbers) {
    if ([1, 4, 7].includes(num)) {
      // 왼쪽열인 경우 - 답 추가,위치 이동
      answer += "L";
      lhand = numToPoint(num);
    }
    if ([3, 6, 9].includes(num)) {
      // 오른쪽 열인 경우 - 답 추가,위치 이동
      answer += "R";
      rhand = numToPoint(num);
    }
    if ([2, 5, 8, 0].includes(num)) {
      const lD = getDist("L", numToPoint(num)[0], numToPoint(num)[1]);
      const rD = getDist("R", numToPoint(num)[0], numToPoint(num)[1]);
      console.log(`[${num}] ${lD} ${rD} `);
      if (lD < rD) {
        answer += "L";
        lhand = numToPoint(num);
      } else if (lD > rD) {
        answer += "R";
        rhand = numToPoint(num);
      } else {
        if (hand === "right") {
          answer += "R";
          rhand = numToPoint(num);
        } else {
          answer += "L";
          lhand = numToPoint(num);
        }
      }
    }
  }
  // 가운데인 경우 - 거리 계산 - 같다면 잡이손 - 답추가 ,위치 이동
  return answer;
}

s = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left");
console.log(s);
