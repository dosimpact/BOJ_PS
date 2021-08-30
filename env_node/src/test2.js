// ✅ 1. 생성자 함수 vs 클래스

const User = function (name, age) {
  this.name = name;
  this.age = age;
};

User.prototype.getName = function () {
  return `Name : ${this.name}(${this.age})`;
};

const mike = new User("mike", 23);
console.log(mike.getName());
// console.log(mike.getName.call(mike));
console.log(User.prototype.hasOwnProperty("getName"));
return;

class User2 {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  getName() {
    return `Name : ${this.name}(${this.age})`;
  }
}

const jain = new User2("jain", 30);
console.log(jain.getName());
// console.log(jain.getName.call(jain));

// 차이점 : class생성자는 new가 없다면 typeError,
// - 하지만 Function 생성자는 undefined 리턴

// 2 ✅ , for in 문은 프로토타입포함 프로퍼티 다 보여줌
// - hasOwnProperty을 사용해 객채만 가진 프로퍼티를 판별
// - 클래스함수는 for in문으로 보이지 않는다.
for (let p in mike) {
  console.log(p); // name age getName
}
for (let p in jain) {
  console.log(p); // name age
}
//  둘다 false가 나오게 된다.
console.log(mike.hasOwnProperty("getName")); // false
console.log(jain.hasOwnProperty("getName")); // false

// 3. ✅ 상속, 메소드 오버라이딩
class Car {
  constructor(name, color) {
    this.name = name;
    this.color = color;
  }
  drive() {
    console.log("DRIVE");
  }
  stop() {
    console.log("STOP");
  }
}
class BMW extends Car {
  // ✔ 생성자 오버라이딩
  constructor(name, color) {
    super(name, color);
  }
  park() {
    console.log("parking");
  }
  stop() {
    // ✔ 함수 오버라이딩, 부모의 stop이 override
    super.stop(); // 부모의 함수 호출
    console.log("OFF");
  }
}
const z4 = new BMW("z4", "blue");
console.log(z4.stop()); // STOP OFF
console.log(z4);
