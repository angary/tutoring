import promptSync from 'prompt-sync';
import { pretty } from './pretty.js';

const prompt = promptSync();

let dateString = prompt('Enter time: ');
while (dateString !== null) {
  console.log(pretty(dateString));
  dateString = prompt('Enter time: ');
}

/*
// Alternative shorter solution
// (note the double parentheses inside while loop)

let dateString;
while ((dateString = prompt('Enter time: '))) {
  console.log(pretty(dateString));
}
*/
