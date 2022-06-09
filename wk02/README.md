# Tutorial 2

[TOC]

## A. Code Review

In random groups, you have 8 minutes to review the code in [review.js](review.js):

```js
let x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result = [];
for (let i = 0; i < x.length; i++) {
  if (x[i] % 2 === 0) {
    result.push(x[i] * 2);
  } else {
    result.push(x[i]);
  }
}
console.log(result);
```

Discuss the questions below:

1. What does it do?

1. How can the style be improved here?

1. How can we modify the code to be less like C and more Javascripty?

Share some of your findings with the class and assist your tutor in developing a new solution.
How different is this from the original code?

## B. Teamwork

In random groups,

1. Brainstorm a list of good and poor attributes for team members working on a project.

1. Suppose there is a member in a group who has gone silent and has yet to complete much of their assigned work. The reason is unknown.
   - How should the remaining members approach the situation?
   - What can groups do beforehand such that if this occurs, they can manage or minimise the impact?

## C. Using Javascript & Git

1. Create and checkout a new branch called `rainfall_solution`

1. What does the output of `git branch` indicate?
1. Implement the function `rainfall` in [rainfall.js](rainfall.js), but avoid pushing this code to Gitlab for the time being.

1. On **Gitlab's** master branch, replace the stub `rainfall` function with the alternative solution below:
   <details close>
   <summary>Click to view alternative solution</summary>

   ```javascript
   /**
    * Compute the average of only the positive
    * elements in the integer array.
    * Return null if there are no positive integers.
    */
   function rainfall(integers) {
     let total = 0;
     let count = 0;
     for (let i = 0; i < integers.length; i++) {
       if (integers[i] > 0) {
         total += integers[i];
         count++;
       }
     }
     if (count === 0) {
       return null;
     } else {
       return total / count;
     }
   }
   ```

   </details>

   Commit the change. Also, confirm that there are currently no additional branches on Gitlab.

1. Back in your local terminal, add, commit and push your `rainfall_solution` branch to Gitlab.

1. Open the link that is displayed in the output of the previous push command and create a merge request on Gitlab. Are you able to merge?

1. In the terminal, attempt to pull Gitlab's `master` branch into our local `rainfall_solution` branch.
1. Resolve all conflicts, push to Gitlab and attempt to merge the merge request once again.
