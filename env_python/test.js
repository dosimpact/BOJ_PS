function makeStudent(name, kor, eng, math) {
  var student = {
    name,
    kor,
    eng,
    math,
    getSum: function () {
      return this.kor + this.eng + this.math;
    },
    getAvg: function () {
      return this.getSum() / 3;
    },
  };
  return student; // 객체를 리턴
}
st1 = makeStudent('test', 20, 45, 50);
console.log('st1 ', st1);

function Student(name, kor, eng, math) {
  this.name = name;
  this.kor = kor;
  this.eng = eng;
  this.math = math;
}
Student.prototype.getSum = function () {
  return this.kor + this.eng + this.math;
};
Student.prototype.getAvg = function () {
  return this.getSum() / 3;
};

st2 = new Student('test2', 25, 70, 20);
console.log('st2 ', st2, st2.getSum(), st2.getAvg());
// Student('test3',125,170,120) // this가 window가 되지 않도록 !!

// 캡슐화 - 자유변수 이용
function Rectangle(width, height) {
  // pulbic variable
  this.width = width;
  this.height = height;

  // private varibale
  // 캡술화 = 숨겨두는것
  var color = 'RED';

  this.getWidth = function () {
    return width;
  };
  this.getHeight = function () {
    return height;
  };

  this.setWidth = function (w) {
    width = w;
  };
  this.setHeight = function (h) {
    height = h;
  };

  this.getColor = function () {
    return this.color;
  };
  this.setColor = function (c) {
    color = c;
  };

  this.printInfo = function () {
    return `${(width, height, color)}`;
  };
}

Rectangle.prototype.getArea = function () {
  return this.getWidth() * this.getHeight();
};
Rectangle.prototype.getInfo = function () {
  return `${(this.width, this.height, this.color)}`;
};

var rect1 = new Rectangle(10, 15);
console.log(rect1.printInfo());

rect1.width = 88;
rect1.height = 9;
console.log(rect1.printInfo());

rect1.color = 'PINK';
console.log(rect1.printInfo());

rect1.setWidth(88);
rect1.setHeight(10);
console.log(rect1.printInfo());

rect1.setColor('BLUE');
console.log(rect1.printInfo());

// console.log(rect1, rect1.getArea());
// // 진짜 w,h는 볼 수 없다.
// rect1.width = 88;
// rect1.height = 9;
// console.log(rect1, rect1.getArea());

// // 정말인가 ? 아래 추가한 realWidth랑 캡슐화된 realWidth는 다르다.
// rect1.realWidth = 88;
// rect1.realHeight = 9;
// console.log(rect1, rect1.getArea());

// // setter을 통해 캡슐화된 realWidth에 접근 가능
// rect1.setWidth(88);
// rect1.setHeight(10);
// console.log(rect1, rect1.getArea());
