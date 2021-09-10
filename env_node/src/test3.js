"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");
  console.log("inputString", inputString);
  main();
});

function readLine() {
  return inputString[currentLine++];
}
/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function diagonalDifference(arr) {
  // Write your code here
  let [a, b] = [0, 0];
  const matrixSize = arr.length;
  for (let i = 0; i < matrixSize; i++) {
    a += arr[i][i];
  }
  for (let i = 0; i < matrixSize; i++) {
    b += arr[i][matrixSize - 1 - i]; // 2 - 0 - 1
  }
  console.log("a,b", a, b);
  return a + b > 0 ? a + b : -(a + b);
}

function main() {
  const ws = fs.createWriteStream(
    process.platform === "linux" ? process.env.OUTPUT_PATH : "./test.txt"
  );
  const n = parseInt(readLine().trim(), 10);
  let arr = Array(n);

  for (let i = 0; i < n; i++) {
    arr[i] = readLine()
      .replace(/\s+$/g, "")
      .split(" ")
      .map((arrTemp) => parseInt(arrTemp, 10));
  }
  const result = diagonalDifference(arr);
  ws.write(result + "\n");
  ws.end();
}
