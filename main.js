const fs = require("fs");
let [a, b] = fs.readFileSync("/dev/stdin").toString().split(" ");
console.log(+a + +b);
