const ORIGIN_YEAR = 1970;

const isLeap = (y: number) => new Date(y, 1, 29).getDate() === 29;

export const dayToYear = (days) => {
  let year = ORIGIN_YEAR;
  while (days > 365) {
    if (isLeap(year)) {
      if (days > 366) {
        days -= 366;
        year += 1;
      } else {
        // Catches Bug
        break;
      }
    } else {
      days -= 365;
      year += 1;
    }
  }
  return year;
};
