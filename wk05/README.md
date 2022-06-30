# Tutorial 5

## A. Express Server Build

### The Interface

Below is an interface for a names-ages server:

<details close>
<summary>click to view</summary>

<table>
  <tr>
    <th>Name & Description</th>
    <th>HTTP Method</th>
    <th>Data Types</th>
    <th>Errors</th>
  </tr>
  <tr>
    <td>
      <code>/addnameage</code><br/><br/>
      Given a name and an age, add the entry into the data store if it is valid.
    </td>
    <td>
        ???
    </td>
    <td>
      <b>??? Parameters</b><br/>
      <code>{name: string, age: number}</code>
      <br/><br/>
      <b>Return Object</b><br/>
      <code>{}</code>
    </td>
    <td>
      Return <code>{error: 'error'}</code> when:
      <ul>
        <li>
          The given name is an empty string, <code>""</code>.
        </li>
        <li>
          The given age is not strictly positive.
        </li>
        <li>
          The given name already exists in data.
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <code>/getnamesages</code><br/><br/>
      Return all namesAges that are at equal to or greater than the given <code>minAge</code>.
      <br/><br/>
      If no <code>minAge</code> is supplied, all namesAges are returned.
      <br/><br/>
      Names should be returned in descending age order (e.g. eldest at index 0),
      or in lexiographical case-insenitive order if the ages are equal.
    </td>
    <td>
        ???
    </td>
    <td>
      <b>??? Parameters</b><br/>
      <code>{minAge?: number}</code>
      <br/><br/>
      <b>Return Object</b><br/>
      <code>{namesAges: NameAge[]}</code>
    </td>
    <td>
      Return <code>{error: 'error'}</code> when:
      <ul>
        <li>
          minAge, if given, is not strictly positive.
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <code>/editnameage</code><br/><br/>
      Edit the age for the given name entry.
    </td>
    <td>
      ???
    </td>
    <td>
      <b>??? Parameters</b><br/>
      <code>{name: string, age: number}</code>
      <br/><br/>
      <b>Return Object</b><br/>
      <code>{}</code>
    </td>
    <td>
      Return <code>{error: 'error'}</code> when:
      <ul>
        <li>
          The new age is not strictly positive.
        </li>
        <li>
          The given name does not exist in data.
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <code>/removenameage</code><br/><br/>
      Remove the given nameAge entry.
    </td>
    <td>
      ???
    </td>
    <td>
      <b>??? Parameters</b><br/>
      <code>{name: string}</code>
      <br/><br/>
      <b>Return Object</b><br/>
      <code>{}</code>
    </td>
    <td>
      Return <code>{error: 'error'}</code> when:
      <ul>
        <li>
          The given name does not exist in data.
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <code>/getstats</code><br/><br/>
      Return an object containing stats about the age of all entries
    </td>
    <td>
      ???
    </td>
    <td>
      <b>??? Parameters</b><br/>
      <code>{}</code>
      <br/><br/>
      <b>Return Object</b><br/>
      <code>{stats: AgeStats}</code>
    </td>
    <td>
      Return <code>{error: 'error'}</code> when:
      <ul>
        <li>
          There is no entries in the data store.
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <code>/clear</code><br/><br/>
      Remove all entries from the data store.
    </td>
    <td>
      ???
    </td>
    <td>
      <b>??? Parameters</b><br/>
      <code>{}</code>
      <br/><br/>
      <b>Return Object</b><br/>
      <code>{}</code>
    </td>
    <td>
      N/A
    </td>
  </tr>
</table>

<table>
  <tr>
    <th>Interface</th>
    <th>Structure</th>
  </tr>
  <tr>
    <td>
      NameAge
    </td>
    <td>
      <pre>{
  name: string,
  age: number
}</pre>
    </td>
  </tr>
  <tr>
    <td>
      AgeStats
    </td>
    <td>
      <pre>{
  minAge: number,
  maxAge: number,
  averageAge: number
}</pre>
    </td>
  </tr>
</table>

</details>

### Part 1 - Building the backend

