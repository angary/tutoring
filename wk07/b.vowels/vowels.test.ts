import { findVowels } from './vowels';

describe('Error', () => {
  test.each([
    '!',
    '1',
    'A',
    'lowerUPPER',
    '_',
  ])("findVowels('%s') => Error!", (message) => {
    expect(() => findVowels(message)).toThrow(Error);
  });
});

describe('Success', () => {
  test.each([
    { message: '', expected: { a: 0, e: 0, i: 0, o: 0, u: 0 } },
    { message: 'a', expected: { a: 1, e: 0, i: 0, o: 0, u: 0 } },
    { message: 'aeiou', expected: { a: 1, e: 1, i: 1, o: 1, u: 1 } },
    { message: 'consonants and vowels', expected: { a: 2, e: 1, i: 0, o: 3, u: 0 } },
    { message: 'uwu      ewe      owo', expected: { a: 0, e: 2, i: 0, o: 2, u: 2 } },
  ])("findVowels('$message') => $expected", ({ message, expected }) => {
    expect(findVowels(message)).toStrictEqual(expected);
  });
});
