import { drawX } from './x';

describe('even size error', () => {
  for (let size = 0; size < 10; size += 2) {
    test(`size = ${size}`, () => {
      expect(drawX(size)).toEqual('error');
    });
  }
});

describe('odd cases', () => {
  test.each([
    { size: 1, expected: 'x' },
    { size: 3, expected: 'x x\n x\nx x' },
    { size: 5, expected: 'x   x\n x x\n  x\n x x\nx   x' },
    { size: 7, expected: 'x     x\n x   x\n  x x\n   x\n  x x\n x   x\nx     x' },
    { size: 9, expected: 'x       x\n x     x\n  x   x\n   x x\n    x\n   x x\n  x   x\n x     x\nx       x' },
  ])('testing drawX($size)', ({ size, expected }) => {
    expect(drawX(size)).toEqual(expected);
  });
});
