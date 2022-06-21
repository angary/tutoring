# Tutorial 4

## A. Agile

Your tutor will break you up into random groups. You will have 15 minutes to quickly share:

1. When you are running standups and whether they are synchronous or asynchronous
1. How often you meet, how you meet, and what the goals/outcomes of any meetings so far have been
1. Have they or will you try pair programming
1. Any challenges you've faced already after being in a group

Other group members (in other teams) are encouraged to ask questions and learn from what other groups are doing/saying.

## B. Typing

1. Open `package.json` and look through `"dependencies"` and `devDependencies` (if they exist). Install the packages.

1. Install [typescript](https://www.npmjs.com/package/typescript), [ts-node](https://www.npmjs.com/package/ts-node), [ts-jest](https://www.npmjs.com/package/ts-jest) and [@types/jest](https://www.npmjs.com/package/@types/jest) as development dependencies.
    
1. Modify package.json to include any scripts that you may find helpful.

In [b.typing/rescript.js](b.typing/rescript.js) lies a few functions extracted or modified from lab01 and lab02:

### Interface: Functions

<table>
  <tr>
    <th>Name & Description</th>
    <th>Parameters</th>
    <th>Return Type</th>
  </tr>
  <tr>
    <td>
        <code>isLeap</code><br/><br/>
        Given a strictly positive year, return true if it is a <a href='https://en.wikipedia.org/wiki/Leap_year#Algorithm'>leap year</a> and false otherwise.
    </td>
    <td>
        (year: <code>number</code>)
    </td>
    <td>
        <code>boolean</code>
    </td>
  </tr>
  <tr>
    <td>
        <code>countLeap</code><br/><br/>
        Given an array of strictly positive years, return the number of leap years present in the array.
    </td>
    <td>
        (yearArray: <code>number[]</code>)
    </td>
    <td>
        <code>number</code>
    </td>
  </tr>
  <tr>
    <td>
        <code>getSatisfactionResult</code><br/><br/>
        Given a fast food restaurant object, calculate its satisfaction and return the result in a satisfaction object.
    </td>
    <td>
        (fastFoodRestaurant: <code>FastFoodRestaurant</code>)
    </td>
    <td>
        <code>SatisfactionResult</code>
    </td>
</tr>
</table>

#### Satisfaction Formula

The satisfaction of a restaurant is the average score between `customerService`, `foodVariety`, `valueForMoney`, `timeToMake` and `taste`. Thus, the formula is:
```math
\text{satisfaction} = 
\frac{
    \text{customerService}
    + \text{foodVariety}
    + \text{valueForMoney}
    + \text{timeToMake}
    + \text{taste}
}
{5}
```
You do not need to round the satisfaction value.

### Interface: Data Types

<table>
  <tr>
    <th>Interface</th>
    <th>Structure</th>
  </tr>
  <tr>
    <td>
        <code>FastFoodRestaurant</code>
    </td>
    <td>
        Object containing keys
        <pre>{
    name: string,
    customerService: number,
    foodVariety: number,
    valueForMoney: number,
    timeToMake: number,
    taste: number
}</pre>
    </td>
  </tr>
  <tr>
    <td>
        <code>SatisfactionResult</code>
    </td>
    <td>
        Object containing keys
        <pre>{
    restaurantName: string,
    satisfaction: number,
}</pre>
    </td>
  </tr>
</table>

### Task

1. At the bottom of [b.typing/rescript.js](b.typing/rescript.js),
    - what will happen if these functions were supplied with invalid (e.g. wrong type), missing or extra arguments?
    - uncomment a few `console.log` lines and run the program with:
        ```shell
        $ node rescript.js
        ```
        Discuss the results

1. Rename `rescript.js` file to `rescript.ts` and add type annotations to the functions
    
1. What will happen to the invalid console.log statements now when we run the program with `tsc` or `ts-node`?

1. Tests have been written in `rescript.test.ts`. **Export** your functions and check that they pass the given tests.

## C. Linting + Code Review

Below is a piece of software written by a COMP1531 tutor back when they were still a newbie programmer in COMP1511. This was the interface that they followed:

### Interface: Functions

<table>
  <tr>
    <th>Name & Description</th>
    <th>Parameters</th>
    <th>Return Type</th>
    <th>Error</th>
  </tr>
  <tr>
    <td>
        <code>drawX</code><br/><br/>
        Return a string that contains an x of a certain size, made up of smaller x-es.<br/>
        There should be no trailing white spaces.
    <td>
        (size)
    </td>
    <td>
        <code>string</code>
    </td>
    <td>
        Return the string <code>'error'</code> if the given <code>size</code> is not an odd number.
    </td>
  </tr>
</table>

1. Without modifying the code, review the `drawX` function in [c.linting/x.ts](c.linting/x.ts):
    - What, if any, are some good points about the implementation?
    - What are some styling/design issues?

1. Open `package.json` and look through `dependencies` and `devDependencies`. Install them!

1. Install [eslint](https://eslint.org/) and a few additional plugins for linting to work with jest and typescript:

1. Add a `lint` script to `package.json` along with any other scripts that may be useful.
    
1. Use `eslint` to identify any linting issues.
    
1. Use `eslint` to auto-fix most issues.

1. Fix any remaining issues manually and refactor the code if applicable.
