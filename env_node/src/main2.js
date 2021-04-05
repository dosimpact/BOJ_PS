// 로봇을 이용하여 여러 종류의 완제품 만들자.
//로봇 하나는 한 부품만 처리
// 완제품은 여러 부품  필요
// 로봇 r대로 최대한 다양한 완제품 만들려함

function combination(arr, selectNum) {
  const result = [];
  if (selectNum === 1) return arr.map((v) => [v]);
  arr.forEach((v, idx, arr) => {
    const fixed = v;
    const restArr = arr.slice(idx + 1);
    const combinationArr = combination(restArr, selectNum - 1);
    const combineFix = combinationArr.map((v) => [fixed, ...v]);
    result.push(...combineFix);
  });
  return result;
}

function solution(needs, r) {
  const N = needs.length;
  const M = needs[0].length;
  const machin = {};
  // 각 기계별  필요한 부품 파싱
  for (let [i, row] of needs.entries()) {
    machin[i] = new Set();
    for (let [j, e] of row.entries()) {
      if (e == 1) {
        machin[i].add(j);
      }
    }
  }
  // console.log(machin);
  // 콤비네이션 후 갯수
  const combiList = combination([...Array(M).keys()], r);
  let ansList = [];
  // console.log(combiList);
  for (let combi of combiList) {
    let ansTmp = 0;
    for (let key in machin) {
      const a = new Set(combi);
      const b = new Set([...machin[key]]);
      const intersection = new Set([...b].filter((x) => a.has(x)));
      // console.log(combi, machin[key], intersection);
      if (intersection.size == machin[key].size) {
        ansTmp += 1;
      }
    }
    ansList = [...ansList, ansTmp];
  }
  // console.log(ansList);
  // 최대값 리턴
  return Math.max(...ansList);
}

let res = solution(
  [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1],
  ],
  2
);
console.log(res);

// set , union, intersection
// 조합 직접 구현
