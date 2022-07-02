interface NumberFunction {
  (n: number): number;
}

// We can assign functions to variables
const double: NumberFunction = function (n: number) {
  return n * 2;
};

/*
// OR
const double2: NumberFunction = (n) => {
  return n * 2;
};

// OR
const double3: NumberFunction = (n: number) => n * 2;
*/

console.log(double(30));

// We can also pass a function as an argument to another function
const apply = (func: NumberFunction, array: number[]) => {
  return array.map(i => func(i));
};

/*
// OR
const apply2 = (func: NumberFunction, array: number[]) => array.map(i => func(i));
*/

console.log(apply(double, [1, 2, 3, 10, 20, 30]));
console.log(apply((n: number) => n - 1, [1, 2, 3, 10, 20, 30]));

// Finally, we can write a function that returns another function
const numberFunctionMaker = (multiplier: number) => {
  return (n: number) => n * multiplier;
};

/*
// OR
const numberFunctionMaker2 = (multiplier: number) => (n: number) => n * multiplier;
*/

const triple = numberFunctionMaker(3);
console.log(apply(triple, [1, 2, 3, 10, 20, 30]));

const times1000 = numberFunctionMaker(1000);
console.log(apply(times1000, [1, 2, 3, 10, 20, 30]));
