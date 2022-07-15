import promptSync from 'prompt-sync';

const prod = (list: number[]) => list.reduce((accumulatingValue, currentNumber) => accumulatingValue * currentNumber, 1);

/**
 * Given an array of n integers, calculate the minimum, maximum, and the
 * product of the first n-1 numbers and last n-1 numbers.
 */
const drykiss = (myList: number[]): number[] => {
  const min = Math.min(...myList);
  const max = Math.max(...myList);
  // const prodHead = prod(myList.slice(0, myList.length - 2));
  const prodHead = prod(myList) / myList[myList.length - 1];
  const prodTail = prod(myList) / myList[0];
  return [min, max, prodHead, prodTail];
}

const prompt = promptSync();
const myList = [..."abcde"].map(char => parseInt(prompt(`Enter ${char}: `)));
const [min, max, prodFirst, prodLast] = drykiss(myList);
const prodLen = myList.length - 1;
console.log(`
  Minimum:
  ${min}
  Maximum:
  ${max}
  Product of first ${prodLen} numbers:
  ${prodFirst}
  Product of last ${prodLen} numbers:
  ${prodLast}
  `.trim().replace(/\n\s+/g, '\n')
);
