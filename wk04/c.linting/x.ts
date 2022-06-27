export function drawX(size: number) {
  if (size % 2 === 0) {
    return 'error';
  }
  let result = '';
  for (let row = 0; row < size; row++) {
    for (let col = 0; col < size; col++) {
      if (col === row || col === size - row - 1) {
        result += 'x';
      } else {
        result += ' ';
      }
    }
    result = result.trim() + '\n';
  }
  return result.slice(0, -1);
}
