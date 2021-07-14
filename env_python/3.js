const makeReg = (str, cnt) => {
  return str.split("").join("[a-z]".repeat(cnt));
};

function solution(line1, line2) {
  let ans = 0;
  let Reg;
  for (let i = 0; i <= line1.length; i++) {
    const regLen = line2.split("").join("*".repeat(i)).length;
    if (regLen > line1.length) break;

    let target = line1;
    Reg = new RegExp(makeReg(line2, i), "g");
    let spoint = 0;
    while (Reg.test(target)) {
      ans += 1;
      spoint = target.search(Reg);
      if (spoint + 1 >= target.length) break;
      target = target.slice(spoint + 1);
      Reg.test(target);
    }
  }
  return ans;
}
// console.log(solution("abbbcbbb", "bbb"));
console.log(solution("abcabcabc", "abc"));
// console.log(solution("abacaba", "bbb"));
// console.log("abbbcbbb".match(/b[a-z]b[a-z]b/gi));
// console.log("abbbcbbb".search(/b[a-z]b[a-z]b/gi));
// console.log("abbbcbbb".slice(1));
// console.log(/bbb/g.test("bbcbbb "));

//⚠ if 안에도 클로져인듯..
