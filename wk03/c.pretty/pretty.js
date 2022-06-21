export function pretty(inputString) {
  let hours = parseInt(inputString.slice(0, 2));
  let timePeriod = 'am';
  if (hours === 0) {
    // for 0000 => 12:00 am
    hours = 12;
  } else if (hours >= 12) {
    timePeriod = 'pm';
    if (hours > 12) {
      hours -= 12;
    }
  }

  const minutes = inputString.slice(2);
  const padHours = String(hours).padStart(2, 0);
  return `${padHours}:${minutes} ${timePeriod}`;
}

/*
// Alternative Solution
// $ npm i date-fns

// https://date-fns.org/docs/format
import { format } from 'date-fns';

export function pretty(inputString) {
  const date = new Date();
  date.setHours(parseInt(inputString.slice(0, 2)));
  date.setMinutes(parseInt(inputString.slice(2)));
  return format(date, 'hh:mm aaa');
}
*/
