// eg) sum array
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);

// eg)  average array
const avg = (...arr) =>
  [...arr].reduce((acc, val) => acc + val, 0) / arr.length;

// eg) product array
const product = (...arr) => [...arr].reduce((acc, val) => acc * val, 1);

// eg) matrix sum 2Darray
//  row 에서 map 을 iterate -> i
//  col 에서 map 을 iterate -> j -> B[i][j] 를 더한다.
const matrixSum = (A, B) =>
  A.map((row, i) => row.map((col_e, j) => col_e + B[i][j]));
