// 상품번호가 적힌 상품권, 교환가능
// 원치않은 상품 받는것 최소로

function solution(gift_cards, wants) {
  // 현재 기프트 카드 -> dict, wants에 서 빼,
  const remain = {};
  for (const gift of gift_cards) {
    if (gift in remain) {
      remain[gift] += 1;
    } else {
      remain[gift] = 1;
    }
  }
  let result = wants.length;
  for (const w of wants) {
    if (w in remain) {
      remain[w] -= 1;
      result -= 1;
      if (remain[w] == 0) {
        delete remain[w];
      }
    }
  }
  return result;
}

let res = solution([1, 1, 4, 4, 5], [5, 5, 5, 4, 1]);
console.log(res);

// set , union, intersection
