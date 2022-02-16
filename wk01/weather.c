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
