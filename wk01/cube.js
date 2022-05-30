/**
 * A comparison of arrow functions vs traditional functions.
 * The first function uses traditional function declaration,
 * whilst the second one uses arrow expressions.
 */

/**
 * @param {number} x the number to cube
 * @returns the cubed number
 */
function cube1(x) {
  return x ** 3;
}

/**
 * @param {number} x the number to cube
 * @returns the cubed number
 */
const cube2 = (x) => {
  return x ** 3;
};

const number = 5;
const result = cube2(number);
console.log(`${number}^3 = ${result}`);
