#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Base58 alphabet
#define BASE58_ALPHABET "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
#define BASE58_ALPHABET_SIZE 58

// Helper function to reverse a byte array
void byteArrReverse(unsigned char *bytes, int length) {
    int i;
    unsigned char temp;
    for (i = 0; i < length / 2; i++) {
        temp = bytes[i];
        bytes[i] = bytes[length - i - 1];
        bytes[length - i - 1] = temp;
    }
}

// Helper function to convert a value to base58 character
char base58Char(int value) {
    return BASE58_ALPHABET[value];
}

// Helper function to convert a base58 character to its value
int base58Value(char c) {
    const char *str = BASE58_ALPHABET;
    int index = 0;
    while (*str) {
        if (c == *str)
            return index;
        str++;
        index++;
    }
    return -1; // Invalid character
}

// Function to divide the byte array by 58 and get the remainder
void divideBy58(unsigned char *bytes, int *length, int *remainder) {
    int temp = 0;
    for (int i = 0; i < *length; i++) {
        temp = temp * 256 + bytes[i];
        bytes[i] = temp / 58;
        temp = temp % 58;
    }
    // Remove leading zeros in the quotient
    while (*length > 0 && bytes[*length - 1] == 0)
        (*length)--;
    *remainder = temp;
}

// Function to encode a byte array to base58 string
char *base58Encode(const unsigned char *input, int inputLength) {
    int leadingZeros = 0;
    while (leadingZeros < inputLength && input[leadingZeros] == 0)
        leadingZeros++;

    int length = inputLength - leadingZeros;
    unsigned char *bytes = (unsigned char *)malloc(length);
    memcpy(bytes, input + leadingZeros, length);
    byteArrReverse(bytes, length);

    int quotientLength = length;
    int remainder;
    char *result = (char *)malloc(length * 2); // Allocate enough space
    int resultIndex = 0;

    while (quotientLength > 0) {
        divideBy58(bytes, &quotientLength, &remainder);
        result[resultIndex++] = base58Char(remainder);
    }
    // Add leading '1's for leading zeros
    for (int i = 0; i < leadingZeros; i++)
        result[resultIndex++] = '1';
    result[resultIndex] = '\0';
    byteArrReverse((unsigned char *)result, resultIndex);

    free(bytes);
    return result;
}

// Function to decode a base58 string to byte array
unsigned char *base58Decode(const char *encoded, int *outputLength) {
    int leadingOnes = 0;
    int length = strlen(encoded);

    // Count leading '1's
    while (encoded[leadingOnes] == '1' && encoded[leadingOnes] != '\0')
        leadingOnes++;

    // Initialize a big integer to hold the decoded value
    int bigInt[256] = {0};
    int bigIntLength = 0;

    for (int i = leadingOnes; i < length; i++) {
        int c = base58Value(encoded[i]);
        if (c == -1) {
            *outputLength = 0;
            return NULL;
        }
        int carry = c;
        for (int j = 0; j < bigIntLength || carry; j++) {
            int temp = bigInt[j] * 58 + carry;
            bigInt[j] = temp % 256;
            carry = temp / 256;
            if (temp != 0 || j < bigIntLength)
                bigIntLength = j + 1;
        }
    }

    // Allocate memory for the output bytes, including leading zeros
    *outputLength = bigIntLength + leadingOnes;
    unsigned char *output = (unsigned char *)malloc(*outputLength);
    if (output == NULL) {
        *outputLength = 0;
        return NULL;
    }
    // Copy bigInt to output, starting from the end
    for (int j = 0; j < bigIntLength; j++)
        output[leadingOnes + j] = bigInt[j];
    // Add leading zeros
    for (int j = 0; j < leadingOnes; j++)
        output[j] = 0;

    return output;
}

char *expander(const char *input, int len)
{
    int length = strlen(input);
    char *expanded = (char *)malloc(len + 1);
    if (expanded == NULL) {
        return NULL;
    }
    if (length >= len) {
        strncpy(expanded, input, len);
    } else {
        strncpy(expanded, input, length);
        for (int i = length; i < len; i++) {
            expanded[i] = 'a';
        }
    }
    expanded[len] = '\0';
    return expanded;
}

char *encode_string(const char *input)
{
    char *expanded = expander(input, 33);
    if (expanded == NULL)
        return NULL;
    char *encoded = base58Encode((unsigned char *)expanded, 33);
    free(expanded);
    return encoded;
}

char *decode_to_string(const char *encoded) {
    int outputLength;
    unsigned char *decoded = base58Decode(encoded, &outputLength);
    if (decoded == NULL) {
        return NULL;
    }
    char *result = (char *)malloc(outputLength + 1);
    memcpy(result, decoded, outputLength);
    result[outputLength] = '\0';
    free(decoded);
    return result;
}

#include <string.h>

int cmp(const char *str1, const char *str2)
{
    while (*str1 && *str2 && *str1 == *str2)
    {
        str1++;
        str2++;
    }
    return *(const unsigned char *)str1 - *(const unsigned char *)str2;
}

int main(int argc, char **argv)
{
    // const char *input = "42HN{65a8e27d8879283831b664bd8b7f0ad4}";
    // KXEfPQmjUpRBKjAPPK6Hxx6LyVudZXa3ynCUfc1vfkjmqU25m1y5
    // VsoEvndbVhXUhEuSYD9FgXWrTWDN7cYitWkgnkuydV7ho
    // 65a8e27d8879283831b664bd8b7f0ad4a
    printf("%s\n", argv[0]);
    if (strcmp(argv[0], "./yeet") || argc < 2)
    {
        printf("Yeet!\n");
        return (1);
    }
    char *encoded = encode_string(argv[1]);
    // printf("Encoded: %s\n", encoded);

    if (!cmp(encoded, "VsoEvndbVhXUhEuSYD9FgXWrTWDN7cYitWkgnkuydV7ho"))
        printf("good job!");
    // char *decoded = decode_to_string(encoded);
    // printf("Decoded: %s\n", decoded);

    free(encoded);
    // free(decoded);
    return 0;
}
