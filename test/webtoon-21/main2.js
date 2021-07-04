//
// 머니 리밋 , cost 배열
function solution(money, cost) {
  cost = cost.map(Number);
  const d = new Array(cost.length).fill(0).map((e) => new Object()); // 0층 부터

  if (cost[0] <= money) {
    d[0] = { [Number(cost[0])]: 1 }; // 해당 돈으로 길이 1을 늘렸다.
  }
  for (let i = 1; i < cost.length; i++) {
    // 첫번째 층의 cost 먼저 살핀다.
    // 새로 가는 경우
    if (cost[i] <= money) {
      d[i] = { ...d[i], [Number(cost[i])]: 1 };
    }
    // 이어 가는 경우 - 가격 제한 체크
    for (let prev_cost in d[i - 1]) {
      if (Number(prev_cost) + Number(cost[i]) <= money) {
        const new_cost = [Number(prev_cost) + Number(cost[i])];
        const new_len = d[i - 1][prev_cost] + 1;

        if (d[i].hasOwnProperty(new_cost) && d[i][new_cost] > new_len) continue;
        d[i] = { ...d[i], [new_cost]: new_len };
      }
    }
  }
  // console.log(d);
  let ansMax = [0];
  for (let i = 0; i < d.length; i++) {
    for (let key in d[i]) {
      ansMax.push(d[i][key]);
    }
  }
  return Math.max(...ansMax);
}
console.log(solution(420, [0, 900, 0, 200, 150, 0, 30, 50, 60, 60, 60]));

//❌ object key에 number를 넣고 싶다.
//❌ object 를 key값 존재성 + 추가만, 새로 할당 아닌
