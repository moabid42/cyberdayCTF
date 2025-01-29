import string

def rot_n(text, n):
    result = []
    for char in text:
        if char in string.ascii_lowercase:
            result.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif char in string.ascii_uppercase:
            result.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def main():
    plaintext = "42HN{REDACTED}"
    ciphertext = plaintext
    for i in range(800):
        ciphertext = rot_n(ciphertext, i + 1)
    print("ROTen Challenge")
    print("================")
    print("Ciphertext:")
    print(ciphertext)
    print("\nCan you recover the original flag?")

if __name__ == "__main__":
    main()
