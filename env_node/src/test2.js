function getPosMinIdx(arr) {
  let idx = 0;
  let now = -1;
  for (let [a, i] of arr.entries()) {
    if (a <= 0) continue;
    if (now === -1) {
      now = a;
      idx = i;
      continue;
    }
    if (a < now) {
      idx = i;
      now = a;
      continue;
    }
  }
  return idx;
}

function checkFin(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] !== arr[i + 1]) return false;
  }
  return true;
}

function solution(arr) {
  let ans = 0;
  while (!checkFin(arr)) {
    console.log("arr", arr, "ans cycle", ans);
    // const idx = getPosMinIdx(arr);
    // const minVal = arr[idx];
    const minVal = Math.min(...arr.filter((e) => e > 0));
    const idx = arr.indexOf(minVal);
    console.log(`minVal ${minVal}로 ${idx} 기준 감소 <-->`);
    for (let i = idx; i >= 0; i--) {
      if (arr[i] >= minVal) {
        arr[i] -= minVal;
      } else {
        break;
      }
    }
    for (let i = idx + 1; i < arr.length; i++) {
      if (arr[i] >= minVal) {
        arr[i] -= minVal;
      } else {
        break;
      }
    }
    ans += 1;
  }

  return ans;
}
console.log(solution([1, 2, 4, 8, 4, 2, 1]));
