/*
 * `codeOwnersMap`과 `directory`를 입력받아
 * `directory`의 코드 주인 목록을 반환하는 함수를 작성하세요.
 */
function refObjDot(key, obj) {
  if (String(key).includes(".")) {
    const head = String(key).slice(0, key.indexOf("."));
    const tail = String(key).slice(key.indexOf(".") + 1);
    return refObjDot(tail, obj[head]);
  } else {
    return obj[key];
  }
}
function solution(codeOwnersMap, directory) {
  const parsing = String(directory).split("/");
  return refObjDot(`${parsing.join(".")}`, codeOwnersMap);
  // return codeOwnersMap[`${parsing.join(".")}`];
}

const codeOwnersMap = {
  scripts: ["배수진"],
  services: {
    "business-ledger": ["고찬균", "배수진"],
    "toss-card": ["채주민", "유재섭"],
    payments: ["유재섭"],
  },
};
console.log(solution(codeOwnersMap, "scripts"));
console.log(solution(codeOwnersMap, "services/toss-card"));
