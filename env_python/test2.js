// 캡슐화 - 자유변수 이용
function Rectangle(width, height) {
  // pulbic variable
  this.width = width;
  this.height = height;

  // private varibale
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
    return `${this.width} ${this.height} ${this.color}`;
  };
}

Rectangle.prototype.getArea = function () {
  return this.getWidth() * this.getHeight();
};
Rectangle.prototype.getInfo = function () {
  return `${this.width} ${this.height} ${this.color}`;
};

var rect1 = new Rectangle(10, 15);
console.log(rect1.printInfo()); //10 15 undefined
console.log(rect1.getInfo()); // 10 15 undefined

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
