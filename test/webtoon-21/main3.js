// block borad
//

const bPoints = [
  [
    [1, 0],
    [2, 0],
  ],
  [
    [0, 1],
    [0, 2],
  ],
  [
    [1, 0],
    [1, 1],
  ],
  [
    [0, 1],
    [-1, 1],
  ],
  [
    [0, 1],
    [1, 1],
  ],
  [
    [0, 1],
    [1, 0],
  ],
];
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);
function solution(block, board) {
  const getScore = (board) => {
    let row = 0;
    const goal = board[0].length;

    for (let i = 0; i < board.length; i++) {
      if (goal === sum(...board[i])) row += 1;
    }
    return row;
  };
  const [n, m] = [board.length, board[0].length];
  const inRange = (x, y) => 0 <= x && 0 <= y && x < n && y < m;
  const answer = [0];

  // 보드판을 순회한다. | 보드가 놓일수 있는경우 , 없는 경우
  // block 을 놓는다.

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      let cannot = false;
      const blockPoints = [[i, j]];
      blockPoints.push(
        ...bPoints[block].map((pint) => [pint[0] + i, pint[1] + j])
      );
      // 범위 체크
      for (const [x, y] of blockPoints) {
        if (!inRange(x, y)) cannot = true;
      }
      if (cannot) continue;

      // 보드 1 인지 체크
      for (const [x, y] of blockPoints) {
        if (board[x][y] === 1) cannot = true;
      }
      if (cannot) continue;

      // 보드 0 이라면
      blockPoints.forEach(([x, y]) => {
        board[x][y] = 1;
      });
      const result = getScore(board);
      answer.push(result);
      // 원상태
      blockPoints.forEach(([x, y]) => {
        board[x][y] = 0;
      });
    }
  }
  return Math.max(...answer);
}

console.log(
  solution(5, [
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
  ])
);

// ❌ for - cannot continue 내부 for문만 작동했었음
// ❌ for i=0  - arr.legnth 로 해야한다. ( of 가 아닌 .. )
