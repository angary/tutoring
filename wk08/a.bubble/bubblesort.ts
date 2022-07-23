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
