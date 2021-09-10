// 0~9 버튼 숫자
function solution(passwords, s) {
  // psswords 을 2차원 배열로 파싱한다.
  const db = {};
  for (let pair of passwords) {
    db[pair[0]] = pair[1];
  }
  let step = 1; //1 호수 , 2비번
  let inputPassword = "";
  let ans = 0;
  const pass = String(s).split("#").slice(0, -1);

  for (let p of pass) {
    if (step === 1) {
      if (p in db) {
        inputPassword = db[p];
        step = 2;
      }
    } else if (step === 2) {
      if (String(inputPassword) === String(p)) {
        ans += 1;
      }
      step = 1;
    }
  }
  // s를 split하여 읽으면서 password을 점검
  return ans;
}

console.log(
  solution(
    [
      [101, 101],
      [102, 102],
      [201, 101],
      [202, 101],
    ],
    "101#101#102#101#203#101#201#101#101#"
  )
);
// ✅ 1.  add,delete,has,size,clear
const mySet = new Set(); // {}
mySet.add(1); // {1}
console.log(mySet.add(2)); //{1,2}
console.log(mySet); //{1,2}
console.log(mySet.size); // 2
mySet.delete(1); //{2}
mySet.has(2); //true
mySet.has(1); //false
mySet.clear(); // {}

// ✅ 2. eg) set 순회
// set은 iterable 객체가 있다. => of 가능
// keys,values,entries, ...
mySet.add(10);
mySet.add(10);
mySet.add("10");

for (let s of mySet) {
  console.log("of : ", s); // of :  10 , of :  10
}

for (let [i, s] of mySet.entries()) {
  // entries of 10 : 10, entries of 10 : 10
  console.log(`entries of ${i} : ${s}`);
}
console.log(mySet.keys()); // [Set Iterator] { 10, '10' }
console.log(mySet.values()); //[Set Iterator] { 10, '10' }

// ✅ 3. eg) set -> Array
let arr = [...mySet]; //Spread 연산자를 이용해 array로 만들 수 있다.
console.log(arr); // [ 10, '10' ]

// ✅ 4. eg) 중복 제거
//array중복제거 하고싶으면 Set바꿨다 arr 하면 쉽게 해결
const unique = (...arr) => [...new Set(arr)];
console.log(unique(...[1, 2, 2, 3])); //[ 1, 2, 3 ]
console.log(unique(1, 2, 2, 3)); //[ 1, 2, 3 ]
