# Iteration 1 General Feedback

Hey everyone, here's just some general iteration 1 feedback :)

There's 3 main sections for the feedback, **Code**, **Tests** and **Git**.
This has been split into **high priority** (this would have likely impacted your mark if you did not implement this) and **low priority** (you likely would not have lost marks from not doing this, but it would still help).

Note that a lot of the JavaScript syntax i.e. object destructuring or higher order functions are shown / introduced in the labs or their solutions, so please do your labs or skim the solution (which can be found in the `solution` branch).

## Code

### High Priority

- Use helper functions for repeated code - you can write them in some file i.e. `util.js` and import them in other files
  - I.e. often times you have to check if an `authUserId` is valid, a helper function like `getUserFromId()` would be useful
  - This makes your code more readable and cleaner because the loops / code for finding a user is removed, and the function name serves to "self document" what is going on
  - If we change how the data is stored, i.e. implement a database like postgresql, rather than have to change all the code for finding a user in each function, we just have to change the helper function
- Use higher order functions like `map`, `filter`, `find`, etc in your code.
  This will **SIGNIFICANTLY CLEAN UP YOUR CODE**.

  - You can find more details about them in the week 4 lecture "Advanced Functions"
  - You can find examples of this in action in `lab04_encanto` (make sure you understand what's going on in the following example of code)
    <details>
    <summary>Show code</summary>

    ```js
    export function extractNamesMixed(array: (Madrigal | Song)[]): string[] {
      return array.map((i: Madrigal | Song) => i.name);
    }

    export function sortedMadrigals(madrigals: Madrigal[]): Madrigal[] {
      return [...madrigals].sort((m1, m2) => {
        if (m1.age !== m2.age) {
          return m1.age - m2.age;
        }
        return m1.name.localeCompare(m2.name);
      });
    }

    export function filterSongsWithMadrigals(
      madrigals: Madrigal[],
      songs: Song[]
    ): Song[] {
      return songs.filter((s) => madrigals.some((m) => madrigalIsSinger(m, s)));
    }

    export function getMostSpecialMadrigal(
      madrigals: Madrigal[],
      songs: Song[]
    ): Madrigal {
      return madrigals.reduce((m1, m2) => {
        const m1Songs = songs.filter((s) => madrigalIsSinger(m1, s)).length;
        const m2Songs = songs.filter((s) => madrigalIsSinger(m2, s)).length;
        return m1Songs >= m2Songs ? m1 : m2;
      });
    }
    ```

  </details>

- Check for errors before you have the rest of the logic (an easy way to ensure this is ensure all, or at least most of your `return { error: 'error' }` before you return what is supposed to be returned in a success case)

### Low Priority

- The standard way for documenting JavaScript / TypeScript functions is a comment above the function in the following format

  ```js
  /**
   * @param {number} a - the first number to add
   * @param {number} b - the second number to add
   * @returns {number} - the result of the sum of a and b
   */
  const sum (a, b) => a + b;
  ```

  Note the type declaration i.e. `{number}` can be removed if it is in TypeScript, i.e.

  ```ts
  /**
   * @param a - the first number to add
   * @param b - the second number to add
   * @returns - the result of the sum of a and b
   */
  const sum (a: number, b: number): number => a + b;
  ```

  This is useful as using a text editor like VSCode will show the comment you've written if you hover over the function.

- If the variable name is the same as the name of the key in an object, you can omit the key, i.e.

  ```js
  // Instead of:
  return {
    authUserId: authUserId,
    someKeyName: someVariableName,
  };

  // You can remove the key (if the key and variable name is the same)
  return {
    authUserId,
    someKeyName: someVariableName,
  };
  ```

- There are often cleaner ways to loop through an array than `for (let i = 0; i < array.length; i++)`, i.e.

  - `for (const item of array)`
  - `array.forEach((item, index) => {...})`

  A list of the pros and cons of looping methods can be found [here](wk01/shopping.js)

- Avoid comparing variables with booleans in conditional statements, i.e.

  ```js
  // Instead of:
  if (isValidUser === true || isValidChannel === false) { ... }

  // Do this:
  if (isValidUser || !isValidChannel) { ... }
  ```

- You can initialise arrays with variables, i.e.

  ```js
  // Instead of:
  const array = [];
  array.push(x);

  // Do this:
  const array = [x];
  ```

## Tests

### High Priority

- Make sure your tests are all **BLACK BOX**, this means

  - Not importing the data store
  - Not making assumptions about the implementation, i.e. do not assume a new user's ID is `0` and it increments by 1 with each register

  To know for sure that an `authUserId` is invalid, you can do something like

  ```js
  describe("someFunction tests", () => {
    test("error case: Non-existent authUserId input", () => {
      clearV1();
      const { authUserId } = authRegisterV1(...);
      expect(someFunction(authUserId + 1).toStrictEqual({ error: "error" }));
    });
  });
  ```

- Make sure that all your tests have good names, you can make the text description as long as you want
  To check determine if a name is good, try running

  ```sh
  jest --verbose
  ```

  and see if you can understand what each test is testing for.
  Some tips is to use

  - Move all tests for a single function inside a `describe()` function, and then inside that, a group of `test()` functions to test for specific cases
  - A naming scheme like `success case: ${description of test}` or `error case: ${description of test}` so that you know which tests test for error cases or not

- Try to avoid repetition in tests, i.e. take advantage of the `beforeEach(() => { ... })` function which runs before each test case.
  Inside this function, you might like to do something like
  - Clearing out the data
  - Initialising test variables (i.e. registering users)

### Low Priority

- When testing for things like a 50 character limit on an input:

  ```js
  // Instead of:
  const fiftyLetterWord = "12345678901234567890123456789012345678901234567890";

  // Do this:
  const fiftyLetterWord = "a".repeat(50);
  ```

- You can use [object destructuring](https://dmitripavlutin.com/javascript-object-destructuring/) to extract out the variables of an object from the return value of a function, i.e.

  ```js
  // `authUserId` is now a number which is the user id
  const { authUserId } = authRegisterV1(...);

  // `user1` is the id of the first user, and `user2` is the id of the second user
  const { authUserId: user1 } = authRegisterV1(...);
  const { authUserId: user2 } = authRegisterV1(...);
  ```

## Git

### Low Priority

There tends to be a lot of commits (or even merge requests) that are repeated / doing similar things in the same time.
I.e.

- Adding the word `export` before a single function and making a MR for that.
  In this case, it would be good to group multiple commits doing this for different functions into one commit and or MR
- Fixing a mistake and having multiple commits for it.
  In this case, try to avoid pushing your code immediately after a commit unless you know the commit is all good.
  You can overwrite a local commit by typing
  ```
  git add ${file}
  git commit --amend -m ${message}
  ```
  to overwrite a local commit (however you cannot overwrite a commit that you have already pushed)
