# Tutorial 8

[TOC]

## A. Good software

The `bubblesort` algorithm below was written by a COMP1531 staff from their love for bubbles.
```ts
function bubblesort(array: any[]) {
  const newArray = [...array];
  for (let i = 0; i < newArray.length - 1; i++) {
    for (let j = 0; j < newArray.length - i - 1; j++) {
      if (newArray[j].age > newArray[j + 1].age) {
        // current person older than next person, swap them!
        const temp = newArray[j];
        newArray[j] = newArray[j + 1];
        newArray[j + 1] = temp;
      } else if (newArray[j].age === newArray[j + 1].age && newArray[j].name.localeCompare(newArray[j + 1].name)) {
        // equal age, swap for lexiographical-order names
        const temp = newArray[j];
        newArray[j] = newArray[j + 1];
        newArray[j + 1] = temp;
      }
    }
  }
  return newArray;
}
```
It can be used as follows:
```ts
interface Person {
  name: string;
  age: number;
}

const people: Person[] = [
  { name: 'Miyoung', age: 8 },
  { name: 'Danny', age: 7 },
  { name: 'Bill', age: 7 },
  { name: 'Aaron', age: 7 },
  { name: 'Miyoung', age: 20 },
  { name: 'Jack', age: 20 },
  { name: 'Cherrie', age: 7 },
  { name: 'Iktimal', age: 19 },
];

console.log(bubblesort(people));
```

They did not use the default `.sort()` method of arrays because it is unlikely to be implemented with bubble-sort.

Your tutor will break you up into random groups. Discuss with your group 

1. A few qualities that make a good piece of software.
    > For example,
    > - functional
    > - testable
    > - debuggable
    > - maintainable
    > - measurable
    > - reusable
    > - robust
    > - scalable
    > - extensible

1. Efficiency aside, why is this **implementation of bubble sort** not an example of a good piece of software? How can it be improved?
    > To name a few:
    > - repeated code
    > - side effect of modifying the original array
    > - only works for a `Person` array
    >     - neither reusable nor extensible
    >     - potential error/undefine behaviour when a different type of array is given (wrong parameter type `any[]`), not robust.
    

<details close>

<summary>click to view</summary>

```ts
interface Comparator<Type> {
  (item1: Type, item2: Type): number;
}

function bubblesortGeneric<Type>(array: Type[], compare: Comparator<Type>) {
  // shallow copy the array
  const newArray = [...array];
  for (let i = 0; i < newArray.length - 1; i++) {
    for (let j = 0; j < newArray.length - i - 1; j++) {
      if (compare(newArray[j], newArray[j + 1]) > 0) {
        const temp = newArray[j];
        newArray[j] = newArray[j + 1];
        newArray[j + 1] = temp;
      }
    }
  }
  return newArray;
}

interface Person {
  name: string;
  age: number;
}

const people: Person[] = [
  { name: 'Miyoung', age: 8 },
  { name: 'Danny', age: 7 },
  { name: 'Bill', age: 7 },
  { name: 'Aaron', age: 7 },
  { name: 'Miyoung', age: 20 },
  { name: 'Jack', age: 20 },
  { name: 'Cherrie', age: 7 },
  { name: 'Iktimal', age: 19 },
];

const comparePeople = (person1: Person, person2: Person) => {
  if (person1.age !== person2.age) {
    return person1.age - person2.age;
  }
  return person1.name.localeCompare(person2.name);
};

// Works for Person[]
console.log(bubblesortGeneric(people, comparePeople));

// Works for number[]
console.log(bubblesortGeneric([5, 1, 3, 4, 2], (a, b) => a - b));

interface Polygon {
  shape: string;
  sides: number;
}

const polygons: Polygon[] = [
  { shape: 'pentagon', sides: 5 },
  { shape: 'octagon', sides: 8 },
  { shape: 'triagle', sides: 3 },
  { shape: 'rectangle', sides: 4 },
  { shape: 'heptagon', sides: 7 },
];

// Works for Polygon[]
console.log(bubblesortGeneric(polygons, (poly1: Polygon, poly2: Polygon) => poly1.sides - poly2.sides));
```

</details>


## B. Using Coverage

Below is a piece of software that you may remember from a previous week's activity:
```ts
const ORIGIN_YEAR = 1970;

const isLeap = (y: number) => new Date(y, 1, 29).getDate() === 29;

export const dayToYear = (days) => {
  let year = ORIGIN_YEAR;
  while (days > 365) {
    if (isLeap(year)) {
      if (days > 366) {
        days -= 366;
        year += 1;
      }
    } else {
      days -= 365;
      year += 1;
    }
  }
  return year;
};
```

1. What is code coverage and how it can be useful?
    > - Code coverage is a metric to quantify how much of written source code is executed during testing.
    > - Can help developers improve their tests by considering and accounting for more scenarios in their the code.

1. Run the current tests in [b.coverage/day-to-year.test.ts](b.coverage/day-to-year.test.ts) with the `--coverage` option from `jest`.
Open the resulting `html` file in your browser. How can we interpret this result?
    > ```json
    > "scripts": {
    >   "test": "jest --coverage",
    > }
    > ```
    > ```shell
    > $ npm t day-to-year.test.ts
    > ```
    > Open `./coverage/lcov-report/index.html`, select the file and hover mouse on the highlighted lines for reason. 

1. Write a test case to achieve 100% coverage.
    > ```ts
    > { days: 365 + 365 + 366, year: 1972 }, // "December 31st 1972"
    > ```

1. Make any modifications to the program as appropriate.
    > ```ts
    > } else {
    >   break;
    > }
    > ```
    > after `if (days > 366) {`

## C. System Model - State Diagram

Create a state diagram to describe the states and subsequent transitions that would occur for a grocery store checkout system, from the perspective of the user-machine interaction.

![](https://www.canstarblue.com.au/wp-content/uploads/2018/09/shutterstock_793003627-300x189.jpg)

> See [state.png](state.png):
>
> <details close>
> <summary>click to view</summary>
>
> ![](state.png)
>
> </details>

1. What are some limitations of our current model?

1. How can our model be used in the designing stages of software?