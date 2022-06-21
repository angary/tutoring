const ERROR = { error: 'error' };

function getRectangleDetails(base, height) {
  if (base < 0 || height < 0) {
    return ERROR;
  }
  return {
    area: base * height,
    perimeter: 2 * (base + height),
  };
}

function getSquareDetails(size) {
  return getRectangleDetails(size, size);
}

function getCircleDetails(radius) {
  if (radius < 0) {
    return ERROR;
  }
  return {
    area: Math.PI * radius ** 2,
    perimeter: 2 * Math.PI * radius,
  };
}

console.log('1. Square of size 5:');
console.log(getSquareDetails(5));
console.log();

console.log('2. Rectangle of base 3 and height 6:');
console.log(getRectangleDetails(3, 6));
console.log();

console.log('3. Circle of radius 2:');
console.log(getCircleDetails(2));
