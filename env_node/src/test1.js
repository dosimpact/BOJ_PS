// 변수명 = 숫자
// print 변수명 , error 출력
// *동일 이름 여러개 출력 가능
// *블록이라는 개념, 가장 나중에 생성된 변수 출력
const res = new Array();
const scope = new Array(30).fill(0).map((e) => new Object());
function printCode(lastStr, dotCount) {
  // .의 갯수 이하부터 돌면서 변수를 출력하려함, 없으면 애러
  const key = lastStr.split(" ")[1];
  for (let i = dotCount; i >= 0; i--) {
    if (key in scope[i]) {
      res.push(`${key}=${scope[i][key]}`);
      return;
    }
  }
  res.push("error");
  return;
}

function solution(codes) {
  for (let code of codes) {
    // .. 이 갯수 찾기
    const lastDotIdx = String(code).lastIndexOf(".");
    const dotCount = lastDotIdx + 1;
    const lastStr = String(code).slice(dotCount);
    if (lastStr.includes("print")) {
      printCode(lastStr, dotCount);
    } else {
      // 변수를 해당 블록 레벨에 추가
      const [key, value] = lastStr.split("=");
      scope[dotCount] = {
        ...scope[dotCount],
        [key]: value,
      };
    }
  }
  return res;
}

// console.log(
//   solution([
//     "a=3",
//     "..a=4",
//     "..b=3",
//     "..print a",
//     ".......a=6",
//     ".......print a",
//     ".......print b",
//     "..print a",
//     "....a=7",
//     "....print a",
//     "print a",
//     "print b",
//     "a=4",
//     "print a",
//     "...print a",
//   ])
// );

console.log(
  solution([
    "x=3",
    "x=4",
    "z=5",
    "..x=99",
    "..y=98",
    "..z=97",
    ".print x",
    ".print y",
    ".print z",
    "...print x",
    "...print y",
    "...print z",
    ".......a=6",
    ".......print a",
    ".......print b",
  ])
);
("use strict");

// ✅ Activity라는 부모 클래스 생성
// - Activity 프로퍼티
function Activity(amount) {
  this.amount = amount; // public 프로퍼티
}

// - Activity 메서드
// amount 에 대한 setter,setter
Activity.prototype.setAmount = function (amount) {
  if (amount <= 0) return false;
  this.amount = amount;
  return true;
};

Activity.prototype.getAmount = function () {
  return this.amount;
};
// --------------------------
// ✅ Payment라는 자식 클래스 1 생성
// - Payment 프로퍼티
function Payment(amount, receiver) {
  Activity.call(this, amount); // super
  this.receiver = receiver; //
}
// - Payment 상속
Payment.prototype = Object.create(Activity.prototype); // extends
Payment.prototype.constructor = Activity; // ?

// - Payment 메서드
Payment.prototype.setReceiver = function (receiver) {
  this.receiver = receiver;
};
Payment.prototype.getReceiver = function () {
  return this.receiver;
};
// -------------
function Refund(amount, sender) {
  Activity.call(this, amount);
  this.sender = sender;
}
Refund.prototype = Object.create(Activity.prototype);
Refund.prototype.constructor = Activity;

Refund.prototype.setSender = function (sender) {
  this.sender = sender;
};
Refund.prototype.getSender = function () {
  return this.sender;
};

// ✅ activity와 Activity.prototype의 프로퍼티 확인
const activity = new Activity(500);
console.log(activity); // Activity { amount: 500 }
console.log(activity.getAmount()); // 500
console.log(Activity.prototype.hasOwnProperty("setAmount")); // true
console.log(Activity.prototype.hasOwnProperty("getAmount")); // true
// Activity.prototype 에는 자식에서 만든 메서드가 없는 것이 당연
console.log(Activity.prototype.hasOwnProperty("setSender")); // false
console.log(Activity.prototype.hasOwnProperty("getSender")); // false

// ✅ refund와 Refund.prototype의 프로퍼티 확인
const refund = new Refund(1000, "john");
console.log(refund); // Activity { amount: 1000, sender: 'john' }
console.log(refund.getAmount()); // 1000
//
console.log(Refund.prototype.hasOwnProperty("setAmount")); // false
console.log(Refund.prototype.hasOwnProperty("getAmount")); // false
// Refund.prototype 에 정의된 메서드 이다.
console.log(Refund.prototype.hasOwnProperty("setSender")); // true
console.log(Refund.prototype.hasOwnProperty("getSender")); // true

// ✅ refund의 프로퍼티 확인
// refund
// refund.__proto__
// refund.__proto__.__proto__

// refund를 만들어낸 프로토 타입에는  setSender 있음 ( static method )
console.log(refund.__proto__.hasOwnProperty("setSender")); // true
// 하지만 분명히 setAmount을 쓸 수 있는데, 본인이 가진 프로퍼티는 아님
console.log(refund.__proto__.hasOwnProperty("setAmount")); // false
// 한단계 올라가서 있음
console.log(refund.__proto__.__proto__.hasOwnProperty("setAmount")); //true
