// 상품번호가 적힌 상품권, 교환가능
// 원치않은 상품 받는것 최소로

function solution(gift_cards, wants) {
  let a = new Set(gift_cards);
  let b = new Set(wants);
  let intersection = new Set([...b].filter((x) => a.has(x)));
  return wants.length - intersection.size;
}

let res = solution([1, 1, 4, 4, 5], [5, 5, 5, 4, 1]);
console.log(res);

// set , union, intersection
