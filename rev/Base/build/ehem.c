#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Our custom Base57 alphabet.
// We start with the common Base58 alphabet "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
// and remove one character (here we remove the final 'Z' from the uppercase section) to get exactly 57 characters.
static const char base57_alphabet[] = "123456789ABCDEFGHJKLMNPQRSTUVWXYabcdefghijkmnopqrstuvwxyz";
#define BASE 57

// Function: base57_encode
//   Encodes an array of bytes (of length len) into a null-terminated Base57 string.
//   The caller must free the returned string.
char *base57_encode(const unsigned char *input, size_t len) {
    // Count leading zeros.
    size_t zcount = 0;
    while (zcount < len && input[zcount] == 0)
        zcount++;

    // Allocate enough space for the encoding.
    // The size estimation is similar to the Base58 encoding algorithm.
    size_t size = (len - zcount) * 138 / 100 + 1;
    unsigned char *buffer = (unsigned char *)calloc(size, sizeof(unsigned char));
    if (!buffer) {
        return NULL;
    }

    // Process the bytes.
    for (size_t i = zcount; i < len; i++) {
        int carry = input[i];
        // Apply "bignum" division.
        for (size_t j = size; j-- > 0;) {
            carry += buffer[j] * 256;
            buffer[j] = carry % BASE;
            carry /= BASE;
        }
    }

    // Skip any leading zeroes in the buffer.
    size_t i = 0;
    while (i < size && buffer[i] == 0)
        i++;

    // Allocate the result string.
    size_t result_len = zcount + (size - i);
    char *result = (char *)malloc(result_len + 1);
    if (!result) {
        free(buffer);
        return NULL;
    }
    size_t k = 0;
    // Add the leading zeros as the first character of the alphabet.
    for (size_t j = 0; j < zcount; j++)
        result[k++] = base57_alphabet[0];
    // Convert the rest of the buffer to Base57 digits.
    for (; i < size; i++)
        result[k++] = base57_alphabet[buffer[i]];
    result[k] = '\0';

    free(buffer);
    return result;
}

// Function: base57_decode
//   Decodes a Base57-encoded null-terminated string into a newly allocated array of bytes.
//   The output length is stored in *outlen and the caller must free the returned array.
//   Returns NULL if an invalid character is encountered.
unsigned char *base57_decode(const char *input, size_t *outlen) {
    size_t input_len = strlen(input);
    
    // Count leading zeros (which are represented by the first alphabet char).
    size_t zcount = 0;
    while (zcount < input_len && input[zcount] == base57_alphabet[0])
        zcount++;
    
    // Allocate enough space for the decoded bytes.
    // The size estimation here uses a ratio similar to Base58 decoding.
    size_t size = (input_len - zcount) * 733 / 1000 + 1;
    unsigned char *buffer = (unsigned char *)calloc(size, sizeof(unsigned char));
    if (!buffer)
        return NULL;
    
    // Process each character.
    for (size_t i = zcount; i < input_len; i++) {
        // Find the index in the alphabet.
        const char *p = strchr(base57_alphabet, input[i]);
        if (!p) {
            // Invalid character found.
            free(buffer);
            return NULL;
        }
        int carry = p - base57_alphabet;
        // Multiply the current buffer by BASE and add carry.
        for (size_t j = size; j-- > 0;) {
            carry += buffer[j] * BASE;
            buffer[j] = carry % 256;
            carry /= 256;
        }
    }
    
    // Skip leading zeros in the buffer.
    size_t i = 0;
    while (i < size && buffer[i] == 0)
        i++;
    
    // Allocate the final output.
    *outlen = zcount + (size - i);
    unsigned char *result = (unsigned char *)malloc(*outlen);
    if (!result) {
        free(buffer);
        return NULL;
    }
    // Leading decoded zeros.
    memset(result, 0, zcount);
    memcpy(result + zcount, buffer + i, size - i);
    
    free(buffer);
    return result;
}

char expected[] = "KkVoC8XTiv9oppQjmHTviGsMukffs52scFVjUqEFW8yit5NAEBx1";
// 42HN{65a8e27d8879283831b664bd8b7f0ad4}

int main(int argc, char **argv)
{
    int var = 15;
    if(argc != 2) return 1;
    size_t flag_len = strlen(argv[1]);
    char *encoded = base57_encode((const unsigned char *)argv[1], flag_len);
    if (!encoded) {
        fprintf(stderr, "Encoding failed\n");
        return 1;
    }
    // printf("Encoded: %s\n", encoded);

    if(var == 14 && strcmp(encoded, expected) != 0) {
        printf("Incorrect encoded flag.\n");
        return 1;
    }
    printf("Correct!\n");

    // size_t decoded_len;
    // unsigned char *decoded = base57_decode(encoded, &decoded_len);
    // if (!decoded) {
    //     fprintf(stderr, "Decoding failed\n");
    //     free(encoded);
    //     return 1;
    // }
    // printf("Decoded: ");
    // fwrite(decoded, 1, decoded_len, stdout);
    // printf("\n");

    free(encoded);
    // free(decoded);
    return 0;
}
