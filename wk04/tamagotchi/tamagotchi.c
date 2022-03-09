#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


/**
 * Definition of a Tamagotchi struct
 * Note that we use typdef in C so that instead of saying "struct *tamagotchi"
 * we can say "Tamagotchi"
 */
struct tamagotchi {
    char name[50];
    bool is_dead;
    int age;
    int hunger;
    int boredom;
};
typedef struct tamagotchi *Tamagotchi;

/**
 * Function to initialize a tamagotchi
 * In Python, the declarations of variables in a class and the initialization
 * happen in the same function
 */
Tamagotchi init_tamagochi(char* name) {
    Tamagotchi tamagochi = malloc(sizeof(Tamagotchi));
    strcpy(tamagochi->name, name);
    tamagochi->is_dead = false;
    tamagochi->age = 0;
    tamagochi->hunger = 5;
    tamagochi->boredom = 0;
    return tamagochi;
}

/**
 * In C we typically write functions that take in a struct and interact with it
 * However, in Python, and other "Object Orientated Languages", we can define
 * "methods", which are essentially functions within a struct
 */
bool is_dead(Tamagotchi tamagotchi) {
    return tamagotchi->is_dead;
}

void feed(Tamagotchi tamagotchi) {
    if (is_dead(tamagotchi)) {
        return;
    }
    tamagotchi->hunger -= 3;

    if (tamagotchi->hunger < 0) {
        tamagotchi->hunger = 0;
        tamagotchi->is_dead = true;
    }
}

void play(Tamagotchi tamagotchi) {
    if (is_dead(tamagotchi)) {
        return;
    }

    tamagotchi->boredom -= 5;
    if (tamagotchi->boredom < 0) {
        tamagotchi->boredom = 0;
    }
}

void increment_time(Tamagotchi tamagotchi) {
    if (is_dead(tamagotchi)) {
        return;
    }
    tamagotchi->hunger += 1;
    tamagotchi->age += 1;
    tamagotchi->boredom += 1;

    if (tamagotchi->age > 15) {
        tamagotchi->is_dead = true;
    }
    if (tamagotchi->hunger > 10) {
        tamagotchi->is_dead = true;
    }
    if (tamagotchi->boredom > 10) {
        tamagotchi->is_dead = true;
    }
}


/**
 * If we want to "print" out the tamagotchi in C, we have to convert it into a
 * string, so we define this function "to_string()" which we call and it will
 * return a string representation of the tamagotchi. In Python we have special
 * functions, i.e. "__str__" that Python automatically calls when you print out
 * an object, i.e.
 * 
 * In C:
 *     printf("%s\n", to_string(tamagotchi));
 * 
 * In Python:
 *     print(tamagotchi)
 */
char* to_string(Tamagotchi tamagotchi) {
    char* str;
    if (is_dead(tamagotchi)) {
        asprintf(&str, "Name:    %s\nDEAD\n", tamagotchi->name);
    } else {
        asprintf(&str, "Name:    %s\nHunger:  %d\nBoredom: %d\nAge:     %d\n", tamagotchi->name, tamagotchi->hunger, tamagotchi->boredom, tamagotchi->age);
    }
    return str;
}

int main(void) {
    // Create the tamagotchi
    char* name;
    asprintf(&name, "Alfredo");
    Tamagotchi tamagotchi = init_tamagochi(name);

    // Print out their details
    printf("Just born!\n");
    printf("%s\n", to_string(tamagotchi));

    // Wait a bit and print out their details
    printf("After one day\n");
    increment_time(tamagotchi);
    printf("%s\n", to_string(tamagotchi));

    // Feed them, wait a bit and print out their details
    printf("Fed and after two days\n");
    feed(tamagotchi);
    increment_time(tamagotchi);
    printf("%s\n", to_string(tamagotchi));

    // Play with them, wait a bit and print out their details
    printf("Played with and after three days\n");
    play(tamagotchi);
    increment_time(tamagotchi);
    printf("%s\n", to_string(tamagotchi));

    // Wait out a very long time until it dies
    printf("Doing nothing for 20 days\n");
    for (int i = 0; i < 20; i++) {
        increment_time(tamagotchi);
    }
    printf("%s\n", to_string(tamagotchi));
    
    return 0;
}
