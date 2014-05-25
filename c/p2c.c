// Project Euler Problem 2 - C
// Created 5-2-2014
// Sum of all Fibonacci numbers less than 4 million

#include <stdio.h>

void main() {

    int f = 0;
    int s = 1;
    int t = 0;
    int sums = 0;
    
    while(s <= 4000000) {
        if(s % 2 == 0) {
            sums += s;
        }

        t = f + s;
        f = s;
        s = t;
    }
    
    printf("Sum of Fibonacci series less than 4 million\n");
    printf("Total: %d\n", sums);
}
