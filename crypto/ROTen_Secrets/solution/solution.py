import string

def rot_n(text, n):
    """Apply a ROT-N transformation to the input text."""
    result = []
    for char in text:
        if char in string.ascii_lowercase:
            result.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif char in string.ascii_uppercase:
            result.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


def solve_challenge(ciphertext):
    """Reverse the ROT800 transformation to recover the plaintext."""
    # Calculate the total rotation (sum of first 800 numbers mod 26)
    total_rotation = sum(range(1, 801)) % 26

    # Reverse the rotation
    plaintext = rot_n(ciphertext, -total_rotation)
    return plaintext

def main():
    ciphertext="42JP{7yk57gT_8qq}"
    plaintext=solve_challenge(ciphertext)
    print(plaintext)

if __name__ == "__main__":
    main()