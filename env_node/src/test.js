// 0~9 버튼 숫자
function solution(passwords, s) {
  // psswords 을 2차원 배열로 파싱한다.
  const db = {};
  for (let pair of passwords) {
    db[pair[0]] = pair[1];
  }
  let step = 1; //1 호수 , 2비번
  let inputPassword = "";
  let ans = 0;
  const pass = String(s).split("#").slice(0, -1);

  for (let p of pass) {
    if (step === 1) {
      if (p in db) {
        inputPassword = db[p];
        step = 2;
      }
    } else if (step === 2) {
      if (String(inputPassword) === String(p)) {
        ans += 1;
      }
      step = 1;
    }
  }
  // s를 split하여 읽으면서 password을 점검
  return ans;
}

console.log(
  solution(
    [
      [101, 101],
      [102, 102],
      [201, 101],
      [202, 101],
    ],
    "101#101#102#101#203#101#201#101#101#"
  )
);
