import { pretty } from './pretty.js';

// basic test
test('pretty(0000) => 12:00 am', () => {
  expect(pretty('0000')).toEqual('12:00 am');
});

// Can use describe to group similar test
describe('pretty', () => {
  // Can use test.each for tests with identical structure
  // but different input/output
  test.each([
    { input: '0030', expected: '12:30 am' },
    { input: '0100', expected: '01:00 am' },
    { input: '0730', expected: '07:30 am' },
    { input: '1159', expected: '11:59 am' },
    { input: '1200', expected: '12:00 pm' },
    { input: '1930', expected: '07:30 pm' },
    { input: '2359', expected: '11:59 pm' },
  ])("pretty('$input') => '$expected'", ({ input, expected }) => {
    expect(pretty(input)).toEqual(expected);
  });
});
