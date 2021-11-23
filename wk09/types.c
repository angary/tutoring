#include <stdio.h>

/**
 * C unlike python is a statically typed language
 * 
 * This means you have to specify if it is an int, double, char, pointer, etc
 * The benefit of "types" is that the computer can do checks on your code at
 * compile time for errors.
 * 
 * Anytime that you can get a computer to check your code automatically for
 * errors is REALLY GOOD!
 */

int get_val_from_array(int x) {
    /**
     * @param x: the index of the array (should be smaller than 6)
     * @return double the input
     */
    int array[] = {0, 1, 2, 4, 8, 16, 32};
    return array[x];
}

int main(void) {
    int val = get_val_from_array(1.1);
    printf("Value was %d\n", val);
    return 0;
}
