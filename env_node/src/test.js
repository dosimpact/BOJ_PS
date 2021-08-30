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
