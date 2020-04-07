var a = 0;

(function () {
  this.a = 1;
  this.b = 2;
  console.log(a);
})();

console.log(a);
console.log(b);
