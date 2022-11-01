///////////////////////////////
///// Number Brute Forcer /////
///////////////////////////////

#include <stdio.h>

void brute() {
    int target;
    int guess = 0;

    printf("Enter a number: ");
    scanf("%d", &target);

    while (0 == 0) {
        if (guess == target) {
            printf("The number is %d\n", guess);
            break;
        } else {
            printf("Tried %d\n", guess);
            guess++;
        }
    }
}

int main() {
    brute();
    return 0;
}
