const arr1 = [1, 10, 20];
console.log(arr1);
const arr2 = arr1.map((e) => e);
console.log(arr2);

arr1.push(77);

console.log(arr1);
console.log(arr2);
