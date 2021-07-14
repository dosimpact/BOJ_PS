// 로또 6/45
// 일부 번호 변수(0표기) - 최저,최고 순위

// 맞은 경우, 틀린경우, 모르는 경우
// 맞은 수를 -> 등수로 변환

function solution(lottos, win_nums) {
  const answer = [];
  // 일치 하는 숫자
  const unkown = lottos.filter((e) => e === 0).length;
  // 미지수,
  let baseCorret = lottos.filter((e) => e !== 0 && win_nums.includes(e)).length;
  console.log(baseCorret);
  // 1개만 맞는 경우 예외
  const toRank = (e) => {
    if (2 <= e && e <= 6) return 7 - e;
    else {
      return 6;
    }
  };
  return [toRank(baseCorret + unkown), toRank(baseCorret)];
}
s = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]);
