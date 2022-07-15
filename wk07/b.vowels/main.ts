import promptSync from 'prompt-sync';
import { findVowels } from './vowels';

const prompt = promptSync();

let input: string;
while ((input = prompt('Enter message: '))) {
  try {
    console.log(findVowels(input));
  } catch (e) {
    console.log(`Caught Error from findVowels: '${e.message}'.`);
  }
}
