import { dayToYear } from './day-to-year';

describe('day to year tests', () => {
  test.each([
    { days: 1, year: 1970 }, // "January 1st 1970"
    { days: 365 + 1, year: 1971 }, // "January 1st 1971"
    { days: 365 + 365 + 1, year: 1972 }, // "January 1st 1972"
    { days: 365 + 365 + 366 + 1, year: 1973 }, // "January 1st 1973"

    // Catch bug
    { days: 365 + 365 + 366, year: 1972 }, // "December 31st 1972"

  ])('dayToYear($days) => $year', ({ days, year }) => {
    expect(dayToYear(days)).toEqual(year);
  });
});
