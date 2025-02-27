#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>
#include <stdarg.h>

#define MAX_INPUT_LENGTH 29

int key[14] = {12, 13, 14, 18, 15, 12, 11, 10, 9, 8, 7, 6, 5, 4};

int *_(const char *string)
{
    int len = strlen(string);
    int *result = (int *)malloc((len + 1) * sizeof(int));

    if (!result) {
        printf("Memory allocation failed!\n");
        return NULL;
    }

    for (int i = 0; i < len; i++) {
        result[i] = string[i] ^ key[i % 14];
    }
    printf("\n");
    result[len] = '\0';

    return result;
}

int cmp(int *s1, int *s2)
{
    if (!s1 || !s2) return -1;
    int i = 0;

    while (s1[i] != '\0' && s2[i] != '\0')
    {
        if (s1[i] != s2[i]) {
            return 0;
        }
        i++;
    }

    return (s1[i] == '\0' && s2[i] == '\0') ? 1 : 0;
}

void appendChar(char *buf, char arg)
{
    size_t len = strlen(buf);
    buf[len] = arg;
    buf[len + 1] = '\0';
}

void c(char *buf, ...)
{
    va_list args;
    va_start (args, buf);

    char arg = va_arg(args, int);
    
    while( arg ) {
        appendChar(buf, arg);
        arg = va_arg(args, int);
    }

    va_end (args);
}


char *secondPart()
{
    char *str = malloc(512);
    c(str, '_', 's', '3', 'C', 'o', 'n', 'd', '_', 'W', 'o', 'r', 'd', '!', '}', 0);
    return str;
}

int main(int argc, char **argv)
{
    char input[MAX_INPUT_LENGTH];
    char firstHalf[MAX_INPUT_LENGTH / 2 + 1];
    char secondHalf[MAX_INPUT_LENGTH / 2 + 1];
    int length, mid;

    printf("Enter a string: ");
    if (fgets(input, MAX_INPUT_LENGTH, stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    input[strcspn(input, "\n")] = '\0';

    length = strlen(input);
    mid = (length + 1) / 2;

    strncpy(firstHalf, input, mid);
    firstHalf[mid] = '\0';

    strncpy(secondHalf, input + mid, length - mid);
    secondHalf[length - mid] = '\0';

    if (strcmp(firstHalf, "42HN{f1rst_r3V") == 0) {
    } else {
        return 0;
    }

    int *encryptedSecondHalf = _(secondHalf);
    int *encryptedTarget = _(secondPart());

    if (cmp(encryptedSecondHalf, encryptedTarget) == 1) {
        printf("Good job!\n");
    } else {
        printf("Yeet!\n");
    }

    free(encryptedSecondHalf);
    free(encryptedTarget);

    return 0;
}
