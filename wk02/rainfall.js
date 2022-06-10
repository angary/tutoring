/**
 * Compute the average of only the positive
 * elements in the integer array.
 * Return null if there are no positive integers.
 */
const rainfall = (integers) => {
  const positives = [];
  let sum = 0;
  for (const integer of integers) {
    if (integer > 0) {
      positives.push(integer);
      sum += integer;
    }
  }
  if (positives.length === 0) {
    return null;
  }
  return sum / positives.length;
};

/**
 * An alternative method of implementing rainfall using `filter` and `reduce`
 * which is functions used in "functional programming".
 *
 * NOTE: You do not need to understand this until week 4.
 */
const rainfallFunctionalProgramming = (integers) => {
  const positives = integers.filter((x) => x > 0);
  if (positives.length === 0) {
    return null;
  }
  const sum = positives.reduce((acc, x) => acc + x, 0);
  return sum / positives.length;
};
