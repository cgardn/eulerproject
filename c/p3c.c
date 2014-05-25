// Project Euler Problem 3 - C
// Created 5-24-2014

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long primefactor(long long);

long long primefactor(long long n) {

    int f = 2;
    int lf = 1;
    int mf = 0;
    //int n = strtol(fact, NULL, 0);

    if((n % 2) == 0) {
        lf = 2;
        while(n % 2 == 0) {
            n = n/2;
        }
    }
    else {
        lf = 1;
    }

    f = 3;
    mf = sqrt(n);
    
    while(n > 1 && f <= mf) {
        if(n % f == 0) {
            n = n/f;
            lf = f;
            while(n % f == 0) {
                n = n/f;
            }
            mf = sqrt(n);
        }
        f += 2;
    }

    if(n == 1) {
        return lf; }
    else {
        return n; }
}

int main(int argc, char *argv[]) {

    long long n = 0;

    n = primefactor(strtol(argv[1], NULL, 0));

    printf("Greatest prime factor: %lld\n", n);
    return 0;
}