Your tutors will break you up into five random groups.

1. Without considering the HTTP aspect of the specification, each group will be assigned a backend "function" to implement (similar to iteration 1) in the next 10 minutes.

2. Your group should also discuss the `HTTP` method (GET/PUT/POST/DELETE) and the parameter type (Query/Body) that would be appropriate for the HTTP route which will wrap around your function.

Below is the starter code for the backend functions in `names.ages.ts`:

<details close>
<summary>click to view</summary>

```ts
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

```

</details>

If your team wishes to communicate with another team, whether for cooperation or intimidation, your team should send an ambassador. At the end of 10 minutes, your tutor will complete the remaining parts of this activity together with the class.

### Part 2 - Server Installation

1. Install all dependencies and devDependencies from `package.json`.

1. Install [express](https://www.npmjs.com/package/express) for the server and [morgan](https://www.npmjs.com/package/morgan) to help with debugging by logging HTTP requests.

1. Install the type definitions for the packages above.

1. Finally, add any relevant scripts to your `package.json`.

### Part 3 - Server Stubs

Write a simple express server that contains corresponding routes in `server.ts`. The routes should simply be stubs for now.

### Part 4 - Failing HTTP Tests

For testing, install [sync-request](https://www.npmjs.com/package/sync-request) which will allow us to send HTTP requests to our server.

Write two different test cases for
1. A route that uses body parameters
1. A route that uses query parameters

These tests should fail when you run them.

### Part 5 - Implementation

Complete the implementation of the two routes in part 3 wrapping them around your backend "functions". Your tests should (hopefully) pass.

### Part 6 - Automarking

Complete the remaining routes. Your tutor will run a pre-written `automarking.test.ts` on the server to see how well the class performed.

## B. Bonus Activity: First-class functions

<details close>

<summary>click to view</summary>
  
<br/>


Below is an interface called `NumberFunction`, which describes functions that take in a number as input and return a number as output:
```ts
interface NumberFunction {
  (n: number): number;
}
```

1. Declare a variable named `double` and assign it to an anonymous `NumberFunction` function. `double` takes in an argument `n: number` and returns twice of `n`. Show how this can be done with the
    - normal function syntax
    - arrow function syntax


1. Create another function called `apply` which takes in a `numFunc: NumberFunction` and an `array: number[]`. The `apply` function should return a new array where each new element is the result of applying `numFunc` on the original element.

1. Finally, create a function `numberFunctionMaker` which takes in a `multiplier: number` and returns a `NumberFunction`. Use `numberFunctionMaker` to create new functions such as `triple`, `quadruple`, `times1000`, etc and show how this can be used in conjunction with our `apply` function.

</details>
    
## C. Bonus Activity: JSON and YAML

<details close>

<summary>click to view</summary>
  
<br/>

Convert the `JSON` file below to `YAML`:

```json
{
  "channels": [
    {
      "id" : 3,
      "name" : "Channel 1",
      "messages" : [
        {
          "id" : 1,
          "user_id" : 5,
          "message" : "Hello world"
        },
        {
          "id" : 2,
          "user_id" : 5,
          "message" : "Its me"
        },
        {
          "id" : 3,
          "user_id" : 7,
          "message" : "What are you doing??"
        }
      ]
    },
    {
      "id" : 4,
      "name" : "Channel 2",
      "messages" : []
    }
  ]
}
```

Convert the `YAML` file below to `JSON`:

```yaml
---
keyData:
  JWT_SECRET: wfasduf98ajs98d5r342m5l
  HASH_SALT: 8s9982345798237948
users:
- id: 3
  email: z1234567@unsw.edu.au
  firstName: Micky
  lastName: Mouse
  handle: mickymouse
  sessions:
  - SDJKFNSDJf
  - 23849887es
  - sd78fy8shf
- id: 4
  email: z9876543@unsw.edu.au
  firstName: Micky
  lastName: Mouse
  handle: mickymouse1
  sessions:
  - 89sF*(sdf8
  - sdf89sdjff
  - '4903509455'
```

</details>
