# Tutorial 3

## A. Code Review

In [a.review/shapes.js](a.review/shapes.js), there is an implementation of a program that computes the area and perimeter of different shapes.

<details close>
<summary> Contents of shapes.js </summary>

```js
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

 * Note: this function is in very good shape. No need replace me!
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
'''
1. Square of size 5:
{ area: 25, perimeter: 20 }

2. Rectangle of base 3 and height 6:
{ area: 18, perimeter: 18 }

3. Circle of radius 4:
{ area: 50.26548245743669, perimeter: 25.132741228718345 }
'''

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
```

</details>

Your tutor will share a hackmd.io file for the class to collaboratively modify. In your **project groups**:

1. Discuss any code smells with the current design (i.e. the helper function `getShapeDetails`).
2. Refactor [a.review/shapes.js](a.review/shapes.js) to address these flaws and document the reason for your changes. You can be flexible with the design (e.g. you can refactor/remove/replace the function `getShapeDetails`).

## B. Package Management

In your project groups, consider the interface below:

### Interface: Functions

| Name & Description                                                                                                                                                                                                                                                                                | Parameters | Return Object                | Errors                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------- | -------------------------------------------- |
| `stamp` <br/><br/> Given an email, stamp it with a unique `identifier` and a `timeString`. <br/><br/>The `identifier` universally unique (e.g. someone from across the world has an improbable chance of generating the same string).<br/><br/>It should not rely on the characters in the email. | (email)    | `{ identifier, timeString }` | Return `{ error }` when the email is invalid |

### Interface: Data Types

| If the variable name | It is of type                                                                          |
| -------------------- | -------------------------------------------------------------------------------------- |
| is **error**         | `string` with value exactly `'error'`                                                  |
| is **email**         | `string`                                                                               |
| is **identifier**    | `string` that is globally unique                                                       |
| is **timeString**    | `string` in the format `'WEEKDAY - hh:mm:ss [am/pm]"`. e.g. `'Saturday - 06:03:54 pm'` |

For example:

```js
stamp("valid@email.com");
```

may return something like:

```javascript
return {
  identifier: "some unique string that no one can guess",
  timeString: "Saturday - 06:03:23 pm",
};
```

1. Before researching, discuss with your group the kinds of tools you'd likely need to solve this problem.

1. Look through the [npm registry](https://www.npmjs.com/) or other sources for any package that meets your needs. Note them down. If you have time, try to complete the function.

1. Each group will share their packages (and potentially code) with the class. Your tutor will demonstrate how these packages can be installed with `npm` and used (by importing) in [b.stamp/stamp.js](b.stamp/stamp.js)

## C. Testing, Coding, Multi-file

In [c.pretty/pretty.js](c.pretty/pretty.js), there exists a stub for the function `pretty` which converts 24-hour time into 12-hour time.

You can assume all inputs will be a valid 24-hour time (e.g. from `0000` to `2359`).

Here are a few example cases:

```js
pretty('0000') => '12:00 am'
pretty('0030') => '12:30 am'
pretty('0100') => '01:00 am'
pretty('0730') => '07:30 am'
pretty('1159') => '11:59 am'
pretty('1200') => '12:00 pm'
pretty('1930') => '07:30 pm'
pretty('2359') => '11:59 pm'
```

### Part 1 - Tests

1. `cd` into `c.pretty` and use `npm` to install `jest` and `@babel/preset-env` as development dependencies

1. Modify `package.json` to use `jest` as our test script

1. Write tests for the function `pretty` in [c.pretty/pretty.test.js](c.pretty/pretty.test.js). Check that the code fails your test initially.

### Part 2 - Implementation

Implement the function `pretty` and check that it passes all of your tests.

### Part 3 - main.js

In [c.pretty/main.js](c.pretty/main.js), write a program that reads 24-hour time input and outputs 12-hour time.
For example:

```shell
$ node main.js
Enter time: 0000     # user enters 0000
00:00 am
Enter time: 1159     # user enters 1159
11:59 am
Enter time: 1200     # user enters 1200
12:00 pm
Enter time: ^C       # Ctrl+C
$
```

You are recommended to use the package [prompt-sync](https://www.npmjs.com/package/prompt-sync):

```shell
$ npm install prompt-sync
```
