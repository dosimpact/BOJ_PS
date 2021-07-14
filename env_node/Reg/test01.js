// 정규식
// 1) 정규식을 통과 하냐 못하냐 -> true,false
// 2) 통과한 부분을 다른 문자열로 replace 가능

`
replace
match
search
split
`;

// eg) we 라는 단어 (대소 구분 없이 찾기)
(() => {
  const RegExp = /we/gi; // 대소 구분없이, 전체 찾기
  console.log(RegExp.test("Hello We will, we will rock you")); // true
  console.log(RegExp.exec("Hello We will, we will rock you")); // ['we',index:,input:,groups:]
  console.log("Hello We will, we will rock you".replace(RegExp, "you")); // Hello you will, you will rock you
  console.log("Hello We will, we will rock you".match(RegExp) || []); // [ 'We', 'we' ]
  console.log("Hello We will, we will rock you".search(RegExp)); //  6
  console.log("Hello We will, we will rock you".split(RegExp)); // [ 'Hello ', ' will, ', ' will rock you' ]
})();

console.log("-------------------------------------");
// eg) match - global options
// match 의 결과 array가 된다.
// match 결과가 없으면 null이 되기떄문에 []을 사용해야 한다.
(() => {
  let str = "We will, we will rock you";
  console.log(str.match(/we/gi) || []); // [ 'We', 'we' ]
})();

console.log("-------------------------------------");
// eg) match - global not options
// match 의 결과가 indexable array 가 된다.

(() => {
  let str = "We will, we will rock you";

  let result = str.match(/we/i); // 플래그 g 없음
  console.log(result); // ['We',index,input,groups]
  console.log(result[0]); // We (패턴에 일치하는 첫 번째 부분 문자열)
  console.log(result.length); // 1
  // Details:
  console.log(result.index); // 0 (부분 문자열의 위치)
  console.log(result.input); // We will, we will rock you (원본 문자열)
})();

console.log("-------------------------------------");
// eg) replace
(() => {
  // 플래그 g 없음
  console.log("We will, we will".replace(/we/i, "I")); // I will, we will
  // 플래그 g 있음
  console.log("We will, we will".replace(/we/gi, "I")); // I will, I will
})();

console.log("-------------------------------------");

// eg) replace 특수 문자 사용 가능
// $& : 패턴과 일치하는 부분 문자열
(() => {
  console.log("I love HTML".replace(/HTML/, "$& and JavaScript and $&"));
  // I love HTML and JavaScript and HTML
})();

console.log("-------------------------------------");
// eg) 숫자 체크
// 정규식상, 여러번 중첩되어 일치한다.
const test01 = () => {
  const tel = "01012345678"; // 정규 표현식 리터럴
  const myRegExp = /\d(?=\d{4})/g;
  console.log(myRegExp.test(tel)); // true
  console.log(tel.replace(myRegExp, "*")); // *******5678
  console.log(tel.match(myRegExp, "*")); /*['0', '1', '0','1', '2', '3','4'] */
};
// test01();
console.log("-------------------------------------");
