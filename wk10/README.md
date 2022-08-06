# Tutorial 10

[TOC]

## A. MyExperience

It's time to fill out MyExperience!

Your tutor will give you 10 minutes to fill out the MyExperience survey which you can access on UNSW Moodle.

Please do so (even if it is just ticking the boxes) as the information is invaluable to us, and also because the cat below will be eternally unhappy otherwise!

![lulu](assets/lulu.jpg)

## B. History

1. Create a new branch from this repository called `history`.
   > ```shell
   > $ git checkout -b history
   > ```
1. Create a new file called `lost.txt` and commit it to history.

   > ```shell
   > $ echo "sayonara" > lost.txt
   > $ git add lost.txt
   > $ git commit -m "added lost.txt"
   > ```

1. Look at the last 3 commits in the log.

   > ```shell
   > $ git log -3
   > ```

1. Hard reset to the second most recent commit (before the one we've just done). What does this do?

   > ```shell
   > $ ls
   > $ git reset --hard <FIRST_FEW_CHARACTERS_OF_RELEVANT_COMMIT_HASH>
   > $ ls
   > $ git status
   > $ git log -3
   > ```

1. Create a new file called `retain.txt` and commit it to history
   > ```shell
   > $ echo "legendary artifact" > retain.txt
   > $ git add retain.txt
   > $ git commit -m "added retain.txt"
   > ```
1. This time, soft reset to the second most recent commit. What does this do?
   ```shell
   $ git reset --soft <FIRST_FEW_CHARACTERS_OF_RELEVANT_COMMIT_HASH>
   $ ls
   $ git status
   $ git log -3
   ```

## C. Complexity Analysis

> 10 minutes

Below are solutions to `lab01_leap`. For each function, draw a control flow graph and calculate the resulting cyclomatic complexity.

1. `isLeap`:

   ```ts
   const isLeap = (year: number) => {
     let result: boolean;
     if (year % 4 !== 0) {
       result = false;
     } else if (year % 100 !== 0) {
       result = true;
     } else if (year % 400 !== 0) {
       result = false;
     } else {
       result = true;
     }
     return result;
   };
   ```

   > <details close>
   > <summary>view diagram</summary>
   >
   > ![](solutions/isLeapComplexity.png)
   >
   > </details>
   >
   > C = 4

1. `getNextLeap`:

   ```ts
   const getNextLeap = (year: number) => {
     let nextLeap = year + 1;
     while (!isLeap(nextLeap)) {
       nextLeap++;
     }
     return nextLeap;
   };
   ```

   > <details close>
   > <summary>view diagram</summary>
   >
   > ![](solutions/getNextLeapComplexity.png)
   >
   > </details>
   >
   > C = 2

1. `countLeaps`:
   ```ts
   const countLeaps = (yearArray: number[]) => {
     let count = 0;
     for (const year of yearArray) {
       if (isLeap(year)) {
         count++;
       }
     }
     return count;
   };
   ```
   > <details close>
   > <summary>view diagram</summary>
   >
   > ![](solutions/countLeapsComplexity.png)
   >
   > </details>
   >
   > C = 3

You may want to retain your notes for the incoming Kahoot, which will contain a more challenging example.

## D. Kahoot Activity

You will spend the remaining part of the tutorial doing a Kahoot activity with your tutor. They will share a code with you!
