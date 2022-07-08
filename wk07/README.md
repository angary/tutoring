# Tutorial 7

[TOC]

## A. DRY & KISS

The code in [a.drykiss](a.drykiss/drykiss.ts) is unnecessarily complicated, and there is a lot of repetition. Take some time to refactor this code focusing on DRY and KISS principles to create a concise and easily-understood code.

<details close>

<summary>click to view</summary>

```ts
import promptSync from 'prompt-sync';

/**
 * Given an array of n integers, caclulate the minimum, maximum, and the
 * product of the first n-1 numbers and last n-1 numbers.
 */
function drykiss(myList: number[]) {
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
```

</details>

## B. Finding Vowels

Below is the interface for the function findVowels:

<table>
  <tr>
    <th>Name & Description</th>
    <th>Parameters</th>
    <th>Return Object</th>
    <th>Errors</th>
  </tr>
  <tr>
    <td>
      <code>findVowels</code>
      <br/><br/>
      Return the count of all vowels in the given message. For example, for the string 'helloworld':
      <br/>
      <code>{ a: 0, e: 1, i: 0, o: 2, u: 0 }</code>.
    </td>
    <td>
      (message: string)
    </td>
    <td>
<pre>{
  a: number,
  e: number,
  i: number,
  o: number,
  u: number
}</pre>
    </td>
    <td>
      Throw <code>Error</code> when
      <ul>
        <li>The message contains characters that are not lower-case letters or spaces</li>
      </ul>
    </td>
  </tr>
</table>

1. In [b.vowels/vowels.test.ts](b.vowels/vowels.test.ts), write a suite of tests that cover both the error cases and success cases for the `findVowels`.
    
1. Complete the implementation of `findVowels` in [b.vowels/vowels.ts](b.vowels/vowels.ts). Ensure that they pass your tests.

1. In [b.vowels/main.ts](b.vowels/main.ts), write a program that reads in messages one at a time and prints out the result of `findVowels`. The program should also `try`/`catch` any errors that are thrown.

## C. Creating Routes

1. Your tutor will break up into random groups for this activity. Take a look at [this webpage](https://www.youtube.com/watch?v=GfL5zOhpB14). What routes do you think are necessary to allow this webpage to function? For each route:
    - Discuss the data it might take in
    - Discuss the data it might return

    ~~Your tutor may provide you with a [hackmd.io](https://hackmd.io) file for everyone to edit together.~~

    Google doc link: [here](https://docs.google.com/document/d/1oKyf1YE5-IdgW6hXystcHJ39K7IEXSck6Xc8EYyu-vM/edit?usp=sharing).

1. Are there any considerations that need to be made when choosing how to break up routes?
