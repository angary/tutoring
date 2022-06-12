/**
 * "good" helper function that returns the area of these shapes:
 * - square
 * - rectangle
 * - circle
 *
 * Note: shape must always be valid, otherwise this function won't work.

 * Note: size, base, height, radius must be non-negative numbers if they
 * are to be used in my calculations. If the arguments are unused, set
 * them to null or whatever.

 * Note: this function is in very good shape. No need for change!
 */
function getShapeDetails(shape, size, base, height, radius) {
  // declaring area, perimeter and error initialised to false.
  let area;
  let perimeter;
  let error = false;

  if (shape === "square") {
    if (size < 0) {
      // size negative, set error to true
      error = true;
    }
    // The shape is a square, area is size times size
    area = size * size;
    // The shape is a square, perimeter is 4 * size
    perimeter = 4 * size;
  } else if (shape === "rectangle") {
    if (base < 0 || height < 0) {
      // base or height is negative, error true!
      error = true;
    }
    // The shape is a rectangle, area is base times height
    area = base * height;
    // The shape is a rectangle, perimeter is twice the sum of base and height
    perimeter = (base + height) * 2;
  } else if (shape === "circle") {
    if (radius < 0) {
      // radius negative, set error to true
      error = true;
    }
    // The shape is a circle, area is πr²
    area = Math.PI * radius * radius;
    // The shape is a circle, return 2πr
    perimeter = 2 * Math.PI * radius;
  } else {
    // user's at fault, not an error with numbers.
    // just set to 0. They should read the Notes!
    area = 0;
    perimeter = 0;
  }

  if (error === true) {
    // there is an error somewhere, likely negative numbers.
    return { error: "error" };
  }

  // success, return area and perimeter
  return { area: area, perimeter: perimeter };
}

/*
When run with
    $ node shapes.js

Program should output:
```
1. Square of size 5:
{ area: 25, perimeter: 20 }

2. Rectangle of base 3 and height 6:
{ area: 18, perimeter: 18 }

3. Circle of radius 4:
{ area: 50.26548245743669, perimeter: 25.132741228718345 }
```

- Your code should work for varying shapes and sizes.
- The function getShapeDetails can be modified/replaced if you wish.
*/
console.log("1. Square of size 5:");
console.log(getShapeDetails("square", 5, null, null, null));
console.log();

console.log("2. Rectangle of base 3 and height 6:");
console.log(getShapeDetails("rectangle", null, 3, 6, null));
console.log();

console.log("3. Circle of radius 4:");
console.log(getShapeDetails("circle", null, null, null, 4));
