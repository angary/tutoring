import { isLeap, countLeaps, getSatisfactionResult } from './rescript';

describe('isLeap', () => {
  test.each([
    { year: 2299, expected: false },
    { year: 2304, expected: true },
    { year: 2300, expected: false },
    { year: 2400, expected: true },
    { year: 1, expected: false },
    { year: 4000000, expected: true },
  ])('isLeap($year) => $expected', ({ year, expected }) => {
    expect(isLeap(year)).toBe(expected);
  });
});

describe('countLeap', () => {
  test.each([
    { yearArray: [], expected: 0 },
    { yearArray: [4], expected: 1 },
    { yearArray: [1999], expected: 0 },
    { yearArray: [2000], expected: 1 },
    { yearArray: [1600, 1700, 1800, 1900], expected: 1 },
    { yearArray: [2299, 2304, 2300, 2400, 1, 400000], expected: 3 },
  ])('countLeaps($yearArray) has $expected leap year(s)', ({ yearArray, expected }) => {
    expect(countLeaps(yearArray)).toBe(expected);
  });
});

describe('Testing sortedSatisfaction', () => {
  test.each([
    {
      fastFoodRestaurant: {
        name: 'kfc',
        customerService: 1,
        foodVariety: 2,
        valueForMoney: 3,
        timeToMake: 4,
        taste: 5,
      },
      satisfactionResult: {
        restaurantName: 'kfc',
        satisfaction: 3,
      }
    },
    {
      fastFoodRestaurant: {
        name: 'mcdonalds',
        customerService: 3,
        foodVariety: 3,
        valueForMoney: 3,
        timeToMake: 4,
        taste: 4,
      },
      satisfactionResult: {
        restaurantName: 'mcdonalds',
        satisfaction: 3.4,
      }
    },
    {
      fastFoodRestaurant: {
        name: 'mrbeast burger',
        customerService: 100,
        foodVariety: 0,
        valueForMoney: 0,
        timeToMake: 0,
        taste: 0,
      },
      satisfactionResult: {
        restaurantName: 'mrbeast burger',
        satisfaction: 20,
      }
    },
  ])('$fastFoodRestaurant.name: $satisfactionResult.satisfaction', ({ fastFoodRestaurant, satisfactionResult }) => {
    expect(getSatisfactionResult(fastFoodRestaurant)).toStrictEqual(satisfactionResult);
  });
});
