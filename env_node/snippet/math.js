// eg) sum array
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);

// eg)  average array
const avg = (...arr) =>
  [...arr].reduce((acc, val) => acc + val, 0) / arr.length;

// eg) product array
const product = (...arr) => [...arr].reduce((acc, val) => acc * val, 1);
