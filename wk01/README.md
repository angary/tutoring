# Tutorial 1

[TOC]

## A. Introduction and Problem Solving

1. Your tutor will split you into your project groups with an icebreaker activity and a problem to solve in 15 minutes. When time is up, they'll ask for your brief introduction and answer.

1. Come back together and reflect with your tutor on how you came up with those answers

## B. From C to Javascript: A quick overview

### Part 1 - Basic Syntax, Input/Output, Conditionals & Control Flow

Consider the following C program in the file [welcome.c](welcome.c):

```c
/*
 * [welcome.c]
 *
 * A simple program to print a welcome message
 * and print 10 numbers with information about
 * whether they are odd or even.
 */
#include <stdio.h>

#define SIZE 10

int main(void) {

    char message[] = "Welcome to COMP1531!";
    printf("%s\n", message);

    printf("Numbers from 1 to %d\n", SIZE);
    for (int num = 1; num <= SIZE; num++) {
        if (num % 2 == 0) {
            printf("EVEN: %d\n", num);
        } else {
            printf("ODD:  %d\n", num);
        }
    }
    return 0;
}
```

In this repository, there is another file called [welcome.js](welcome.js). In this file, convert the C program above into a JavaScript program.

As you write the program, discuss the following questions:

- Why don't we need to specify the type of a variable when we declare it?

> JavaScript is _dynamically typed_, AKA "duck typing" - the interpreter figures out at runtime what the type of the variable is.

- What are `const` and `let`?

> `const` is used to declare a constant, whilst `let` is used to declare a variable.

- How is JavaScript's `console.log` function different to `printf` in C?

> - `console.log` automatically adds a new line at the end
> - Template strings (AKA formatting) in `console.log` is done through using backtick quotes and having the variable inside a `` console.log(`${variable}`; ``). In `printf`, it is done through `printf("%s\n", variable);`.

### Part 2 - Looping through Arrays

Create a new file called [shopping.js](shopping.js).

In this file, write a program that stores an array of strings containing items in a shopping list.

- Use a regular `for` loop to print each element in the array using their indices.
- Next, change your program to use a `for-of` loop and print each element out instead.

### Part 3 - Functions

Consider the following C program in [cube.c](cube.c):

```c
/**
 * [cube.c]
 */

#include <stdio.h>

int cube(int x);

int main(void) {

    int number = 5;
    int result = cube(number);
    printf("%d^3 = %d\n", number, result);

    return 0;
}

int cube(int x) {
    return x * x * x;
}
```

Convert this into a JavaScript program.

As you write the program, answer the following questions:

- Why don't JavaScript programs need a `main` function?

> Because JavaScript has an interpreter (node) that reads the code from top
> down and runs it as it reads it

- Which operator can we use instead of needing to write `x * x * x`?

> `x ** 3` or more generally `number ** exponent`

## C. Git Fundamentals

1. In the terminal, use the command

   ```shell
   $ git status
   ```

   What does it say about the files we have added or modified (e.g. [cube.js](cube.js))?

> If a file is added, then there is a `U` next to the file name meaning that it is "untracked" by Git.
> If a file is modified after it has been added to git, then there is a `M` next to the file name meaning that it has been "modified".

1. Add [cube.js](cube.js) to the git's staging area (index) using the command

   ```shell
   $ git add cube.js
   ```

   then type `git status` again. What changed?

> Now there is an `A` next to the file meaning that it has been added.

1. To make a commit with a relevant message for our changes, use the command

   ```shell
   $ git commit -m 'finished cube.js'
   ```

   then type `git status` again. What's different?

> We have made the changes locally but we have not uploaded out changes to the remote repository. 2. Push the committed changes to Gitlab with the command

```shell
$ git push
```

and refresh the Gitlab repository page. Are the recent changes present?

> yes

3. On Gitlab, add a comment at the bottom of [cube.js](cube.js) and commit the change. Back in your local terminal, type

```shell
$ git pull
```

Confirm that the changes made on Gitlab are present locally.

4. Add, commit and push any remaining files (from `git status`) to Gitlab.
