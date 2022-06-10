# Tutorial 2

[TOC]

For online tutorials on Teams, if breakout rooms do not work well for you, consider:

1. Create public channels for random groups, e.g. TUTGRP1, TUTGRP2, ...
1. Pre-assign students beforehand, or use a [random group generator](https://www.randomlists.com/team-generator) during the tutorial.
1. Share the results and allow students to start separate calls in these public channels. Inform them of the time to come back (can also tag @General, or hop into their calls when time is almost up to remind).

## A. Code Review

> 15 minutes

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

   > create a new array from the original array with even numbers doubled.

1. How can the style be improved here?

   > - More descriptive variable names
   > - Consistent and proper spacing
   > - 2 space indentation
   >   - using 4 spaces is fine if done consistently
   >   - however, we use 2 in COMP1531
   > - `const` instead of `let` (arrays can be modified/used without reassigning in this case)

1. How can we modify the code to be less like C and more Javascripty?
   > See [solutions/review.js](solutions/review.js) (avoid filter/map/reduce!):
   >
   > <details>
   > <summary>Click to view</summary>
   >
   > ```js
   > const integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
   > const result = [];
   > for (const integer of integers) {
   >   result.push(integer % 2 === 0 ? integer * 2 : integer);
   > }
   > console.log(result);
   >
   > /*
   > 
   > // NOTE: filter/map/reduce will be covered in more details in week 4+.
   > // YOU DO NOT NEED TO UNDERSTAND THE CODE BELOW BEFORE THEN.
   > 
   > const integerArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
   > const result = integerArray.map(integer => integer % 2 === 0 ? integer * 2 : integer);
   > console.log(result);
   > 
   > */
   > ```
   >
   > </details>

Share some of your findings with the class and assist your tutor in developing a new solution.
How different is this from the original code?

## B. Teamwork

15 minutes

For this activity, in the interest of time, you may want to have each group present just one main point from each question.

In random groups,

1. Brainstorm a list of good and poor attributes for team members working on a project.

   > Answers will vary:
   >
   > - Good communicaticator
   >   - listen and provide inputs
   >   - document their work
   > - Good time management
   >   - propose self-induced deadlines
   >   - complete assigned tasks on time
   > - Honest and responsible
   >   - notify groups early if they cannot complete their part on time
   >   - seek help from teammates (rather than suffering in silence)
   >
   > Poor attributes could include the converse of the above.

1. Suppose there is a member in a group who has gone silent and has yet to complete much of their assigned work. The reason is unknown.

   - How should the remaining members approach the situation?

     > **Approaches** (answers may wary):
     >
     > 1. Try to reach out to the member via email and Teams.
     >
     >    - If the group has new knowledge that this member is struggling, devise a way to assist them in getting back on track (e.g. pair-programming)
     >
     > 1. Let your tutor know and keep them updated.

   - What can groups do beforehand such that if this occurs, they can manage or minimise the impact?
     > **Preparations** (answers may wary)
     >
     > 1. Hold regular meetings and standups and document these in minutes/standup notes.
     >
     > 1. Introduce self-imposed deadlines that are a few days before the iteration due date to leave time for teammates to cover or redistribute remaining work

## C. Using Javascript & Git

> 15 minutes

1. Create and checkout a new branch called `rainfall_solution`

   > ```shell
   > $ git checkout -b rainfall_solution
   > ```

1. What does the output of `git branch` indicate?
   > Also useful for showing remote branches: `git branch --all` (or `-a` for short)
1. Implement the function `rainfall` in [rainfall.js](rainfall.js), but avoid pushing this code to Gitlab for the time being.

   > See [solutions/rainfall.js](solutions/rainfall.js) (avoid filter/map/reduce!):
   >
   > <details close>
   > <summary>click to view</summary>
   >
   > ```js
   > function rainfall(integers) {
   >   let total = 0;
   >   let positiveCount = 0;
   >   for (const integer of integers) {
   >     if (integer > 0) {
   >       total += integer;
   >       positiveCount++;
   >     }
   >   }
   >   return positiveCount > 0 ? total / positiveCount : null;
   > }
   >
   > /*
   > 
   > // NOTE: filter/map/reduce will be covered in more details in week 4+.
   > // YOU DO NOT NEED TO UNDERSTAND THE CODE BELOW BEFORE THEN.
   > 
   > function rainfallAlternative(integers) {
   >   // Filter for 'integer' such that 'integer is greater than 0'
   >   const positives = integers.filter(integer => integer > 0);
   >   if (positives.length === 0) {
   >     return null;
   >   }
   >   const sum = positives.reduce((currentSum, integer) => currentSum + integer);
   >   return sum / positives.length;
   > }
   > 
   > */
   > ```

   </details>

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

   > Since this is a new local branch that Gitlab has no knowledge of, we need to specify the `--set-upstream` (or `-u` for short)
   >
   > ```shell
   > $ git push -u origin rainfall_solution
   > ```
   >
   > after the initial set-up for a new branch, the regular `git push` will work.

1. Open the link that is displayed in the output of the previous push command and create a merge request on Gitlab. Are you able to merge?

1. In the terminal, attempt to pull Gitlab's `master` branch into our local `rainfall_solution` branch.
   > ```shell
   > $ git pull origin master
   > ```
   >
   > Note: the pull command above does not update your "local" master branch, so when creating a new feature branch, make sure to pull again on master.
   >
   > Alternative (longer) method: checkout master, pull, checkout rainfall_solution, merge master.
1. Resolve all conflicts, push to Gitlab and attempt to merge the merge request once again.
   > May also want to locally checkout the `master` branch, `git log`, then `git pull` and `git log`.
