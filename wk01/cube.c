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
    printf("The cube of the number you have entered is %d.\n", result);

    return EXIT_SUCCESS;
}

int cube(int x) {
    return x * x * x;
}
