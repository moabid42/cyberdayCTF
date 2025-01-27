#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Base57 alphabet definition
const char base57Alphabet[] = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
const int base57Size = 57;

// Helper function to get base57 character
char base57Char(int value) {
    if (value < 0 || value >= base57Size) {
        return 0;
    }
    return base57Alphabet[value];
}

// Helper function to get value of a base57 character
int charToBase57Value(char c) {
    char* pos = strchr(base57Alphabet, c);
    if (pos == NULL) {
        return -1;
    }
    return pos - base57Alphabet;
}

// Encoding function
char* base57Encode(const unsigned char* input, int inputLength) {
    int leadingZeros = 0;
    while (leadingZeros < inputLength && input[leadingZeros] == 0) {
        leadingZeros++;
    }

    int dataLength = inputLength - leadingZeros;
    unsigned char* data = (unsigned char*)malloc(dataLength);
    if (!data) {
        return NULL;
    }
    memcpy(data, input + leadingZeros, dataLength);

    unsigned long long bigInt = 0;
    for (int i = 0; i < dataLength; i++) {
        bigInt = (bigInt << 8) + data[i];
    }

    free(data);

    char* result = (char*)malloc(dataLength * 2 + 1);
    if (!result) {
        return NULL;
    }
    int resultIndex = 0;

    do {
        int remainder = bigInt % 57;
        bigInt /= 57;
        result[resultIndex++] = base57Char(remainder);
    } while (bigInt > 0);

    for (int i = 0; i < leadingZeros; i++) {
        result[resultIndex++] = '1';
    }
    result[resultIndex] = '\0';

    // Reverse the result string
    for (int i = 0, j = resultIndex - 1; i < j; i++, j--) {
        char temp = result[i];
        result[i] = result[j];
        result[j] = temp;
    }

    return result;
}

// Decoding function
unsigned char* base57Decode(const char* encoded) {
    int length = strlen(encoded);
    char* reversed = (char*)malloc(length + 1);
    if (!reversed) {
        return NULL;
    }
    for (int i = 0; i < length; i++) {
        reversed[i] = encoded[length - 1 - i];
    }
    reversed[length] = '\0';

    int leadingOnes = 0;
    while (leadingOnes < length && reversed[leadingOnes] == '1') {
        leadingOnes++;
    }

    char* dataStr = (char*)malloc(length - leadingOnes + 1);
    if (!dataStr) {
        free(reversed);
        return NULL;
    }
    strncpy(dataStr, reversed + leadingOnes, length - leadingOnes);
    dataStr[length - leadingOnes] = '\0';

    unsigned long long bigInt = 0;
    for (int i = 0; i < strlen(dataStr); i++) {
        int value = charToBase57Value(dataStr[i]);
        if (value == -1) {
            free(reversed);
            free(dataStr);
            return NULL;
        }
        bigInt = bigInt * 57 + value;
    }

    free(reversed);
    free(dataStr);

    int dataLength = 0;
    unsigned long long temp = bigInt;
    while (temp > 0) {
        temp >>= 8;
        dataLength++;
    }
    dataLength = dataLength > 0 ? dataLength : 1;

    unsigned char* data = (unsigned char*)malloc(dataLength + leadingOnes);
    if (!data) {
        return NULL;
    }
    for (int i = dataLength - 1; i >= 0; i--) {
        data[i] = bigInt & 0xFF;
        bigInt >>= 8;
    }

    for (int i = 0; i < leadingOnes; i++) {
        data[dataLength + i] = 0;
    }

    return data;
}

int main() {
    const char* input = "hello world";
    int inputLength = 11; // "hello world" without null terminator

    // Encode
    char* encoded = base57Encode((const unsigned char*)input, inputLength);
    if (!encoded) {
        fprintf(stderr, "Encoding failed.\n");
        return 1;
    }
    printf("Encoded: %s\n", encoded);

    // Decode
    unsigned char* decoded = base57Decode(encoded);
    if (!decoded) {
        fprintf(stderr, "Decoding failed.\n");
        free(encoded);
        return 1;
    }

    // Verify decoding
    printf("Decoded: %s\n", decoded);

    // Check if decoded matches input
    int match = 1;
    for(int i = 0; i < inputLength; i++) {
        if(decoded[i] != input[i]) {
            match = 0;
            break;
        }
    }
    if(match) {
        printf("Decoding successful.\n");
    } else {
        printf("Decoding failed.\n");
    }

    // Free memory
    free(encoded);
    free(decoded);

    return 0;
}
