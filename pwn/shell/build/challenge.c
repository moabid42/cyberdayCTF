#include <stdio.h>
#include <stdlib.h>

void setup(void)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main(void)
{
    char shell[32];

    setup();

    printf("Give me a 🐚. ");
    printf("Don't worry I will save it in %p\n> ", shell);
    gets(shell);
    printf("So this is your shell: %s?\n", shell);

    return 0;
}
