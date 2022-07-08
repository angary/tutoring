import promptSync from 'prompt-sync';
import { findVowels } from './vowels';

const prompt = promptSync();

let input: string;
while ((input = prompt('Enter message: '))) {
  console.log('FIXME', input);
}
