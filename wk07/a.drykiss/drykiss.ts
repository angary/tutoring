import promptSync from 'prompt-sync';

/**
 * Given an array of n integers, calculate the minimum, maximum, and the
 * product of the first n-1 numbers and last n-1 numbers.
 */
const drykiss = (myList: number[]): number[] => {
  let myMin = Infinity;
  for (let i = 0; i < myList.length; i++) {
    if (myList[i] < myMin) {
      myMin = myList[i];
    }
  }

  let myMax = -Infinity;
  for (let i = 0; i < myList.length; i++) {
    if (myList[i] > myMax) {
      myMax = myList[i];
    }
  }

  let prod = 1;
  for (let i = 0; i < 4; i++) {
    prod = prod * myList[i];
  }
  const prodHead = prod;

  prod = 1;
  for (let i = 1; i < 5; i++) {
    prod = prod * myList[i];
  }

  const result = [myMin, myMax, prodHead, prod];
  return result;
}

const prompt = promptSync();
const a = parseInt(prompt('Enter a: '));
const b = parseInt(prompt('Enter b: '));
const c = parseInt(prompt('Enter c: '));
const d = parseInt(prompt('Enter d: '));
const e = parseInt(prompt('Enter e: '));
const myList = [a, b, c, d, e];
const result = drykiss(myList);
console.log('Minimum:');
console.log(`${result[0]}`);
console.log('Maximum:');
console.log(`${result[1]}`);
console.log('Product of first 4 numbers:');
console.log(`${result[2]}`);
console.log('Product of last 4 numbers');
console.log(`${result[3]}`);
