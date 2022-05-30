/**
 * A program to print out the values of a shopping list
 */

#include <stdio.h>

int main(void)
{
    char *shopping_list[] = {"apples", "oranges", "pears"};
    for (int i = 0; i < 3; i++)
    {
        printf("%s\n", shopping_list[i]);
    }
    return 0;
}
