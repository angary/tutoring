# Tutorial 1

## A. Introduction

Your tutor will run a short introduction/icebreaker activity.

## B. Problem Solving

1. Your tutor will help separate you into your project groups.

2. As a group, your tutor is going to give you a problem to solve in 10 minutes. At the end, they'll ask for your answers.

3. Come back together, and reflect with your tutor on how you came up with those answers and any assumptions you made during the exercise

## C. From C to Python: A Crash Course

### Part 1 - Basic Syntax, Input/Output, Conditionals & Control Flow

Consider the following C program.

```c
//
// A simple program to print out a recommendation
// for what to wear out given the weather
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

    char weather[50];
    scanf("%s", weather);

    if (strcmp(weather, "raining") == 0) {
        printf("You should wear a raincoat when you go out\n");
    } else if (strcmp(weather, "sunny") == 0) {
        printf("You should wear a hat when you go go out\n");
    } else {
        printf("Have a nice day!\n");
    }

    return EXIT_SUCCESS;
}
```

Convert this into a Python program.

As you write the program, discuss the following questions:
* Why don't we need to specify the type of a variable when we declare it?
* How do we denote code blocks in Python compared to C?
* How is the `print` function in Python different to `printf` in C?

### Part 2 - Looping and Lists

Write a program that stores a list of strings containing items in a shopping list.
* Use a `for-range` loop to print out each element in the list by index;
* Then change your program to be more Pythonic, using a `for-in` loop to print each element out instead.

### Part 3 - Functions

Consider the following C program.

```c
//
// A program that prints the cube of a given number
//

#include <stdio.h>
#include <stdlib.h>

int cube(int x);

int main(int argc, char *argv[]) {

    int number;
    printf("Please enter a number: ");
    scanf("%d", &number);

    int result = cube(number);
    printf("The cube of the number you have entered is %d\n.", result);

    return EXIT_SUCCESS;
}

int cube(int x) {
    return x * x * x;
}
```

Convert this into a Python program.

As you write the program, answer the following questions:
* Why don't Python programs need a `main` function?
* Why don't we need to write a function declaration for `cube` at the top of the file?
* What operator can we use instead of needing to write `x * x * x`?

## D. Git Fundamentals

* Type `git status` into the command line. What does it show?
* `git add` all of the files you have edited, and then enter `git status` again. What's different?
* `git commit` your changes and write a commit message. Enter `git status` and see what has changed again.
* `git push` all of your changes and view them on GitLab
* Make a change to a file on GitLab, and then `git pull` these changes
