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
