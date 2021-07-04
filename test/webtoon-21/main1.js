// ? 달러 사는 경우 조건 ,
// ? 달러 + 한국돈에 d로 들어갸야 하나?

function solution(k, rates) {
  //초기금액,환율
  const d = new Array(rates.length).fill(0).map((e) => new Array(2).fill(0));
  // 달러 없어
  d[0][0] = k;
  // 달러 있어
  if (k >= rates[0]) d[0][1] = k - rates[0];

  for (let i = 1; i < rates.length; i++) {
    // 달러를 파는 경우
    d[i][0] = Math.max(...[...Array(i).keys()].map((j) => d[j][1])) + rates[i];
    // 달러를 사는 경우
    d[i][1] = Math.max(...[...Array(i).keys()].map((j) => d[j][0])) - rates[i];
  }
  console.log(d);
  return Math.max(...d.map((e) => e[0]));
}
// 2150
console.log(
  solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100])
);
// 환테크
// 초기 금액 k원
// 1달러만 사고, 1달러만 판매 가능
// 원화에는 제한이 없음
// ❌ typeing 너무 헷갈리낟. ( sum 에도, max에도 ... 천지)
