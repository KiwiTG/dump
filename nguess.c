////////////////////////////////////////////
///// Number Guesser Game written in C /////
////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

void game() {

    srand(time(NULL));

    int minr = rand() % 10;
    int maxr = rand() % 10;

    int random = rand() % 100;
    int nmin = random - minr;
    int nmax = random + maxr;

    int guess;
    int answer = random;

    int correct = 0;
    int incorrect = 0;

    do {
        system("clear");

        printf("Correct: %d", correct);
        printf("\nIncorrect: %d", incorrect);
        printf("\nGuess the number between %d and %d: ", nmin, nmax);
        scanf("%d", &guess);

        if (guess < nmin) {
            printf("Out of range, too low!");
            sleep(1);
            incorrect++;
            system("clear");

        } else if (guess > nmax) {
            printf("Out of range, too high!");
            sleep(1);
            incorrect++;
            system("clear");
        }

        if (guess > answer) {
            printf("You guessed incorrectly, too high!");
            sleep(1);
            incorrect++;
            system("clear");
        } else if (guess < answer) {
            printf("You guessed incorrectly, too low!");
            sleep(1);
            incorrect++;
            system("clear");
        } else {
            printf("You guessed correctly!");
            sleep(2);
            correct++;
            system("clear");

        }
    } while (guess != answer);
}

int main() {
    while (0 == 0) {
        game();
    }
    return 0;
}
