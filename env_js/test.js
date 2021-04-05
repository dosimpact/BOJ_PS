// const tobj = {
//   2: new Set([1]),
//   4: new Set([1, 2, 3]),
// };

// for (let e in tobj) {
//   console.log(e);
// }

const q = [1, 2, 3];

while (q.length !== 0) {
  const now = q.pop(0);
  console.log(now);
}
console.log(q);
q.push(1);
console.log(q);
while (q.length !== 0) {
  console.log(q[0]);
  q.splice(0, 1);
}
