// From lab01_leap solution
function isLeap(year: number): boolean {
  if (year % 4 !== 0) {
    return false;
  } else if (year % 100 !== 0) {
    return true;
  } else if (year % 400 !== 0) {
    return false;
  }
  return true;
}

// From lab01_leap solution
function countLeaps(yearArray: number[]): number {
  let count = 0;
  for (const year of yearArray) {
    if (isLeap(year)) {
      count++;
    }
  }
  return count;
}

interface FastFoodRestaurant {
  name: string;
  customerService: number;
  foodVariety: number;
  valueForMoney: number;
  timeToMake: number;
  taste: number;
}

interface SatisfactionResult {
  restaurantName: string;
  satisfaction: number;
}

// Spin-off from lab02_satisfaction
function getSatisfactionResult(
  fastFoodRestaurant: FastFoodRestaurant
): SatisfactionResult {
  const sum =
    fastFoodRestaurant.customerService +
    fastFoodRestaurant.foodVariety +
    fastFoodRestaurant.valueForMoney +
    fastFoodRestaurant.timeToMake +
    fastFoodRestaurant.taste;
  return {
    restaurantName: fastFoodRestaurant.name,
    satisfaction: sum / 5,
  };
}

export { isLeap, countLeaps, getSatisfactionResult };
// Invalid arguments supplied to functions
// console.log(isLeap('What happens if we pass in a string?'));
// console.log(isLeap());
// console.log(countLeaps([1,2,3,4], 'extra argument'));
// console.log(getSatisfactionResult({ invalid: 'object' }));
