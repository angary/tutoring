/*
 * [welcome.c]
 *
 * A simple program to print a welcome message
 * and print 10 numbers with information about
 * whether they are odd or even.
 */
#include <stdio.h>

#define SIZE 10

int main(void)
{

    char message[] = "Welcome to COMP1531!";
    printf("%s\n", message);

    printf("Numbers from 1 to %d\n", SIZE);
    for (int num = 1; num <= SIZE; num++)
    {
        if (num % 2 == 0)
        {
            printf("EVEN: %d\n", num);
        }
        else
        {
            printf("ODD:  %d\n", num);
        }
    }
    return 0;
}
