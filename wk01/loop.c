#include<stdio.h>

int main(void) {
    char* items[] = {"apple", "oranges", "pears"};
    int i = 0;
    while (i < 3) {
        printf("%s\n", items[i]);
        i++;
    }
    return 0;
}
