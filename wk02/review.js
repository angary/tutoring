const integerArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const result = [];

for (const num of integerArray) {
  // if (num % 2 === 0) {
  //   result.push(num * 2);
  // } else {
  //   result.push(num);
  // }

  // Ternary operator (one line if ... else statement)
  const value = num % 2 === 0 ? num * 2 : num;
  result.push(value);
}
console.log(result);

/**
 * An alternative method using `map`
 * which is a function used in "functional programming".
 *
 * NOTE: You do not need to understand this until week 4.
 */
const resultFunctionalProgramming = integerArray.map((x) =>
  x % 2 === 0 ? x * 2 : x
);
console.log(resultFunctionalProgramming);
