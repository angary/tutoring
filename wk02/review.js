/*
1. What does it do?

2. What style could be improved here?

3. How can we modify the code to be less like 'C' and more 'Javascripty'?

*/

let x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result = [];
for (let i = 0; i < x.length; i++) {
  if (x[i] % 2 === 0) {
    result.push(x[i] * 2);
  } else {
    result.push(x[i]);
  }
}
console.log(result);
