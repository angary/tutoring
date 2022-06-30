interface NameAge {
  name: string,
  age: number,
}

let namesAges: NameAge[] = [];

export function addNameAge(name: string, age: number) {
  // FIXME Group 1
  return {};
}

export function getNamesAges(minAge?: number) {
  // FIXME Group 2
  return {
    namesAges: [
      { name: 'one', age: 1 },
      { name: 'two', age: 2 },
    ]
  };
}

export function editNameAge(name: string, age: number) {
  // FIXME Group 3
  return {};
}

export function removeNameAge(name: string) {
  // FIXME Group 4
  return {};
}

export function getStats() {
  // FIXME Group 5
  return {
    minAge: 0,
    maxAge: 10,
    averageAge: 5,
  };
}

export function clear() {
  namesAges = [];
  return {};
}
