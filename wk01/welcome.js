/**
 * A simple program to print a welcome message
 * and print 10 numbers with information about
 * whether they are odd or even.
 */

// We use `const` to declare constants
const SIZE = 10;

// We use `let` to declare variables
let message = "Welcome to COMP1531";

// We use `console.log()` to print stuff to the terminal
console.log(message);

// Use back ticks and s`${}` to print out variables
console.log(`Numbers from 1 to ${SIZE}`);

// For loop and if else is the same as C
for (let num = 0; num <= SIZE; num++) {
  if (num % 2 == 0) {
    console.log(`EVEN: ${num}`);
  } else {
    console.log(`ODD: ${num}`);
  }
}
