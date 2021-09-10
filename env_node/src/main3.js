function parseSearch() {
  let search = "?from=twitter&range=1&range=8";
  /* 쿼리 문자열 `search`를 파싱하는 함수를 작성해주세요. */
  if (search === "") return {};
  search = search.slice(1);
  const result = {};
  const token = search.split("&");
  token.map((t) => {
    const [key, value] = t.split("=");
    if (key in result) {
      result[key].push(value);
    } else {
      result[key] = [value];
    }
  });
  for (let key in result) {
    if (result[key].length === 1) {
      result[key] = result[key][0];
    }
  }
  return result;
}
console.log(parseSearch());
/*
 * NOTE: 아래 코드는 코드 동작을 확인하기 위한 코드입니다. 수정하지 말아주세요.
 */
function solution(search) {
  var query = parseSearch(search);
  return submit(query);
}

function submit(answer) {
  return JSON.stringify(answer);
}
