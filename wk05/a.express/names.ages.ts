interface NameAge {
  name: string;
  age: number;
}

let namesAges: NameAge[] = [];

function getNameAge(name: string) {
  return namesAges.find((nameAge) => nameAge.name === name);
}

export function addNameAge(name: string, age: number) {
  if (name === '' || age <= 0) {
    return { error: 'error' };
  }
  const person = getNameAge(name);
  if (person) {
    return { error: 'error' };
  }
  namesAges.push({ name, age });
  return {};
}

export function getNamesAges(minAge = 1) {
  if (minAge <= 0) {
    return { error: 'error' };
  }
  return {
    namesAges: namesAges
      .filter((nameAge) => nameAge.age >= minAge)
      .sort((a, b) =>
        (b.age - a.age) ? b.age - a.age : a.name.localeCompare(b.name)
      ),
  };
}

export function editNameAge(name: string, age: number) {
  if (age <= 0) {
    return { error: 'error' };
  }
  const index = namesAges.findIndex((nameAge) => nameAge.name === name);
  if (index === -1) {
    return { error: 'error' };
  }
  namesAges[index] = { name, age };
  return {};
}

export function removeNameAge(name: string) {
  const index = namesAges.findIndex((nameAge) => nameAge.name === name);
  if (index === -1) {
    return { error: 'error' };
  }
  namesAges.splice(index);
  return {};
}

export function getStats() {
  if (namesAges.length === 0) {
    return { error: 'error' };
  }
  const ages = namesAges.map((nameAge) => nameAge.age);
  return {
    minAge: Math.min(...ages),
    maxAge: Math.max(...ages),
    averageAge: ages.reduce((sum, nameAge) => sum + nameAge) / ages.length,
  };
}

export function clear() {
  namesAges = [];
  return {};
}
